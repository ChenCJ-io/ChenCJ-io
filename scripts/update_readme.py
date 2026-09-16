#!/usr/bin/env python3
"""Refresh the open-source table in README.md / README.en.md from the GitHub API.

Prose lives in data/upstream.json; only the numbers (stars, merged counts) come
from the API, so editing wording never means touching this script.

Usage:
    GITHUB_TOKEN=... python scripts/update_readme.py [--check]

--check exits 1 when the files would change, without writing them.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "upstream.json"
API = "https://api.github.com"


def request(url: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-updater",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    for attempt in range(4):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=headers), timeout=30
            ) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            # Search API secondary rate limits answer 403/422; back off and retry.
            if exc.code in (403, 422, 429) and attempt < 3:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    raise RuntimeError(f"giving up on {url}")


def search_count(query: str) -> int:
    url = f"{API}/search/issues?q={urllib.parse.quote(query)}&per_page=1"
    return int(request(url)["total_count"])


def format_stars(count: int) -> str:
    if count >= 10_000:
        return f"{count / 1000:.0f}k"
    if count >= 1_000:
        return f"{count / 1000:.1f}k"
    return str(count)


def replace_marked(text: str, marker: str, body: str) -> str:
    pattern = re.compile(
        rf"(<!-- {re.escape(marker)}:start -->).*?(<!-- {re.escape(marker)}:end -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit(f"marker {marker} not found — did the README get rewritten?")
    return pattern.sub(lambda m: f"{m.group(1)}{body}{m.group(2)}", text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if files would change")
    args = parser.parse_args()

    config = json.loads(DATA.read_text(encoding="utf-8"))
    user = config["user"]

    rows = []
    total_merged = 0
    for entry in config["repos"]:
        repo = entry["repo"]
        stars = format_stars(request(f"{API}/repos/{repo}")["stargazers_count"])
        merged = search_count(f"repo:{repo} author:{user} is:pr is:merged")
        total_merged += merged

        counts = {"merged": merged}
        if entry["mode"] == "in_review":
            counts["prs"] = search_count(f"repo:{repo} author:{user} is:pr is:open")
            counts["issues"] = search_count(f"repo:{repo} author:{user} is:issue is:open")

        rows.append({"entry": entry, "stars": stars, "counts": counts})
        print(f"{repo}: {stars}★, merged={merged}", file=sys.stderr)

    changed = False
    for lang, meta in config["i18n"].items():
        path = ROOT / meta["file"]
        original = path.read_text(encoding="utf-8")

        lines = []
        for row in rows:
            entry, counts = row["entry"], row["counts"]
            template = meta["review_row"] if entry["mode"] == "in_review" else meta["merged_row"]
            lines.append(
                template.format(
                    repo=entry["repo"],
                    stars=row["stars"],
                    short=entry["short"][lang],
                    **counts,
                )
            )

        updated = replace_marked(original, "oss-table", "\n" + "\n".join(lines) + "\n")
        updated = replace_marked(
            updated, "oss-intro", meta["intro"].format(total=total_merged)
        )
        # Actions runs in UTC; pin to Asia/Shanghai so local and CI agree on the date.
        today = datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
        updated = replace_marked(updated, "oss-asof", today)

        if updated != original:
            changed = True
            if not args.check:
                path.write_text(updated, encoding="utf-8")
                print(f"updated {meta['file']}", file=sys.stderr)

    if args.check and changed:
        print("README is stale — run scripts/update_readme.py", file=sys.stderr)
        return 1
    if not changed:
        print("no changes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
