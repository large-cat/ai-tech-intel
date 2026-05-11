# Cognitive Memory > RAG

> 存储"为什么"而不仅是"是什么"。RAG存储事实，Cognitive Memory存储决策理由。

> 详见 [Harness 方法论](README.md) 中的 "关键组件" 部分。

## Cognitive Memory 详解

Harness Engineering 的关键组件之一，位于五层架构的**L2上下文层**和**L5生命周期层**之间。

### 与RAG的区别

| 特性 | RAG | Cognitive Memory |
|------|-----|------------------|
| 存储内容 | 事实信息 | 决策理由和上下文 |
| 查询方式 | 语义相似度匹配 | 决策模式匹配 |
| 使用场景 | 知识检索 | 决策复用和优化 |

### 核心价值

- **超越RAG**：不仅存储"是什么"，更存储"为什么"
- **决策复用**：Agent可以在后续任务中理解和复用之前的决策逻辑
- **经验积累**：随着任务执行，Agent的决策质量持续提升

## 实践示例

- **Contracts**：输入输出约束、验证门、权限边界
- **File-backed State**：外部化持久状态，路径可寻址
- **Failure Taxonomy**：命名失败模式驱动恢复

## 相关实体
- [Anthropic](../../entities/anthropic.md)
- [OpenAI](../../entities/openai.md)
- [月之暗面](../../entities/moonshot.md)
- [DeepSeek](../../entities/deepseek.md)
- [Meta](../../entities/meta.md)
