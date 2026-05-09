# AI Tech Intel 知识手册

> **知识编译**视角的概念图谱。按层级、依赖、学习路径组织，而非文件树。

---

## 快速跳转

### 📅 今日速递
- [2026年5月9日：Harness成为核心范式、NVIDIA双架构、存算一体产品前夜](digest/2026-05-09.md)

### 🤖 分支一：AI Agent 工程

| 层级 | 概念 | 一句话 | ⭐ | ⏱️ |
|------|------|--------|---|---|
| 前置 | [RLHF](agent-engineering/prereq/rlhf.md) | 让模型对齐人类偏好 | ⭐⭐ | 10min |
| 前置 | [测试时计算](agent-engineering/prereq/test-time-compute.md) | 推理时"多想一会" | ⭐⭐ | 10min |
| 根 | [Harness 方法论](agent-engineering/harness/README.md) | Agent = Model + Harness | ⭐⭐⭐ | 20min |
| 子 | [PEV 循环](agent-engineering/harness/pev-cycle.md) | 写计划→执行→验证→重试 | — | — |
| 子 | [三Agent架构](agent-engineering/harness/three-agent.md) | Planner + Generator + Evaluator | — | — |
| 子 | [五层架构](agent-engineering/harness/five-layers.md) | 验证层是最高影响层 | — | — |
| 子 | [Context Engineering](agent-engineering/harness/context-engineering.md) | 动态组装上下文 | — | — |
| 子 | [Cognitive Memory](agent-engineering/harness/cognitive-memory.md) | 存储"为什么" | — | — |
| 实践 | [Anthropic](agent-engineering/practices/anthropic.md) | 三Agent + Managed Agents | ⭐⭐⭐⭐ | — |
| 实践 | [OpenAI](agent-engineering/practices/openai.md) | 100万行零手写代码 | ⭐⭐⭐ | — |
| 实践 | [Stripe Minions](agent-engineering/practices/stripe.md) | 确定性×智能体混合 | ⭐⭐⭐⭐ | — |
| 实践 | [LangChain](agent-engineering/practices/langchain.md) | 仅优化Harness，52.8%→66.5% | ⭐⭐⭐ | — |
| 实践 | [月之暗面](agent-engineering/practices/moonshot.md) | 100子Agent并行 | ⭐⭐⭐⭐ | — |
| 工具 | [MCP](agent-engineering/tools/mcp.md) | 模型控制协议 | — | — |
| 工具 | [LangGraph](agent-engineering/tools/langgraph.md) | 状态管理图 | — | — |
| 延伸 | [Agent Skills](agent-engineering/extended/agent-skills.md) | AI编程Agent技能库 | ⭐⭐⭐ | — |

### ⚡ 分支二：AI 硬件与芯片

| 层级 | 概念 | 一句话 | ⭐ | ⏱️ |
|------|------|--------|---|---|
| 前置 | [冯·诺依曼瓶颈](hardware/prereq/memory-wall.md) | 60%+能耗花在数据搬运 | ⭐ | 5min |
| 根 | [存算一体](hardware/pim/README.md) | 在内存里做计算 | ⭐⭐⭐ | 20min |
| 子 | [近存运算](hardware/pim/near-memory.md) | 最接近产品化 | — | — |
| 子 | [存内计算](hardware/pim/compute-in-memory.md) | 实验室→原型 | — | — |
| 子 | [存内逻辑](hardware/pim/logic-in-memory.md) | 早期研究 | — | — |
| 根 | [HBM](hardware/hbm/README.md) | 高带宽内存，AI瓶颈 | ⭐⭐ | 15min |
| 子 | [HBM3E](hardware/hbm/hbm3e.md) | 当前主流 | — | — |
| 子 | [HBM4](hardware/hbm/hbm4.md) | 2026H2主力 | — | — |
| 子 | [cHBM](hardware/hbm/chbm.md) | 定制化HBM | — | — |
| 根 | [Chiplet](hardware/chiplet/README.md) | 芯粒模块化设计 | ⭐⭐ | 15min |
| 竞争 | [NVIDIA](hardware/competition/nvidia.md) | Rubin + Feynman双架构 | ⭐⭐⭐ | — |
| 竞争 | [AMD MI450](hardware/competition/amd.md) | 2nm工艺首次反超 | ⭐⭐⭐ | — |
| 竞争 | [内存厂商](hardware/competition/memory-vendors.md) | SK海力士 + 三星 | — | — |

### 🧠 分支三：大模型厂商

| 阵营 | 厂商 | 定位 |
|------|------|------|
| 闭源 | [Anthropic](vendors/closed/anthropic.md) | Harness领导者 |
| 闭源 | [OpenAI](vendors/closed/openai.md) | 规模+开源并重 |
| 闭源 | [Google DeepMind](vendors/closed/google.md) | 多语言+长上下文 |
| 开源 | [月之暗面](vendors/open-source/moonshot.md) | Agent Swarm |
| 开源 | [DeepSeek](vendors/open-source/deepseek.md) | 推理效率极致 |
| 开源 | [Meta](vendors/open-source/meta.md) | Llama+基础设施 |

### 🔧 分支四：开源与人物
- [ds4 本地推理引擎](open-source/ds4.md)
- [值得关注的人物](people/README.md)

---

*由 [OpenClaw](https://openclaw.ai) 自动维护*  
*GitHub：[large-cat/ai-tech-intel](https://github.com/large-cat/ai-tech-intel)*
