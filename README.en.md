<h1 align="center">Chunjie Chen · ChenCJ</h1>

<p align="center">
  <b>AI Agent Engineer</b> — building agents you can ship, regress, and audit
</p>

<p align="center">
  <img alt="Base" src="https://img.shields.io/badge/Base-Xiamen,_China-0A66C2?style=flat-square">
  <img alt="Focus" src="https://img.shields.io/badge/Focus-Agent_Infra_%7C_Eval-5B5BD6?style=flat-square">
  <a href="mailto:2503693261@qq.com"><img alt="Email" src="https://img.shields.io/badge/Email-2503693261%40qq.com-D14836?style=flat-square&logo=maildotru&logoColor=white"></a>
</p>

<p align="center">
  <a href="./README.md">中文</a> · <b>English</b>
</p>

---

## 🧭 About

I build agents for a commercial AI product, and open-source infrastructure for evaluating them.

What interests me isn't whether an agent demos well — it's what happens after it ships. When the model, the prompt, the tools or the context change, does the behavior still hold? And when something breaks, can you trace it back through evidence?

Three ideas my work keeps returning to:

- **Push non-determinism down into deterministic constraints** — capability boundaries, version gates and argument validation belong in the architecture, not in a prompt you hope the model honors
- **Connection lifetime ≠ task lifetime** — disconnects, cancellations and pod restarts all have to be recoverable
- **`completed ≠ pass`** — a verdict has to cite immutable evidence

---

## 🔭 What I'm working on

**Day job** — agent development on a commercial AI product team: intent routing, capability boundaries, prompt architecture, tool contracts and runtime infrastructure. Alongside it I'm building a multi-agent evaluation and observability platform that acts as the regression and release-gating workbench for those agents.

Four main tracks:

| Area | What I do |
|---|---|
| **Intent routing & capability gating** | Moving "should the model be doing this at all" out of the prompt and into registries: a deterministic trigger registry (literal match routes directly) → a semantic boundary registry (natural-language patterns → candidate tools) → an LLM capability judge as the fallback (verdict canonicalization, timeouts, kill switch). **Every rule carries an `evidence` field** recording which production incident and which version of the capability catalog it came from — rules grow out of bugs, not out of guesswork. The registries ship with a standalone validator; the dispatch pipeline has explicit phase and failure-kind enums |
| **Observability** | Three layers: a trace-id middleware registered outermost → canonical logs plus bounded diagnostics → end-to-end Langfuse tracing. Bounded diagnostics give every field a byte budget, redact automatically, hash stably and buffer per turn — and **the diagnostic pipeline monitors its own health**. On the alerting side the work is governance, not forwarding: four-part cards (title / conclusion / next steps), rate limiting, error aggregation, per-environment isolation and a 24-hour digest |
| **Evaluation loop & dev pipeline** | 11 hand-built agent skills that interlock into a loop: three triage entry points (runtime log / session store / error dump) → bug archive → mine cases from real sessions → build cases → run regressions → write findings back into living docs. The skills reach my evaluation platform over MCP, so a coding agent drives fixes from real evaluation data |
| **Runtime & context engineering** | Resumable turns (a dropped connection doesn't kill the background task; cursor-based replay), cancellation semantics, a tool-version triple with inheritance chains and channel filtering, immutable agent release fingerprints; tool results past a threshold get recursively compressed and fetched back by reference, taking **token cost from linear to constant** |

**Open source** — the same methodology, made reproducible in public: [AgentRig](https://github.com/ChenCJ-io/agentrig) handles regression evaluation and release gating, [EditFlow Demo Agent](https://github.com/ChenCJ-io/editflow-demo-agent) is its public target under test. Together they form a complete demo that depends on no private assets and costs nothing to reproduce.

**Before that** — a multi-agent chaos-engineering system at **Nanjing Zhengfeng Information Technology**: six specialist agents orchestrated as a parallel DAG on Go + EINO (intent recognition / risk analysis / scenario recommendation / parameter generation / impact assessment / report generation), over a three-tier knowledge graph (atomic faults / system architecture / risk scenarios — 500+ faults, 200+ scenarios) with hybrid vector + graph + BGE-rerank retrieval that lifted recall accuracy from 62% to 89%. Running in a securities client's production environment. The Go / Neo4j / Faiss badges below come from this.

---

## 🌱 Open source

<!-- oss-intro:start -->**19 merged upstream PRs**<!-- oss-intro:end -->, clustered around three themes: **defensive design against external contracts**, **correlatable observability**, and **incremental-data consistency**. Each one is a problem from the same domain as my day job — solved again in someone else's codebase.

<!-- oss-table:start -->
| Upstream | Track | Stars | Merged | Representative work |
|---|---|---:|---:|---|
| [modelscope/evalscope](https://github.com/modelscope/evalscope) | Capability gating · Eval loop | 3.4k | **7** | [#1712](https://github.com/modelscope/evalscope/pull/1712) validate tool-call arguments against the advertised schema · [#1718](https://github.com/modelscope/evalscope/pull/1718)/[#1719](https://github.com/modelscope/evalscope/pull/1719) sandbox stdin isolation and forwarding · [#1698](https://github.com/modelscope/evalscope/pull/1698) record upstream generate failures on the agent trace |
| [latitude-dev/latitude-llm](https://github.com/latitude-dev/latitude-llm) | Observability | 4.6k | **2** | [#4369](https://github.com/latitude-dev/latitude-llm/pull/4369) let dispatch webhooks return external run metadata, linking a dispatch record to the agent run it actually started (partial failure doesn't escalate; bounded reads) · [#4615](https://github.com/latitude-dev/latitude-llm/pull/4615) emit MCP input schemas in input mode |
| [juejin-cn/juejin-usage](https://github.com/juejin-cn/juejin-usage) | Observability (metering & attribution) | 120 | **10** | [#127](https://github.com/juejin-cn/juejin-usage/pull/127) fix a macOS-only fixture and sandbox two full sync rounds — CI moved to a dual-platform matrix, suite 64s → 1.4s · [#98](https://github.com/juejin-cn/juejin-usage/pull/98) add cache pricing so cached tokens stop billing at zero · [#90](https://github.com/juejin-cn/juejin-usage/pull/90)/[#92](https://github.com/juejin-cn/juejin-usage/pull/92) project attribution and double counting across incremental reads |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Runtime & context | 42k | in review | **8 issues + 9 PRs** found while running it in production: [#8341](https://github.com/agno-agi/agno/pull/8341) `session_state` drift across continued runs · [#8344](https://github.com/agno-agi/agno/pull/8344) sanitize historical tool-call arguments for OpenAI-compatible providers · [#9795](https://github.com/agno-agi/agno/pull/9795) bounded JSON-pointer reads from offloaded results |
<!-- oss-table:end -->

<sub>The fourth track — **intent routing** — has no upstream counterpart; its public counterpart is the routing-baseline regression in EditFlow Demo Agent below. Counts are PRs merged into upstream repositories, excluding my own; auto-updated <!-- oss-asof:start -->2026-09-16<!-- oss-asof:end -->.</sub>

---

## 📦 Projects

<table>
<tr><td width="50%" valign="top">

### [AgentRig](https://github.com/ChenCJ-io/agentrig)
`Python` · `MIT` · `alpha`

MCP-native infrastructure for agent regression evaluation and controlled release gating.

- Three agents with separated duties: Manager orchestrates, Curator produces controlled tool results, Judge rules on frozen evidence — each with its own tool surface and credentials
- `completed ≠ pass`: run status, rules, Judge and external-controller verdicts stay explicitly separate
- Controlled provider chain: Fixture → Sample → Curator → Real Tool
- Immutable run snapshots, RunEvents and I/O hashes form the evidence chain

</td><td width="50%" valign="top">

### [EditFlow Demo Agent](https://github.com/ChenCJ-io/editflow-demo-agent)
`Python` · `MIT`

A public agent that exists to be AgentRig's **real target under test**.

- Single ReAct agent on Agno with five native pause/resume `external_execution` tools
- PostgreSQL persistence for both completed and suspended runs
- A tag freezes a deliberately loose routing baseline, for before/candidate prompt-regression demos
- Calls no image APIs — reproducing it costs nothing

</td></tr>
<tr><td width="50%" valign="top">

### [qoder-skill-git-commit](https://github.com/ChenCJ-io/qoder-skill-git-commit)
`Python` · `OpenVINO`

A fully local git commit generator — data never leaves the machine.

- Qwen2.5-Coder on OpenVINO / NPU, on-device inference
- Follows the Agent Skills protocol; loads in Qoder, ModelScope or Claude Code
- Built for the Production AI Skills competition (Intel × ModelScope)

</td><td width="50%" valign="top">

### In flight
`WIP`

- Codex Capacity Guard — resumes after a capacity error in the **same conversation, same model**
- More upstream merged PRs on the same themes: contract defense and observability correlation
- Taking AgentRig from competition preview to something external teams can adopt

</td></tr>
</table>

---

## 🧰 Stack

**Languages & backend**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy_async-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Agents & LLMs**

![Agno](https://img.shields.io/badge/Agno-1B1B1F?style=flat-square)
![EINO](https://img.shields.io/badge/EINO-1B1B1F?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-5B5BD6?style=flat-square)
![Claude](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Qwen](https://img.shields.io/badge/Qwen-615CED?style=flat-square&logo=alibabacloud&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=flat-square)

**Data & observability**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![Faiss](https://img.shields.io/badge/Faiss-0467DF?style=flat-square)
![Langfuse](https://img.shields.io/badge/Langfuse-101014?style=flat-square)

**Frontend & testing**

![React](https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

**Engineering**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white)
![vLLM](https://img.shields.io/badge/vLLM-FDBA74?style=flat-square)

---

## 📊 GitHub

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=ChenCJ-io&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&title_color=5B5BD6&icon_color=5B5BD6">
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ChenCJ-io&layout=compact&hide_border=true&title_color=5B5BD6">
</p>

---

## 📮 Get in touch

<a href="mailto:2503693261@qq.com"><img alt="Email" src="https://img.shields.io/badge/Email-2503693261%40qq.com-D14836?style=for-the-badge&logo=maildotru&logoColor=white"></a>

<sub>Always happy to talk about agent infrastructure, evaluation systems, and context / cost engineering.</sub>
