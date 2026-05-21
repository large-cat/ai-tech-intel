# Agent 工程全景综述

> 综合类型：技术领域综述
> 覆盖层级：前置知识 → 根概念 → 子概念 → 实践案例 → 工具协议
> 更新策略：新实践案例触发补充

## 知识地图

```
Agent Engineering
├── 前置知识
│   ├── [[RLHF]] — 让模型对齐人类偏好
│   └── [[Test-Time Compute]] — 推理时多想一会
├── 根概念
│   └── [[Harness Methodology]] — 2026核心范式
├── 子概念
│   ├── [[PEV Cycle]] — Plan-Execute-Verify
│   ├── [[Three-Agent Architecture]] — Anthropic三Agent
│   ├── [[Five-Layer Architecture]] — 行业共识分层
│   ├── [[Context Engineering]] — 上下文工程
│   └── [[Cognitive Memory]] — 超越RAG的记忆系统
├── 实践案例
│   ├── Anthropic — 三Agent + Managed Agents
│   ├── OpenAI — 100万行零手写
│   ├── Stripe — Minions Blueprint
│   ├── LangChain — Terminal Bench 2.0
│   └── 月之暗面 — Agent Swarm 100子Agent
└── 工具协议
    ├── [[MCP]] — 模型控制协议
    ├── [[LangGraph]] — 状态管理图
    ├── [[E2B]] — 安全Agent沙箱
    └── [[ADK]] — Google Agent套件
```

## 关键演进路线

### 2024-2025：Agent 1.0
- 单Agent完成单一任务
- 提示工程主导
- RAG作为外部记忆

### 2026：Agent 2.0（当前）
- 多Agent协作（Harness）
- 确定性×智能体混合架构
- Cognitive Memory > RAG
- MCP协议标准化

### 2027+：Agent 3.0（预测）
- 自组织Agent Swarm
- 训练时即考虑Harness结构
- Agent间经济/激励机制

## 核心争议

**确定性 vs 智能体**：Stripe Minions Blueprint提出"确定性工作流 + 智能体决策"的混合模式，但业界对"分界线在哪里"仍有分歧。

---

*本综述基于 [[sources/12-factor-agents-humanlayer]]、[[sources/stripe-minions-blueprint]]、[[sources/modern-harness-blueprint-2026]] 等来源综合。*
