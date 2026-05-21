# Q: 什么是 Harness 方法论？

> 关联概念: [[Harness Methodology]], [[Agent Engineering]]
> 关联实体: [[Anthropic]], [[OpenAI]], [[Stripe]], [[LangChain]]
> 来源: [[sources/modern-harness-blueprint-2026]], [[sources/anthropic-three-agent-harness]], [[sources/stripe-minions-blueprint]]

## 一句话回答

**Harness 方法论** = 把「单个AI能做什么」升级为「多个AI怎么协作完成复杂任务」的工程化框架。2026年，它正在复刻2010年代 DevOps 对软件工程的变革。

## 详细解释

### 从单Agent到多Agent

| 阶段 | 模式 | 类比 |
|------|------|------|
| 2024-2025 | 单Agent完成单一任务 | 一个程序员写完整模块 |
| 2026 (现在) | 多Agent协作（Harness） | DevOps团队：规划→执行→验证 |
| 2027+ | 自组织Agent Swarm | 全栈团队自治 |

### 核心架构模式

**Anthropic 三Agent架构**：
- **Planner（规划者）**：拆解任务，制定策略
- **Executor（执行者）**：调用工具，写代码，查资料
- **Verifier（验证者）**：检查结果，发现错误，要求重做

**Stripe Minions Blueprint**：
- **确定性工作流**（Deterministic）+ **智能体决策**（Agentic）的混合
- 400+ MCP工具，200+服务并行
- 当任务明确时走工作流，模糊时交智能体判断

**LangChain Terminal Bench 2.0**：
- 证明「模型不变，Harness变」也能大幅提升性能
- Reasoning Sandwich架构 + LoopDetectionMiddleware

### 为什么现在爆发？

1. **模型能力达标**：GPT-4级别模型已能可靠执行多步推理
2. **协议标准化**：MCP协议让Agent之间能"对话"
3. **工程需求**：企业级部署不能靠"提示工程运气"

### 与 DevOps 的类比

| DevOps | Harness Engineering |
|--------|---------------------|
| CI/CD流水线 | Agent编排流水线 |
| 基础设施即代码 | Harness即代码 |
| 监控告警 | Verifier自动纠错 |
| 蓝绿部署 | 多Agent A/B验证 |

## 常见误解

**❌ "Harness = 多开几个ChatGPT窗口"**

✅ Harness是**有结构的协作**：谁规划、谁执行、谁验证、何时切换，都有明确定义。

## 延伸阅读

- [[concepts/harness-methodology]] — 概念深度页
- [[syntheses/agent-engineering-overview]] — Agent工程全景
- [[sources/modern-harness-blueprint-2026]] — Modern Harness Blueprint源文件

---

*本问答基于 3 篇来源综合生成。如有遗漏，可通过提问触发补充。*
