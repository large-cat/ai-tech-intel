---
title: "Harness Engineering vs SDD for AI Agents"
source: "gonetech.net"
url: "https://gonetech.net/harness-engineering-vs-sdd-for-ai-agents"
date: "2026-04-21"
entities: [Anthropic, OpenAI]
concepts: [Harness方法论]
---

## 关键发现

### PEV循环（Plan-Execute-Verify）
- 标准SDLC对Agent太慢，需要新循环
- Agent写计划 → 在Sandbox执行 → Verifier检查 → 失败则重试
- 无需人工干预的闭环

### Agent = Model + Harness
- 传统SDD（Software-Driven Development）把AI当API调用
- Harness Engineering构建确定性执行环境来约束概率性AI输出
- 模型不变，Harness变，结果剧变

### 核心数据
- LangChain实验：仅优化Harness（模型不变），Terminal Bench 2.0从52.8%→66.5%
- 排名从#30提升到#5

## 引用段落
> "在AI Agent时代，模型本身不再是瓶颈，围绕模型的外部系统设计才是决定性能的关键杠杆。"

## 关联页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md)
- [entities/anthropic.md](../entities/anthropic.md)
- [entities/openai.md](../entities/openai.md)
