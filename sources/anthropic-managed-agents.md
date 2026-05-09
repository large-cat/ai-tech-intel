---
title: "Anthropic Engineering: Managed Agents"
source: "anthropic.com/engineering/managed-agents"
url: "https://www.anthropic.com/engineering/managed-agents"
date: "2026-04"
entities: [Anthropic]
concepts: [Harness方法论]
---

## 关键发现

### 三Agent架构
| Agent | 职责 |
|-------|------|
| Planner | 规划任务、分解步骤 |
| Generator | 执行生成（代码/设计/内容） |
| Evaluator | 评估输出质量，提供反馈 |

### Managed Agents产品化
- Agent拆解为Session（记忆）/ Harness（大脑）/ Sandbox（双手）三层
- Harness与Sandbox完全解耦
- 性能提升：**p50 TTFT↓60%，p95 TTFT↓90%+**
- 安全设计：凭证Token永不进入Sandbox可访问范围

### 迭代过程
- 迭代5-15轮，有时长达4小时
- 输出质量从"模板化"跃升到"生产级"
- 关键原则：AI只能通过验证来证明任务完成，不能自我声明

### Opus 4.7洞察
- 不到一年内第三代模型
- 每次升级不仅改进模型，还简化Harness
- 3月的workaround到4月变成死重 → 需要定期Lint清理

## 引用段落
> "2026年最重要的学科" — Hugging Face Philipp Schmid

## 关联页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md)
- [entities/anthropic.md](../entities/anthropic.md)
