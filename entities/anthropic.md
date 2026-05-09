# Anthropic

> 类型：模型厂商 | 核心产品：Claude系列 | 最后更新：2026-05-09

## 简介

Anthropic是AI安全和对齐研究的前沿公司，Claude系列模型以长上下文和可靠性著称。2026年，Anthropic在Harness Engineering方法论上处于行业领先地位。

## 最新动态

### 2026-04：Harness Engineering 领导者

**核心贡献**
- 2026年2月发布工程博客《Harness design for long-running application development》
- 提出三Agent Harness架构：Planner-Generator-Evaluator
- 发布三篇 Harness 相关论文
- 被Hugging Face的Philipp Schmid称为"2026年最重要的学科"

**三Agent Harness设计**
- **Planner**：负责规划
- **Generator**：负责生成
- **Evaluator**：负责评估（使用Playwright MCP导航实时页面）
- 迭代5-15轮，有时长达4小时
- 关键原则：AI只能通过验证来证明任务完成，不能自我声明

**Managed Agents**
- 将Agent拆解为Session / Harness / Sandbox三层
- Harness（大脑）与Sandbox（双手）完全解耦
- 性能提升：p50 TTFT下降60%，p95 TTFT下降90%以上

### 2026-04：Opus 4.7 发布
- 第三代模型（不到一年内）
- 每次升级不仅改进模型，还简化Harness
- 3月负载的组件到4月变成死重（需要定期清理workaround）

## 技术理念

**公式**：Agent = Model + Harness

- 传统SDD关注"代码如何运行"
- Harness Engineering关注"AI如何在环境中生存和决策"

## 相关概念
- [Harness方法论](../concepts/harness-methodology.md)
- [RLHF](../concepts/rlhf.md)

## 引用来源
- [Anthropic工程博客：Managed Agents](https://www.anthropic.com/engineering/managed-agents) (2026-04)
- [Anthropic研究：Building trustworthy AI agents](https://www.anthropic.com/research/trustworthy-agents) (2026-04)
- [Harness Engineering详解（中文）](https://www.cnblogs.com/qiniushanghai/p/19857911) (2026-04)
- [OpenAI Harness Engineering案例](https://openai.com/index/harness-engineering/) (2026-02)
- [LangChain Harness实验](https://blog.langchain.dev/) (2026)
- [Hugging Face Philipp Schmid评论](https://huggingface.co/) (2026)
