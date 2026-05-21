# Blueprint for a Modern Agentic Harness in 2026 (Gist Summary)

> **来源**: [GitHub Gist - amazingvince](https://gist.github.com/amazingvince/52158d00fb8b3ba1b8476bc62bb562e3)
> **收集时间**: 2026-05-12
> **类型**: 架构蓝图 / 开源方案设计

---

## 核心理念

If you only remember six things:

1. **Harness matters more than the loop** — model-tool loop 已是商品，差异化来自上下文工程、持久状态、策略执行、外部化记忆和协议设计
2. **Design around cache stability first** — prompt caching 改变整个架构设计
3. **Treat filesystem as working memory** — 大工具输出、笔记、计划、恢复状态应存于外部，通过 handle 引用
4. **Keep built-in action space small and stable** — 核心原语：文件操作、搜索/读取、代码执行、规划/任务、子Agent委派、结构化用户询问
5. **Use subagents for context isolation** — 不是因为"多Agent"听起来高级，而是因为需要并行探索、专用提示/工具、独立上下文窗口
6. **Put guardrails in the runtime, not the prompt** — 破坏性工具、密钥访问、网络出口、外部写入需要确定性策略检查

---

## 五层稳定架构

```
1. Execution runtime     — 事件循环、会话管理、检查点、恢复
2. Context system        — 提示布局、产物引用、压缩、缓存纪律
3. Capability surface    — 内置工具、外部工具、技能、子Agent
4. Governance layer      — 审批、钩子、允许/拒绝策略、沙箱、溯源
5. Surface/protocol adapters — CLI、IDE、Web UI、ACP、MCP、A2A
```

---

## 关键决策表

| 领域 | 推荐默认 | 理由 |
|---|---|---|
| 核心运行时 | 持久状态机 / 图运行时 + 检查点 | 长时任务需要暂停/恢复、重放、容错、人工中断 |
| 会话历史 | 追加式事件日志 + 类型化状态快照 | 缓存稳定、可重放、可审计、确定性恢复 |
| 工作记忆 | 产物优先的文件系统 + 元数据存储 | 卸载上下文、保留可恢复性、支持交接 |
| 内置工具 | 窄域、命名空间化的原语 | 小且稳定的动作空间改善选择质量 |
| 大数据处理 | 程序化工具调用或沙箱代码执行 | 中间数据不进入模型上下文 |
| 规划 | 任务图或结构化 todo 原语 | 作为注意力控制和协调状态 |
| 多Agent | 默认编排器-工作者模式 | 上下文隔离和并行工作的最强回报 |
| 协议 | MCP(工具)、ACP(IDE/客户端)、A2A(远程Agent) | 关注点分离和未来互操作性 |
| 人机协作 | 结构化询问工具 + 审批策略 | 比纯文本来回更快更确定 |
| 安全 | 沙箱 + 策略引擎 + 审计日志 | 实际工具使用的信任边界 |

---

## 上下文工程四级策略

| 层级 | 策略 | 触发条件 |
|---|---|---|
| **Tier 0** | 结构化输出默认 | 工具结果已简洁、类型化、产物支撑 |
| **Tier 1** | 即时大结果驱逐 | 工具返回大对象 → 写入产物，仅返回摘要+handle |
| **Tier 2** | 延迟输入/结果驱逐 | 上下文达 80-90% 安全窗口时，将旧输入/结果改写为引用 |
| **Tier 3** | 压缩/摘要 | 总结旧历史为：当前目标、已达状态、开放任务、关键决策、产物引用、下一步建议 |
| **Tier 4** | 全新窗口重启 | 外部化状态良好时，新窗口优于压缩 |

**缓存友好排序**：静态系统提示 > 项目记忆/AGENTS.md > 会话级状态摘要 > 近期消息 > 最新用户输入

---

## 子Agent 模式

| 模式 | 使用时机 | 权衡 |
|---|---|---|
| 单Agent | 多数任务起步 | 最简单、最易调试 |
| Skills | 单Agent 需要大量潜在能力 | 加载上下文随时间累积 |
| Subagents | 需要上下文隔离、专业化或并行工作 | 额外编排调用 |
| Handoffs | 需要顺序阶段式对话 | 更状态化、更难推理 |
| Router | 需要无状态扇出和跨域综合 | 重复路由开销 |

**默认模式：编排器-工作者**
- 主Agent 持有用户契约和任务级状态
- 工作者Agent 获得窄任务简报和隔离上下文
- 工作者仅返回最终输出 + 产物引用
- 工作者不共享对话历史

---

## Skills 与渐进式披露

Skills 不只是"提示片段"，而是一种**有纪律的方式**在不膨胀常驻系统提示或工具目录的前提下增加潜在专业能力。

**推荐格式**：
```
skills/
  release-engineering/
    SKILL.md
    templates/
    scripts/
    references/
```

- YAML frontmatter：`name`、`description`、可选 allowed tools
- 任务框架、决策规则、所需产物/模板、示例、脚本链接

**Skill vs Tool 决策**：
- **Skill**：领域知识、工作流指导、运营策略、模板
- **Tool**：需要执行的能力、有状态操作、副作用、特殊审批边界

---

## 协议层：MCP / ACP / A2A

| 协议 | 关系 | 作用 |
|---|---|---|
| **MCP** | Agent → 工具/资源 | 连接 Agent 到外部工具和数据源 |
| **ACP** | 客户端/IDE → 本地或远程 Agent 运行时 | 标准化编码 Agent 和客户端应用间的通信 |
| **A2A** | Agent → 远程 Agent | 远程 Agent 间委派和任务交换 |

**重要洞察**：A2A 明确将 **messages** 和 **artifacts** 分离，结果应作为 task artifacts 而非聊天消息返回 — 与产物优先设计高度兼容。

---

## 安全架构

**核心原则**：假设模型有能力但不足够可信作为唯一控制平面

| 控制层 | 内容 |
|---|---|
| 文件系统 | 绝对根目录强制、路径规范化、符号链接防御、受限写入范围 |
| 沙箱 | 隔离容器、默认关闭网络出口、包安装限制、资源配额、进程超时 |
| 密钥 | 不暴露 .env 或原始密钥存储、按需注入、记录访问、密钥脱敏 |
| 工具输出注入防御 | 将获取的网页/MCP输出视为不可信、剥离指令注入、要求人工审批敏感操作 |
| 审计和溯源 | 每个外部动作记录：请求者、输入、审批路径、输出/产物引用、时间戳、哈希 |

---

## 产出评估 (Evals) 缺口

LangChain State of Agent Engineering 报告：
- **89%** 已实施可观测性
- **仅 52%** 实施了评估 (Evals)
- → **评估体系规模化**是 Harness Engineering 接下来一年的核心课题
