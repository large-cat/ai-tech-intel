# Q: 2026 年 AI 行业的核心范式转移是什么？

> 关联概念: [[Harness Methodology]], [[Agent Skills]], [[Test-Time Compute]]
> 关联实体: [[Anthropic]], [[OpenAI]], [[Stripe]], [[LangChain]], [[月之暗面]]
> 来源: [[sources/modern-harness-blueprint-2026]], [[sources/stripe-minions-blueprint]], [[sources/langchain-terminal-bench-20]], [[sources/moonshot-kimi-k25]]

## 一句话回答

从「谁的模型更强」转向「谁的 Harness（Agent 编排系统）更稳」。模型是基础能力，Harness 是工程杠杆。

## 范式转移的三重证据

### 证据 1：Anthropic 的三 Agent 架构成为生产标准

Anthropic 不再推销「Claude 4 比 GPT-5 强多少」，而是推广「三 Agent 架构让企业级部署更可靠」。

- Planner → Executor → Verifier 的闭环
- Managed Agents 让企业可以像配置 CI/CD 一样配置 AI 工作流

来源：[[sources/anthropic-three-agent-harness]]

### 证据 2：OpenAI 的 100 万行零手写代码

OpenAI 内部用 AI 写 AI 的基础设施，100 万行生产代码零手写。这说明：

- 模型能力已经足够让「AI 写代码」成为现实
- 但关键在于**如何编排**这些 AI 编码 Agent，而不是单个 Agent 的能力

来源：[[sources/openai-100m-lines]]

### 证据 3：Stripe 的 Minions Blueprint

Stripe 把支付基础设施的确定性（必须 100% 可靠）和智能体的灵活性（处理异常情况）结合起来：

- 400+ MCP 工具
- 200+ 服务并行
- 确定性工作流 + 智能体决策的混合架构

来源：[[sources/stripe-minions-blueprint]]

## 为什么是 2026 年？

| 年份 | 焦点 | 代表 |
|------|------|------|
| 2022-2023 | 模型能力爆发 | GPT-3.5 → GPT-4 |
| 2024 | 工具调用（Function Calling） | GPT-4 Turbo |
| 2025 | 多模态 + 长上下文 | GPT-4o, Claude 3 |
| **2026** | **Harness 工程化** | **三 Agent, MCP, Agent Skills** |

### 三个条件同时成熟

1. **模型可靠性**：GPT-4 级别模型已能稳定执行多步推理
2. **协议标准化**：MCP 让 Agent 之间能互操作
3. **企业需求**：不能再靠「提示工程运气」部署生产系统

## 与历史类比

| 年代 | 技术 | 工程化阶段 |
|------|------|-----------|
| 2010 | 云计算萌芽 | DevOps 诞生 |
| 2020 | LLM 萌芽 | Prompt Engineering |
| **2026** | **LLM 成熟** | **Harness Engineering** |

DevOps 解决的是「如何让软件可靠交付」，Harness Engineering 解决的是「如何让 AI 可靠协作」。

## 对开发者的影响

**以前**：学习 Prompt Engineering，尝试让单个模型做更多
**现在**：学习 Harness Engineering，设计多 Agent 协作架构

**核心技能转变**：
- 从「写更好的提示」→「设计 Agent 分工」
- 从「调模型参数」→「调 Harness 拓扑」
- 从「单轮对话」→「多轮状态管理」

## 延伸阅读

- [[syntheses/2026-ai-industry-trends]] — 2026 年 AI 行业趋势综合
- [[syntheses/agent-engineering-overview]] — Agent 工程全景
- [[concepts/harness-methodology]] — Harness 方法论概念页

---

*本问答基于 4 篇来源综合生成。*