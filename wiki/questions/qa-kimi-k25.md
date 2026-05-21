# Q: 月之暗面 Kimi K2.5 的 Agent Swarm 有什么特别？

> 关联概念: [[Agent Skills]], [[Harness Methodology]], [[Test-Time Compute]]
> 关联实体: [[月之暗面]], [[Anthropic]], [[OpenAI]]
> 来源: [[sources/moonshot-kimi-k25]], [[sources/prm-adaptive-test-time-compute-2026]]

## 一句话回答

Kimi K2.5 的 Agent Swarm = 1 个协调 Agent + 100 个专项子 Agent，单轮可调用 1500+ 工具。这不是「多开几个窗口」，而是一个有指挥体系的 Agent 军队。

## 核心参数

| 指标 | Kimi K2.5 | 行业对比 |
|------|-----------|---------|
| 子 Agent 数量 | 100 | Anthropic: 3-Agent, OpenAI: 未公开 |
| 工具调用/轮 | 1500+ | GPT-4: ~128, Claude: 未公开 |
| 训练方法 | PARL (Process-Adaptive RL) | RLHF + DPO 为主流 |
| License | Modified MIT | 各家专有 |
| 本地部署 | 支持 | 各家受限 |

## Agent Swarm 架构

### 三层结构

```
Orchestrator (协调者)
├── Domain Agent 1 (领域Agent) — 如「代码Agent」
│   ├── Tool 1 → Tool 2 → Tool 3
│   └── 可调用子工具链
├── Domain Agent 2 (领域Agent) — 如「搜索Agent」
│   ├── Search API → 网页抓取 → 摘要生成
│   └── 可调用子工具链
└── ... (最多100个Domain Agent)
```

### 关键创新：PARL 训练

**PARL = Process-Adaptive Reinforcement Learning**

传统 RLHF：训练模型回答「对/好」
PARL：训练模型学会「什么时候该调用哪个Agent、调用多少轮」

- 奖励信号不仅来自「最终答案质量」，还来自「协作过程效率」
- 类似多智能体强化学习（MARL），但针对 LLM 特化

## 与竞品的差异

### vs Anthropic 三Agent

| 维度 | Anthropic | 月之暗面 |
|------|-----------|---------|
| 架构 | 3个固定角色 | 100个可配置角色 |
| 规模 | 精简、可控 | 大规模、灵活 |
| 适用场景 | 企业级确定性任务 | 复杂探索型任务 |
| 验证机制 | Verifier闭环 | PARL自适应 |

### vs OpenAI

OpenAI 未公开其内部 Agent 架构细节（100万行零手写是结果，不是架构）。

## 为什么重要？

1. **中国厂商首次在 Agent 架构上提出原创方法论**（PARL），而非跟随西方
2. **Modified MIT License** 让开源社区可以复现和扩展
3. **1500+ 工具调用** 证明了 LLM 的长上下文能力可以用于复杂编排

## 局限与风险

- **100个Agent的管理复杂度**：协调成本是否会超过收益？
- **PARL的可解释性**：奖励信号如何分解到每个Agent？
- **安全性**：100个Agent同时操作，出错面更大

## 延伸阅读

- [[entities/moonshot]] — 月之暗面实体档案
- [[syntheses/2026-ai-industry-trends]] — 行业趋势综述
- [[comparisons/closed-vs-open-models]] — 闭源vs开源对比

---

*本问答基于 2 篇来源综合生成。*