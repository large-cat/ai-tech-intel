# Harness Engineering: 从 Prompt → Context → Harness 的认知升级

> **来源**: [虎嗅](https://www.huxiu.com/article/4841931.html)
> **日期**: 2026-03-13
> **收集时间**: 2026-05-12

## 一句话总结

Prompt Engineering 管"说什么"，Context Engineering 管"知道什么"，Harness Engineering 管"在什么环境里做事"。

---

## 时间线

| 时间 | 事件 | 意义 |
|---|---|---|
| 2026-02-05 | Mitchell Hashimoto (HashiCorp 联合创始人) 发文命名 Harness Engineering | 概念诞生 |
| 2026-02-11 | OpenAI 发布内部实验报告 | 业界首个大规模实战记录 |
| 2026-02-17 | Martin Fowler Twitter 站台 | 获得架构界认可 |

---

## 关键实验数据

| 实验 | 变量 | 结果 |
|---|---|---|
| LangChain Terminal Bench 2.0 | 仅优化 Harness（文档结构、验证回路、追踪系统） | 得分 52.8% → 66.5%，排名 第30 → 第5 |
| Can Boluk 安全研究 | 仅改变 Agent 代码编辑格式 | Grok Code Fast 1: 6.7% → 68.3% |
| OpenAI 内部实验 | 5名工程师，5个月，0行手写代码 | 交付 100 万行生产级代码 |

---

## OpenAI 实验细节

### 效率数据
- 平均每位工程师每日 3.5 个 PR 合并吞吐量
- 代码审查通过 Agent-to-Agent 循环自动化
- 人工监督仅保留在高层架构决策

### AGENTS.md 进化

**早期错误**：所有信息塞进一份庞大 AGENTS.md
→ Agent 被信息淹没，性能反而下降

**最终方案**：渐进式披露模型
```
AGENTS.md              ← 精简目录 (~100行)
docs/AGENTS.override.md ← 子目录级覆盖规则
docs/ARCHITECTURE.md    ← 分层架构与依赖流向
docs/DESIGN.md          ← 设计原则与模式
docs/PLANS.md           ← 执行计划
docs/PRODUCT_SENSE.md   ← 产品意图与用户旅程
docs/QUALITY_SCORE.md   ← 质量评分标准
docs/RELIABILITY.md     ← 可靠性要求
docs/SECURITY.md        ← 安全约束
```

### 运行时观测
- 日志/指标/追踪 通过 LogQL 和 PromQL 向 Agent 开放
- Agent 可通过 Chrome DevTools Protocol 操作浏览器
- 重现 Bug、验证修复、对 UI 行为推理

### 架构围栏
- 严格分层依赖流向：Types → Config → Repo → Service → Runtime → UI
- 双重拦截：确定性 Linter + 基于 LLM 的审计 Agent
- Linter 错误输出重写：受众从人类变为 AI

---

## Böckeler 三级框架 (Thoughtworks)

> Birgitta Böckeler, Thoughtworks Distinguished Engineer
> 发表于 martin fowler.com

| 维度 | 核心 | 要点 |
|---|---|---|
| **上下文工程** | 确保 Agent 在正确时机获得正确信息 | 渐进式文档披露、动态可观测数据、浏览器行为推理 |
| **架构约束** | 机械化手段强制执行架构边界 | 确定性 Linter（输出格式专为 Agent 设计）+ LLM 审计 Agent |
| **熵管理/垃圾回收** | 约束系统本身不能随时间退化 | 专用清理 Agent 定期扫描文档漂移、模式违规 |

**关键补充**：OpenAI 报告主要关注内部质量，但对**功能性和行为验证覆盖不足**

---

## 行业独立验证

### Stripe Minions
- 每周合并 1,300+ 完全由 AI 编写的 PR
- 每个 Agent 任务在独立预热 devbox 中运行
- 中心化 MCP 服务器 **Toolshed**：近 500 个工具
- "蓝图"模式：确定性节点 + Agent 节点混合

### LangChain 对照实验
- 仅优化 Harness，模型不变
- 得分 52.8% → 66.5%，排名 第30 → 第5
- **最干净的变量控制证据**

### MCP 标准化
- 已纳入 Linux 基金会 Agentic AI 基金会治理
- 月 SDK 下载量 9,700 万+
- OpenAI、Google、Microsoft、AWS 均已采用
- Stripe Toolshed 就是一个 MCP 服务器

### 行业全景数据 (LangChain State of Agent Engineering)
- **89%** 团队已实施可观测性
- **仅 52%** 实施了评估 (Evals)
- → 评估体系规模化是 Harness Engineering 下一年的核心课题

---

## 工程师工作模式转变

### OpenAI 实验中的日常三件事
1. 构建文档与上下文体系（AGENTS.md、Linter、可观测性）
2. 以机器可处理的方式定义业务意图
3. 构建自动化的防呆验证机制

### Peter Steinberger (OpenClaw 创始人)
> "脑中保存项目高层结构的软件架构师" — 使用 Agent 时只讨论架构和重大决策，完全不涉及具体代码实现

### "学徒缺口" (Apprentice Gap)
> Böckeler 提出的问题：如果初级开发者过早进入 Agent 驱动循环，可能缺乏未来构建健壮 Harness 所需的深度系统直觉

---

## Hashimoto 六阶段采用旅程

| 阶段 | 状态 |
|---|---|
| 1 | 起步：把同一个任务做两遍（手动 + Agent） |
| 2 | 养成习惯：每天下班前 30 分钟启动 Agent |
| 3 | 关键跃迁：在项目中建一份 AGENTS.md |
| 4 | 建立评估体系 |
| 5 | **Hashimoto 目前所处阶段** |
| 6 | 完全自主 Agent 工作流 |

---

## 关键引用

> "我们目前最困难的挑战，集中在设计环境、反馈回路和控制系统上。"  
> — Ryan Lopopolo, OpenAI 报告

> "每当你发现 Agent 犯了一个错误，你就花时间设计一个解决方案，使 Agent 永远不再犯同样的错误。"  
> — Mitchell Hashimoto

> "Harness Engineering 是对 AI 使能软件开发关键部分的有价值框架。Harness 包括上下文工程、架构约束和垃圾回收。"  
> — Martin Fowler
