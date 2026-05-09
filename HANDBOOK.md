# 📖 AI Tech Intel 知识手册

> 人类友好的知识导航 — 按主题/场景组织，不是按文件类型。
>
> 想了解项目背景？→ [ABOUT.md](ABOUT.md)
> 想让AI查资料？→ [index.md](index.md)

---

## 🤖 AI Agent 工程（2026年最热范式）

**一句话**：2026年AI行业核心矛盾已从"谁的模型更强"转向"谁的Harness（Agent编排系统）更稳"。

### 核心概念

| 文章 | 一句话 | 深度 |
|------|--------|------|
| [Harness方法论](concepts/harness-methodology.md) | Agent = Model + Harness。模型不变，Harness变，结果剧变。 | ⭐ 最核心 |
| [Agent Skills](concepts/agent-skills.md) | AI编程Agent的工程技能库，GitHub 10K+ Stars | 实用 |
| [RLHF](concepts/rlhf.md) | 人类反馈强化学习，让模型对齐人类偏好 | 基础 |
| [测试时计算](concepts/test-time-compute.md) | 推理时"多想一会"，而非只扩大模型规模 | 基础 |

### 谁在做这个

| 厂商 | 具体实践 | 关键数据 |
|------|----------|----------|
| [Anthropic](entities/anthropic.md) | 三Agent Harness（Planner-Generator-Evaluator）、Managed Agents | p50 TTFT↓60%，p95 TTFT↓90%+ |
| [OpenAI](entities/openai.md) | 团队交付100万行生产代码，零手写 | 100万行 |
| [Stripe](sources/stripe-minions-blueprint.md) | Minions Blueprint：确定性×智能体混合，状态机交替执行 | 每周1300+ PR，200+服务并行，400+ MCP工具 |
| [LangChain](sources/langchain-terminal-bench-20.md) | 仅优化Harness，Terminal Bench 2.0从52.8%→66.5% | 排名#30→#5 |
| [月之暗面](entities/moonshot.md) | Kimi K2.5 Agent Swarm：100子Agent并行，1500工具调用 | SWE-Bench 76.8% |

### 关键工具/协议

- **MCP（模型控制协议）** — 月下载9700万+，Agent工具访问标准
- **LangGraph** — 状态管理图
- **E2B** — 安全Agent沙箱
- **ADK** — Google Agent开发套件

---

## ⚡ AI 硬件与芯片

### GPU/加速器竞争格局

| 厂商 | 最新架构 | 关键数据 | 档案 |
|------|----------|----------|------|
| **NVIDIA** | Rubin (2026H2) + Feynman (2028) | Rubin Ultra 576GB HBM4 / 50 PFLOPS FP4 / 1nm级工艺 | [详情](entities/nvidia.md) |
| **AMD** | MI450 (2026H2) | TSMC 2nm / 432GB HBM4 / 40 PFLOPS FP4 / Meta $100B deal | [详情](entities/amd.md) |
| **Intel** | Gaudi | 追赶中 | [详情](entities/intel.md) |

### 内存技术

| 概念 | 一句话 | 档案 |
|------|--------|------|
| [HBM](concepts/hbm.md) | 高带宽内存，AI推理的带宽瓶颈，HBM4/4E演进中 | [详情](concepts/hbm.md) |
| [存算一体](concepts/processing-in-memory.md) | 在内存里做计算，突破冯·诺依曼瓶颈，60%+能耗花在数据搬运上 | [详情](concepts/processing-in-memory.md) |
| [近存运算](concepts/near-memory-computing.md) | 逻辑层紧邻DRAM/HBM，最接近产品化的存算方向 | [详情](concepts/near-memory-computing.md) |

### 先进封装

| 概念 | 一句话 | 档案 |
|------|--------|------|
| [Chiplet](concepts/chiplet.md) | 芯粒架构，后摩尔时代的模块化设计 | [详情](concepts/chiplet.md) |

### 关键厂商动态

- **[NVIDIA Feynman](sources/nvidia-feynman-gtc2026.md)** — TSMC A16 1.6nm工艺，SPR背面供电，GAA晶体管，硅光子集成，2028年商用
- **[NVIDIA Rubin](sources/nvidia-rubin-platform.md)** — HBM4 576GB，与Intel谈代工分散TSMC风险
- **[SK海力士 cHBM](sources/sk-hynix-ces2026.md)** — "Stream DQ Architecture"在HBM base die上集成计算逻辑，推理吞吐提升~7倍
- **[AMD MI450 vs Rubin](sources/amd-mi450-vs-rubin.md)** — 2nm vs 3nm工艺首次反超，432GB vs 576GB，Meta $100B deal

---

## 🧠 大模型厂商动态

### 闭源阵营

| 厂商 | 最新模型 | 关键动态 | 档案 |
|------|----------|----------|------|
| **Anthropic** | Claude 3.7 / Opus 4.7 | Harness Engineering领导者，三Agent架构，Managed Agents产品化 | [详情](entities/anthropic.md) |
| **OpenAI** | o4-mini / GPT-OSS-120B | 100万行AI写代码零手写；首个开源模型117B MoE | [详情](entities/openai.md) |
| **Google DeepMind** | Gemini 3.1 Pro/Flash | 1M上下文，多语言强 | [详情](entities/google-deepmind.md) |

### 开源/中国阵营

| 厂商 | 最新模型 | 关键动态 | 档案 |
|------|----------|----------|------|
| **月之暗面** | Kimi K2.5 | Agent Swarm 100子Agent，PARL训练，Modified MIT license，API价格屠夫 | [详情](entities/moonshot.md) |
| **DeepSeek** | R2 | 数学/代码专用，$0.27/M input，MIT license | [详情](entities/deepseek.md) |
| **Meta** | Llama 4 | 更大规模Dense模型，未开源同等规模 | [详情](entities/meta.md) |

---

## 🔧 开源工具与项目

| 项目 | 作者 | 一句话 | 档案 |
|------|------|--------|------|
| **ds4** | [antirez](entities/antirez.md) (Redis作者) | DeepSeek V4 Flash专用本地推理引擎，C语言编写，零依赖 | [详情](concepts/ds4.md) |
| **agent-skills** | [Addy Osmani](entities/addy-osmani.md) | AI编程Agent技能库，52.8%→66.5% Harness优化实验 | [详情](concepts/agent-skills.md) |
| **llm-wiki** | [Pratiyush](entities/pratiyush.md) | LLM Wiki模式参考实现，本知识库的模式来源 | [详情](concepts/llm-wiki-pattern.md) |

---

## 👤 值得关注的人物

| 人物 | 身份 | 最近关注点 | 档案 |
|------|------|----------|------|
| **Andrej Karpathy** | ex-Tesla/OpenAI，Eureka Labs | LLM Wiki模式、AI教育、Harness Engineering | [详情](entities/andrej-karpathy.md) |
| **Addy Osmani** | Google Chrome，AI Agent工程 | agent-skills项目、前端性能+AI | [详情](entities/addy-osmani.md) |
| **antirez** | Redis作者 | ds4推理引擎、C语言极致优化 | [详情](entities/antirez.md) |
| **Pratiyush** | 独立开发者 | llm-wiki模式、AI知识管理 | [详情](entities/pratiyush.md) |

---

## 📰 每日动态

| 日期 | 一句话总结 | 详情 |
|------|-----------|------|
| [2026-05-09](weekly-digest/2026-05-09.md) | Harness工程化成为核心范式、NVIDIA GTC 2026双架构发布、存算一体走向产品前夜 | [完整版](weekly-digest/2026-05-09.md) |

> 每天早上 09:30 微信推送简报。`weekly-digest/` 目录有每日完整版。

---

## 📚 知识库方法

| 概念 | 一句话 | 档案 |
|------|--------|------|
| [LLM Wiki模式](concepts/llm-wiki-pattern.md) | 增量式维护的结构化知识库，实体+概念+源文件三层结构 | [详情](concepts/llm-wiki-pattern.md) |

---

## 🗂️ 按文件类型索引（备用）

如果你习惯按文件类型查找：

- **厂商实体** → `entities/` 目录（19个文件）
- **技术概念** → `concepts/` 目录（10个文件）
- **源文件摘要** → `sources/` 目录（10个文件）
- **每日摘要** → `weekly-digest/` 目录
- **机器索引** → [index.md](index.md)

---

*最后更新：2026-05-09*
