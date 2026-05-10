# Context Engineering

> 不是写好一条Prompt，而是设计动态系统来组装上下文。

> 详见 [Harness 方法论](../README.md) 中的 "关键洞察" 部分。

## Context Engineering 详解

Context Engineering 是Harness五层架构中**L2上下文层**的核心实践。

Stripe Minions Blueprint 中的上下文工程实践：

- **规则按子目录条件应用，不是全局System Prompt**
- 例如"只在infra/目录启用lint规则"，节省Token并减少误判

## 关键挑战：Context Anxiety

> **Context Anxiety**：模型接近上下文上限时倾向于提前结束任务，Harness需处理。

这是Harness设计中的关键挑战之一。当Agent的上下文窗口接近上限时，模型可能"焦虑地"提前结束任务，而不是继续完成剩余工作。Harness需要通过以下方式处理：

- **上下文压缩**：智能压缩历史对话，保留关键决策信息
- **分段处理**：将长任务分解为多个短任务，每个任务独立处理
- **状态外化**：使用File-backed State将关键状态持久化到文件，减少上下文占用

## 与Cognitive Memory的关系

Context Engineering 与 Cognitive Memory 配合使用：
- **Context Engineering** 解决"当前看到什么"的问题
- **Cognitive Memory** 解决"为什么做出这个决策"的问题

## 相关实体
- [Anthropic](../../entities/anthropic.md)
- [OpenAI](../../entities/openai.md)
- [月之暗面](../../entities/moonshot.md)
- [DeepSeek](../../entities/deepseek.md)
- [Meta](../../entities/meta.md)
