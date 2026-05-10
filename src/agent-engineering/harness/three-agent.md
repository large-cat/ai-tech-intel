# 三Agent架构（Anthropic）

> Planner + Generator + Evaluator 分离，解决长任务"上下文失忆"问题。

> 详见 [Harness 方法论](../README.md) 中的 "核心框架" 部分。

## 架构设计

Anthropic 提出的三Agent分离架构，每个Agent专注单一职责：

| Agent | 职责 |
|-------|------|
| **Planner** | 规划任务、分解步骤 |
| **Generator** | 执行生成（代码/设计/内容） |
| **Evaluator** | 评估输出质量，提供反馈 |

## 工作方式

1. **Planner** 接收高层目标，分解为可执行的子任务序列
2. **Generator** 根据Planner的输出，生成具体的代码、设计或内容
3. **Evaluator** 检查Generator的输出质量，验证是否符合要求
4. 如果Evaluator反馈不合格，Planner重新调整计划，Generator重新生成

## 行业实践数据

Anthropic 的三Agent Harness 实践效果：

| 指标 | 改进 |
|------|------|
| p50 TTFT | ↓60% |
| p95 TTFT | ↓90%+ |

> TTFT（Time To First Token）：从发送请求到收到第一个Token的时间

## 相关实体
- [Anthropic](../../entities/anthropic.md)
- [OpenAI](../../entities/openai.md)
- [月之暗面](../../entities/moonshot.md)
- [DeepSeek](../../entities/deepseek.md)
- [Meta](../../entities/meta.md)
