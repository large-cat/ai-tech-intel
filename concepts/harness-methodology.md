# Harness Engineering / Harness方法论

> 类型：AI工程方法论 | 热度：🔥 2026年最核心范式 | 最后更新：2026-05-12

## 定义

Harness Engineering（Harness工程）是2026年出现的AI工程新范式，核心是构建一个确定性的"执行环境"来约束和验证概率性的AI输出。

**核心公式**：Agent = Model + Harness

- **模型（Model）**：大脑——推理能力
- **Harness（马具/线束）**：身体+神经系统+规则框架——让模型在真实环境中持续行动、调用工具、完成长任务

## 为什么需要Harness

传统软件开发（SDD）把AI当API调用，但Agent时代面临三大失败：
1. **幻觉逃避测试** —— 传统测试无法覆盖AI的创造性输出
2. **长窗口上下文退化** —— 长时间任务中上下文丢失
3. **会话状态漂移** —— 多轮交互中目标偏离

---

## 🧬 核心框架深度版

### PEV循环（Plan-Execute-Verify）

标准SDLC对Agent太慢。Harness强制Agent进入确定性循环：

```
┌─────────┐    ┌──────────┐    ┌───────────┐    ┌──────────┐
│  Plan   │──→│ Execute  │──→│  Verify   │──→│  Accept? │
│ (规划)   │    │ (执行)    │    │ (验证)     │    │          │
└─────────┘    └──────────┘    └───────────┘    └────┬─────┘
                                                       │ No
                                          ┌────────────┘
                                          ↓
                                    ┌─────────────┐
                                    │   Retry     │
                                    │ (重试/修正)  │
                                    └─────────────┘
```

数学化描述：
- 设任务目标为 $G$，当前计划为 $P_t$，执行结果为 $E_t$，验证分数为 $V(E_t) \in [0, 1]$
- 循环条件：$\max_t V(E_t) < V_{threshold}$
- 最大迭代次数：$T_{max}$（防止无限循环）
- 回溯策略：若 $V(E_t) < V(E_{t-1})$，回退到 $P_{t-1}$ 重新规划

### Verifier Model（验证器模型）

PEV循环的核心是**Verifier**——一个独立的LLM实例，专门负责检查主Agent的输出：

| 属性 | 说明 |
|------|------|
| **独立性** | 与主Agent使用不同系统提示/温度参数，避免"自我验证"偏差 |
| **能力要求** | 不需要比主Agent强，但需要"严格"——宁可误判 false negative，不可放过错误 |
| **验证维度** | 正确性（Correctness）、完整性（Completeness）、安全性（Security）、风格一致性（Style） |
| **输出格式** | 结构化JSON：`{"passed": false, "issues": [{"severity": "critical", "description": "..."}]}` |

**为什么Verifier不能和主Agent合并？**
- 认知心理学中的**确认偏误**（Confirmation Bias）：人倾向于支持自己已有的结论
- LLM同理：让它自己检查自己的输出，会系统性放宽标准
- **独立Verifier** = 给AI装上"外部审计员"

### 三Agent架构（Anthropic）

Anthropic在Harness实践中演化出的三角色分工：

| Agent | 角色 | 职责 | 模型要求 |
|-------|------|------|----------|
| **Planner** | 建筑师 | 任务拆解、依赖分析、制定执行顺序 | 强推理能力，高温度（创造性） |
| **Executor** | 工人 | 按Plan调用工具、写代码、运行命令 | 强工具调用能力，低温度（确定性） |
| **Verifier** | 质检员 | 检查Executor输出，判定是否达标 | 强批判能力，极低温度（严格） |

---

## 🏗️ MCP协议集成（确定性约束层）

Harness 通过 MCP 协议将"不确定性"封装在"确定性边界"内：

```
┌─────────────────────────────────────────────────┐
│                  Harness 框架                     │
├─────────────────────────────────────────────────┤
│  Planner (LLM) → 生成任务计划（文本/JSON）        │
├─────────────────────────────────────────────────┤
│  MCP Protocol Layer（确定性边界）                  │
│  ├── Tool Schema 校验（JSON Schema Draft 7）      │
│  ├── 超时控制（默认30s，可配置）                   │
│  ├── 幂等性检查（防重复执行）                      │
│  └── 审计日志（每次调用记录输入/输出/耗时）         │
├─────────────────────────────────────────────────┤
│  Executor (LLM) → 通过 MCP 调用确定性工具         │
├─────────────────────────────────────────────────┤
│  Verifier (LLM) → 验证输出是否符合预期             │
├─────────────────────────────────────────────────┤
│  Sandbox（隔离执行环境）                           │
│  └── Docker容器 / 受限文件系统 / 网络白名单         │
└─────────────────────────────────────────────────┘
```

### Harness 的 MCP Tool 设计原则

| 原则 | 实现方式 | 目的 |
|------|----------|------|
| **Schema 刚性** | `inputSchema` 使用 JSON Schema Draft 7，`additionalProperties: false` | 防止LLM传递多余/错误参数 |
| **超时熔断** | 每个Tool设置 `timeout_ms`，超时时返回 `{"error": "timeout"}` | 防止长时阻塞 |
| **副作用声明** | Tool元数据标记 `sideEffects: true/false` | Verifier可针对性检查 |
| **幂等键** | 支持 `idempotency_key` 参数 | 网络重试时不重复执行 |
| **审计追踪** | 每次调用生成 `trace_id`，关联到父任务 | 事后分析 + 调试 |

---

## 🏗️ Stripe Minions Blueprint（生产级实现）

> 来源：`sources/modern-harness-blueprint-2026.md`

Stripe在2026年3月公开的 **Minions** 系统，是Harness方法论的最完整生产级实现：

### 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│  Minion（确定性Agent）                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  计划阶段（Plan）                                     │   │
│  │  ├── 读取任务描述 + 上下文（MCP Resources）            │   │
│  │  ├── 调用 "plan_task" Tool 生成执行步骤              │   │
│  │  └── 输出：JSON格式的步骤清单（依赖图）               │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  执行阶段（Execute）                                 │   │
│  │  ├── 遍历步骤清单，每步调用对应 MCP Tool              │   │
│  │  ├── 并行执行无依赖步骤（200+ 服务并发）              │   │
│  │  └── 捕获所有Tool输出，写入审计日志                   │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  验证阶段（Verify）                                  │   │
│  │  ├── 调用 "verify_task" Tool 检查产出                │   │
│  │  ├── 维度：测试通过、安全扫描、性能基准、代码规范     │   │
│  │  └── 任一项不通过 → 触发 Retry                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  重试阶段（Retry）                                   │   │
│  │  ├── 分析失败原因（LLM错误分类）                      │   │
│  │  ├── 调整计划（增加前置步骤/修改参数）                │   │
│  │  └── 最大重试次数：5次（防止无限循环）                │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 关键性能指标

| 指标 | 数值 | 说明 |
|------|------|------|
| MCP Tool 总数 | **400+** | 覆盖测试、部署、监控、审计、安全扫描 |
| 并行服务数 | **200+** | 无依赖步骤并行执行 |
| 单次运行时长 | **90分钟** | 完全自主，无人值守 |
| 成功率 | **>95%** | 首次通过或重试后通过 |
| 人工介入率 | **<5%** | 仅极端异常需人工判断 |

### Minions 的 Harness 实现细节

1. **沙箱隔离**：每个Minion在独立Docker容器中运行，文件系统 `/workspace` 只读挂载 + 可写临时目录
2. **网络白名单**：容器网络仅允许访问预定义的CI/CD服务（GitHub API、内部Registry），外网默认拒绝
3. **资源限制**：CPU 4核 / 内存 8GB / 磁盘 20GB，防止Agent失控消耗资源
4. **密钥管理**：MCP Server以 sidecar 容器运行，持有API密钥，主Agent通过MCP间接调用（密钥不可见）
5. **审计日志**：每次MCP调用记录完整输入/输出/耗时/trace_id，存储90天，支持事后回放

---

## 🔑 关键变体

### 1. Plan-Do-Check-Act（PDCA循环）
质量管理经典循环的AI版本：
- **Plan**：AI生成详细执行计划
- **Do**：在沙箱中执行
- **Check**：Verifier检查 + 单元测试
- **Act**：根据检查结果调整，进入下一轮

### 2. ReAct（Reasoning + Acting）
Yao et al. 2022 提出的推理-行动交替框架：
- **Thought**：LLM内部推理（"我需要先查API文档"）
- **Action**：调用工具（`search_api_docs(query="auth")`）
- **Observation**：观察工具返回（"auth接口需要Bearer Token"）
- **循环**：Thought → Action → Observation → Thought...

与Harness的关系：ReAct是"微观循环"（单步决策），Harness是"宏观循环"（任务级验证）。

---

## 🚀 前沿进展

### LangChain Terminal Bench 2.0（2026-03）

LangChain发布的Agent基准测试，验证Harness质量：
- **Reasoning Sandwich**：在Agent执行链中插入"推理暂停点"，强制AI在关键决策前显式思考
- **LoopDetectionMiddleware**：检测Agent是否陷入循环（重复调用相同Tool/参数），自动触发人工接管
- **Trace Analyzer Skill**：MCP Skill，自动分析Agent执行轨迹，识别低效模式

### 与Agent Skills的关系

| 维度 | Harness方法论 | Agent Skills |
|------|--------------|-------------|
| 层级 | 抽象架构 | 具体实现 |
| 类比 | 建筑设计原则 | 施工规范 |
| 关系 | Harness定义"为什么需要约束" | Agent Skills定义"约束的具体内容" |
| 协作 | Harness框架加载Agent Skills作为MCP Tool | Agent Skills在Harness框架内执行 |

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| Minions工具数 | 400+ MCP Tools | Stripe Engineering Blog |
| Minions并行服务 | 200+ | Stripe Engineering Blog |
| Minion运行时长 | 90分钟（无人值守） | Stripe Engineering Blog |
| MCP超时默认值 | 30s | Anthropic MCP Spec |
| Verifier独立模型 | 推荐不同温度/提示 | Anthropic最佳实践 |
| PEV循环最大重试 | 5次（行业惯例） | Stripe/LangChain实践 |

---

## 🔗 相关页面
- [concepts/agent-skills.md](agent-skills.md) — 具体实现规范
- [entities/anthropic.md](../entities/anthropic.md) — 三Agent架构提出者
- [entities/stripe.md](../entities/stripe.md) — Minions Blueprint
- [entities/langchain.md](../entities/langchain.md) — Terminal Bench 2.0
- [concepts/mcp.md](mcp.md) — MCP协议技术规范

---

*最后更新：2026-05-12*  
*信息来源：Stripe Engineering Blog, Anthropic Harness论文, LangChain Terminal Bench 2.0, MCP Spec (arxiv.org/pdf/2604.05969)*