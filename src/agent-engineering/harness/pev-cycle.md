# PEV 循环（Plan-Execute-Verify）

> Harness的核心执行循环。标准SDLC对Agent太慢 → 写计划→执行→验证→重试。

> 详见 [Harness 方法论](../README.md) 中的 "核心框架" 部分。

## PEV循环详解

Harness Engineering 的核心执行循环，替代传统的标准软件开发生命周期（SDLC）：

- **标准SDLC对Agent太慢** —— 传统瀑布或敏捷流程无法适应AI Agent的迭代速度
- **Harness强制Agent：写计划 → 在Sandbox执行 → Verifier模型检查 → 失败则重试**
- **无需人工干预** —— 整个循环自动化运行，减少人工审核瓶颈

## 与验证相关的设计

LangChain Terminal Bench 2.0 实验中的自验证循环设计（与PEV循环中的Verify阶段对应）：

| 优化维度 | 具体措施 | 效果 |
|----------|----------|------|
| **System Prompts** | 结构化规划指令、Reasoning Sandwich（xhigh规划→high实现→xhigh验证） | 基线提升 |
| **自验证循环** | 时间预算警告、测试要求提示、输出验证 | 减少幻觉 |

## 关键设计原则

- **Plan（计划）**：Agent首先生成详细的执行计划，包括步骤、依赖和预期输出
- **Execute（执行）**：在隔离的Sandbox环境中执行计划，避免影响生产系统
- **Verify（验证）**：Verifier模型检查执行结果的正确性、完整性和安全性
- **Retry（重试）**：验证失败时，自动修正计划并重新执行

## 相关实体
- [Anthropic](../../entities/anthropic.md)
- [OpenAI](../../entities/openai.md)
- [月之暗面](../../entities/moonshot.md)
- [DeepSeek](../../entities/deepseek.md)
- [Meta](../../entities/meta.md)
