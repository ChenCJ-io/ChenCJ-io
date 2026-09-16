<h1 align="center">陈纯杰 · ChenCJ</h1>

<p align="center">
  <b>AI Agent 工程师</b> — 做能上线、能回归、能追责的 Agent 系统
</p>

<p align="center">
  <img alt="Base" src="https://img.shields.io/badge/Base-厦门_Xiamen-0A66C2?style=flat-square">
  <img alt="Focus" src="https://img.shields.io/badge/Focus-Agent_Infra_%7C_Eval-5B5BD6?style=flat-square">
  <a href="mailto:2503693261@qq.com"><img alt="Email" src="https://img.shields.io/badge/Email-2503693261%40qq.com-D14836?style=flat-square&logo=maildotru&logoColor=white"></a>
</p>

<p align="center">
  <b>中文</b> · <a href="./README.en.md">English</a>
</p>

---

## 🧭 关于我

做商业 AI 产品的 Agent 研发，也做开源的 Agent 评测基建。

我关心的不是「Agent 能不能跑通 demo」，而是**上线之后怎么办**——模型、提示词、工具、上下文任意一处变化，行为还满不满足业务约束；出问题时能不能沿证据查回去。

所以我的工作基本围绕三件事：

- **把不确定性下沉为确定性约束** — 能力边界、版本门控、参数校验放进架构，而不是靠提示词祈祷
- **让一次对话可恢复、可追溯** — 连接生命周期 ≠ 任务生命周期；断线、取消、跨 Pod 都得接得回来
- **用评测驱动缺陷治理** — `completed ≠ pass`，结论必须引用不可变证据

---

## 🔭 现在在做

**本职** — 在一家商业 AI 产品团队做 Agent 研发：从意图分发、能力边界、提示词组织，到工具契约与运行时基建。同时在建一个多 Agent 评测与观测平台，给这些 Agent 当回归与守门的工作台。

四条主线：

| 能力 | 我做的 |
|---|---|
| **意图分发与能力门禁** | 把「模型该不该做这件事」从提示词搬进注册表：确定性触发表（词面命中直接路由）→ 语义边界表（自然语言 pattern → 候选工具）→ LLM 能力判定兜底（verdict 规范化 + 超时 + 可开关）。**每条规则带 `evidence` 字段**，写明它是从哪次线上现象、哪个版本的能力口径长出来的——规则不是拍脑袋写的，是从 bug 里长出来的。注册表配独立校验脚本，派发管线有阶段枚举与失败分类 |
| **可观测性** | 三层：trace_id 中间件（注册在最外层）→ canonical 日志 + 受限诊断 → Langfuse 全链路。受限诊断给每个字段字节预算、自动脱敏、稳定 hash、按轮次缓冲，**诊断管线自身还有健康度监控**。告警侧做的是治理不是转发：四段式卡片（标题 / 结论 / 下一步）、频率限制、错误聚合、按环境隔离、24 小时日报 |
| **评测闭环与研发流水线** | 11 个自建 Agent Skill 咬合成闭环：排障三入口（运行日志 / 会话库 / 错误 JSON）→ Bug 归档 → 从真实会话挖用例 → 建用例 → 跑回归 → 落地后回写活文档。Skill 通过 MCP 直连自建评测平台取数与判定，让 coding agent 以真实评测数据驱动修复 |
| **运行时与上下文工程** | 可恢复 Turn（连接断开不终止后台任务，游标续传）、取消语义、工具版本三元组 + 继承链 + 通道裁剪、不可变 Agent Release 版本指纹；工具结果超阈值递归压缩 + 按需引用取回，**Token 开销从线性降到常数** |

**开源** — 把同一套方法论做成可复现的公开基建：[AgentRig](https://github.com/ChenCJ-io/agentrig) 负责回归评测与发布门禁，[EditFlow Demo Agent](https://github.com/ChenCJ-io/editflow-demo-agent) 给它当公开被测对象。两者组成一个不依赖任何私有资产、复现成本为零的完整演示。

**此前** — 在**南京争锋信息科技**做 Multi-Agent 混沌工程智能体：Go + EINO 编排 6 个专业 Agent（意图识别 / 风险分析 / 场景推荐 / 参数生成 / 影响评估 / 报告生成）DAG 并行，三层知识图谱（原子故障 / 系统架构 / 风险场景，覆盖 500+ 故障与 200+ 场景）配向量 + 图谱 + BGE 重排混合检索，召回准确率 62% → 89%，已在证券客户生产环境运行。技术栈里的 Go / Neo4j / Faiss 来自这段。

---

## 🌱 开源贡献

<!-- oss-intro:start -->**19 个已合入上游的 PR**<!-- oss-intro:end -->，集中在三个主题：**外部契约的防御式设计**、**可关联的可观测性**、**增量数据的一致性**。都是和本职同一问题域的问题——在别人的代码库里复现一遍。

<!-- oss-table:start -->
| 上游项目 | 对应主线 | Star | 已合入 | 代表工作 |
|---|---|---:|---:|---|
| [modelscope/evalscope](https://github.com/modelscope/evalscope) | 能力门禁 · 评测闭环 | 3.4k | **7** | [#1712](https://github.com/modelscope/evalscope/pull/1712) 按声明的 schema 校验 tool-call 参数 · [#1718](https://github.com/modelscope/evalscope/pull/1718)/[#1719](https://github.com/modelscope/evalscope/pull/1719) 沙箱 stdin 隔离与转发 · [#1698](https://github.com/modelscope/evalscope/pull/1698) 上游 generate 失败落进 agent trace |
| [latitude-dev/latitude-llm](https://github.com/latitude-dev/latitude-llm) | 可观测性 | 4.6k | **2** | [#4369](https://github.com/latitude-dev/latitude-llm/pull/4369) webhook 回执携带外部 run 元数据，把派发记录关联到真正启动的 agent run（部分失败不升级 + 有界读取）· [#4615](https://github.com/latitude-dev/latitude-llm/pull/4615) input 模式下输出 MCP input schema |
| [juejin-cn/juejin-usage](https://github.com/juejin-cn/juejin-usage) | 可观测性（计量与归因） | 120 | **10** | [#127](https://github.com/juejin-cn/juejin-usage/pull/127) 修掉只在 macOS 过的 fixture + 整轮 sync 上沙箱，CI 转双平台矩阵（套件 64s → 1.4s）· [#98](https://github.com/juejin-cn/juejin-usage/pull/98) 补缓存单价，命中缓存的 Token 不再按 0 计费 · [#90](https://github.com/juejin-cn/juejin-usage/pull/90)/[#92](https://github.com/juejin-cn/juejin-usage/pull/92) 增量续读的项目归属与双倍计数 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 运行时与上下文 | 42k | 评审中 | 生产使用中定位的 **8 个 issue + 9 个 PR**：[#8341](https://github.com/agno-agi/agno/pull/8341) continued run 的 session_state 漂移 · [#8344](https://github.com/agno-agi/agno/pull/8344) OpenAI 兼容端历史 tool_call 参数消毒 · [#9795](https://github.com/agno-agi/agno/pull/9795) offload 结果的有界 JSON-pointer 读取 |
<!-- oss-table:end -->

<sub>剩下的**意图分发**一条上游没有对应物，它的公开对应物是下面 EditFlow Demo Agent 的路由基线回归。计数为上游仓库已 merge 的 PR，不含自有仓库；数据自动更新于 <!-- oss-asof:start -->2026-09-16<!-- oss-asof:end -->。</sub>

---

## 📦 自建项目

<table>
<tr><td width="50%" valign="top">

### [AgentRig](https://github.com/ChenCJ-io/agentrig)
`Python` · `MIT` · `alpha`

MCP 原生的 Agent 回归评测与受控发布门禁基础设施。

- 三 Agent 职责隔离：Manager 编排 / Curator 产受控工具结果 / Judge 依冻结证据裁决，各自独立工具面与凭据
- `completed ≠ pass`：运行状态、规则、Judge、外部控制方结论四者显式分离
- 受控 Provider 链 Fixture → Sample → Curator → Real Tool
- 不可变运行快照 + RunEvent + 输入输出 Hash 构成证据链

</td><td width="50%" valign="top">

### [EditFlow Demo Agent](https://github.com/ChenCJ-io/editflow-demo-agent)
`Python` · `MIT`

给 AgentRig 当**真实被测对象**的公开 Agent。

- Agno 单 ReAct Agent，5 个 `external_execution` 原生暂停/续跑工具
- PostgreSQL 持久化已完成与暂停中的 run
- 用 tag 冻结「故意宽泛的路由基线」，做 Before/Candidate 提示词回归演示
- 不调用任何图像 API，复现成本为零

</td></tr>
<tr><td width="50%" valign="top">

### [qoder-skill-git-commit](https://github.com/ChenCJ-io/qoder-skill-git-commit)
`Python` · `OpenVINO`

纯本地的 Git commit 生成 Skill，数据不出本机。

- Qwen2.5-Coder + OpenVINO / NPU 端侧推理
- 遵循 Agent Skills 协议，Qoder / 魔搭 / Claude Code 通用
- Production AI Skills 大赛（英特尔 × 魔搭）参赛作品

</td><td width="50%" valign="top">

### 还在路上
`WIP`

- Codex Capacity Guard — 容量错误后在**同一会话、同一模型**续跑的插件
- 同主题继续攒上游 merged PR：契约防御 + 可观测关联
- AgentRig 从 competition preview 走向可被外部接入

</td></tr>
</table>

---

## 🧰 技术栈

**语言与后端**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy_async-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Agent 与大模型**

![Agno](https://img.shields.io/badge/Agno-1B1B1F?style=flat-square)
![EINO](https://img.shields.io/badge/EINO-1B1B1F?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-5B5BD6?style=flat-square)
![Claude](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Qwen](https://img.shields.io/badge/Qwen-615CED?style=flat-square&logo=alibabacloud&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=flat-square)

**数据与可观测**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![Faiss](https://img.shields.io/badge/Faiss-0467DF?style=flat-square)
![Langfuse](https://img.shields.io/badge/Langfuse-101014?style=flat-square)

**前端与测试**

![React](https://img.shields.io/badge/React_19-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

**工程**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white)
![vLLM](https://img.shields.io/badge/vLLM-FDBA74?style=flat-square)

---

## 📊 GitHub

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=ChenCJ-io&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&title_color=5B5BD6&icon_color=5B5BD6&locale=cn">
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ChenCJ-io&layout=compact&hide_border=true&title_color=5B5BD6&locale=cn">
</p>

---

## 📮 联系

<a href="mailto:2503693261@qq.com"><img alt="Email" src="https://img.shields.io/badge/Email-2503693261%40qq.com-D14836?style=for-the-badge&logo=maildotru&logoColor=white"></a>

<sub>对 Agent 基建、评测体系、上下文与成本工程的话题都感兴趣，欢迎交流。</sub>
