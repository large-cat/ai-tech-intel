# Stripe Minions Blueprint 架构详解

> 来源：Mitchell Hashimoto博客（Stripe工程师，HashiCorp创始人），Stripe工程博客  
> 日期：2025-2026  
> 关联：[concepts/harness-methodology.md](../concepts/harness-methodology.md) | [entities/stripe.md](../entities/stripe.md)

---

## 背景

Stripe内部自研的AI Agent编排框架，源于对**Goose**（Block/Square开源coding agent）的深度fork。核心目标是解决"AI写代码不稳定"的问题——让Agent既能自主发挥创造力，又在关键步骤上完全可控。

Stripe称这套系统为**Minions**，核心编排单元叫**Blueprint**。

---

## 核心创新：Blueprints = 确定性节点 + 智能体节点

Stripe的关键洞察：不是所有步骤都需要AI的不确定性。有些步骤应该100%可预测。

| 节点类型 | 示例 | 执行方式 | 占比 |
|----------|------|----------|------|
| **确定性节点（Deterministic）** | git commit、lint、测试、创建分支、推送PR、代码格式化 | 硬编码步骤，100%可预测 | ~70% |
| **智能体节点（Agentic）** | "实现任务描述"、"修复CI失败"、"重构模块" | AI自主决策，输出不确定 | ~30% |

---

## 状态机设计

Blueprints的运行方式是**交替执行**：

```
创建分支（确定）→ 写代码（Agent）→ 运行测试（确定）→ 修复失败（Agent）→ 代码格式化（确定）→ 推送PR（确定）→ 请求审查（确定）
```

**关键规则**：
- Agent节点之前/之后必须有确定性节点作为"锚点"
- 如果Agent节点失败（测试未通过），自动重试或路由到修复分支
- 确定性节点失败（如lint错误）直接终止，不浪费Agent调用

---

## 关键子系统

### 1. 上下文工程（Context Engineering）

**不是全局System Prompt，而是条件化规则**：

```yaml
rules:
  - path: "infra/"
    apply: [terraform-lint, aws-policy-check]
  - path: "web/"
    apply: [react-best-practices, accessibility-check]
  - path: "api/"
    apply: [openapi-validate, rate-limit-check]
```

**效果**：
- 每个文件只加载相关的规则，不加载全部规则
- 节省Token（上下文窗口更高效利用）
- 减少误判（不会因为全局规则而错误地约束局部代码）

### 2. Devbox（隔离开发环境）

- **10秒启动**：预配置的Docker容器，包含所有依赖
- **与生产隔离**：Agent在此沙箱中运行，无法触及生产环境
- **状态持久化**：每个Blueprint实例有自己的文件系统状态
- **并行化基础**：因为隔离，同一Blueprint可在200+服务上同时运行

### 3. MCP工具网络（Toolshed）

- 内部"Toolshed"服务器连接**400+ MCP工具**
- Agent按需调用，不是一次性加载全部工具
- 工具分为：代码工具（lint、test、format）、基础设施工具（deploy、rollback）、通信工具（slack、email）

### 4. 多Agent协调

- **不同Agent专精不同领域**：前端Agent、后端Agent、安全审计Agent、文档Agent
- **中央编排器**：根据Blueprint步骤和当前上下文，分配给最适合的Agent
- **Agent间通信**：通过共享状态（File-backed State）传递上下文

### 5. 人类审查红线

**AI只有提交权，没有合并权**：
- Agent可以创建PR、推送代码、请求审查
- 但所有PR必须经过人类审查才能合并
- 审查者可以看到Agent的完整思考过程（Trace）
- 如果Agent频繁犯同类错误，审查者可以反馈到Blueprint规则中

---

## 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 每周合并PR数 | 1300+（AI编写） | Stripe内部统计 |
| Blueprint覆盖率 | 200+服务 | Stripe内部 |
| MCP工具数 | 400+ | Toolshed服务器 |
| 确定性节点占比 | ~70% | 架构设计 |
| 平均PR审查时间 | <2小时 | Stripe工程博客 |

---

## 与Anthropic/OpenAI Harness策略对比

| 维度 | Stripe | Anthropic | OpenAI |
|------|--------|-----------|--------|
| 核心策略 | 确定性×智能体混合 | 三Agent分离 | Raw Power |
| Harness层级 | Blueprint状态机 | Planner-Generator-Evaluator | 约束+反馈循环 |
| 人类角色 | 审查者（合并前必审） | 设计者（定期Lint） | 架构师（设计约束） |
| 并行化 | 200+服务同时 | Session级 | 项目级 |
| 工具数量 | 400+ MCP | Playwright MCP等 | 内部工具 |
| 关键洞察 | "70%步骤不需要AI" | "Harness随模型进化" | "环境比模型重要" |

---

## 引用来源
- Mitchell Hashimoto个人博客：mitchellh.com/writing（2026-02，关于AI采用历程）
- Stripe工程博客：stripe.com/blog（2025-2026，Minions系统介绍）
- Goose项目：block.github.io/goose（开源coding agent，Stripe fork的基础）
- 行业报道：mindstudio.ai/blog/what-is-ai-agent-harness-stripe-minions/（2026-03，Stripe Minions概述）
