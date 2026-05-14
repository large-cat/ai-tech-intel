# 12-Factor Agents 工程原则深度解析

> 来源：HumanLayer / paddo.dev（2026-04）  
> 核心洞察：最成功的 AI 产品不是纯 agentic 循环，而是确定性代码 + 策略性放置的 LLM 决策点

---

## 一、12 条原则总览

受 Heroku 12-factor apps 启发，HumanLayer 提出 AI Agent 的工程化原则。

### Control（控制流）
| # | 原则 | 含义 |
|---|------|------|
| 1 | **Own your prompts** | 直接控制 prompt 工程，不用框架抽象 |
| 2 | **Own your control flow** | 显式执行路径，不委托给框架循环 |
| 3 | **Stateless reducer** | Agent 是纯函数：input state → output state |

### Context（上下文）
| # | 原则 | 含义 |
|---|------|------|
| 4 | **Own your context window** | 精心筛选进入 LLM 注意力的内容 |
| 5 | **Compact errors** | 将失败蒸馏为简洁上下文，而非冗长日志 |
| 6 | **Pre-fetch context** | 执行前预先获取信息，非中途查询 |

### State（状态）
| # | 原则 | 含义 |
|---|------|------|
| 7 | **Unify execution and business state** | 执行状态与业务状态合一，无并行系统 |
| 8 | **Launch/pause/resume** | 为人类介入设置挂起点 |

### Interface（接口）
| # | 原则 | 含义 |
|---|------|------|
| 9 | **Natural language to tool calls** | LLM 输出决策，不输出最终执行 |
| 10 | **Tools are structured outputs** | Tool-calling = 结构化输出生成 |
| 11 | **Trigger from anywhere** | Webhooks、cron、用户动作、外部事件均可触发 |

### Architecture（架构）
| # | 原则 | 含义 |
|---|------|------|
| 12 | **Small, focused agents** | 窄职责胜过单体系统 |
| 13 | **Contact humans with tool calls** | Human-in-the-loop 作为一等操作 |

*注：Factor 13（pre-fetch context）在附录中，但权重同等。*

---

## 二、关键概念：「Dumb Zone」（ dumb 区）

**Factor 3（own your context window）是枢纽**，其他原则依赖它。

Dex Horthy（HumanLayer founder）分析 **100,000 开发者 session** 后发现：
- 大上下文窗口的 **中间 40-60%** 区域，模型 recall 和 reasoning 显著退化
- 填充超过 40% 后，边际收益递减，信号/噪声比恶化
- > **"The more you use the context window, the worse the outcomes."**

这与 "lost in the middle" 研究一致：LLM 对上下文开头和结尾的信息表现最好，长序列中间的信息显著退化。

> "As agents become more capable, they naturally accumulate more tools. Your heavily armed agent gets dumber."  > — Manus AI, Context Engineering for Agents

Manus 为此重建了 4 次 agent 框架。Anthropic 的 context engineering 指导将其框定为：
> "找到最小的高信号 token 集合，以最大化期望结果的概率。"

**实践检查**：在 Claude Code 中输入 `/context`，你会看到 MCP 定义、膨胀的 CLAUDE.md、对话历史在真正工作前就消耗了大量 token。清理上下文 = 锐利 agent。

---

## 三、原则在现有工具中的映射

### Anthropic Plan Mode = Factors 2, 3, 8
- 系统级阻断 write tools
- 你拥有 prompt（factor 2）
- 上下文聚焦于 planning 而非执行产物（factor 3）
- 你控制何时开始执行（factor 8）
- 无框架抽象隐藏决策点

### Parallel subagents = Factor 10
- Plan Mode 派出轻量 Haiku agent 同时探索代码库
- 每个获得隔离上下文窗口，返回浓缩发现后销毁
- 小、聚焦、可丢弃 —— Factor 10 的实体化

### CLAUDE.md = Factor 3
- 项目和用户级指令文件是 curated context
- 短、具体、有观点
- 不是给你看的文档 —— 是给 Claude 的训练
- CLAUDE.md 里的每个 token 都是无法用于理解你实际代码的 token

### Agent harnesses = Factors 5, 6
- 进度文件（`claude-progress.txt`）和特性列表统一执行状态与业务状态
- Agent 在碰代码前先读进度文件
- Launch/pause/resume 通过 git commit 和人类审查实现，非魔法框架 hook

---

## 四、单体 vs 小 Agent 的哲学

**Factor 10 — small, focused agents** 是框架膨胀的解药。

社区曾搭建大量脚手架：
- BMAD：19 个专业 agent
- Spec-Kit：多阶段工作流
- 外部编排层

这些存在是因为工具缺乏原生结构。现在原生功能吸收了这些模式：
- Plan Mode 替代了手动的 plan/act 拆分
- Parallel subagents 替代了外部编排
- 脚手架成为 friction

12-factor 哲学对齐：**不要建单体 agent 系统。建小 agent，清晰接口，让它们组合。** 复杂度活在组合中，不在个体 agent 里。

---

## 五、原则不解决什么

Factor 7（human-in-the-loop） enable 了人机协作，但不替代人类判断。

**仍需人类拥有的**：
- **战略愿景** — 解决什么问题、进入什么市场
- **新颖架构** — 需要深度系统直觉的跨领域决策
- **模糊需求** — spec 不清时，agent 无法自行 resolve
- **最终责任** — 工程师拥有 ship 出去的东西

**SDLC collapse 模式**：委托机械工作，审查正确性，拥有判断 call。原则优化的是委托，不自动化所有权。

**90/90 规则仍然适用**：
- 前 90% 的代码花 90% 的时间
- 后 10% 的代码花另外 90% 的时间
- Agent 加速的是第一遍 pass，edge cases、集成问题、迭代优化的长尾依然长

---

## 六、落地建议

| 建议 | 对应原则 |
|------|---------|
| 将上下文视为稀缺资源 | 3, 4 |
| 拥有控制流 | 2 |
| 建小 agent | 10, 12 |
| 设计暂停点 | 6, 8 |
| 积极预取上下文 | 6, 13 |
| 远离 dumb zone | 3, 4 |

**具体操作**：
- 保持上下文 <40% 容量
- `/clear` _between_ tasks
- 让 auto-compact 处理溢出
- 每个 MCP、每个工具定义、每行 CLAUDE.md 都在消耗注意力预算 —— 保持精简

---

## 七、与 Karpathy 4 条 / 12 条原则的对比定位

| 维度 | Karpathy CLAUDE.md | 12-Factor Agents |
|------|-------------------|------------------|
| **目标** | 单 agent 行为约束 | 多 agent 系统工程 |
| **粒度** | 单次 LLM 调用质量 | Agent 架构与生命周期 |
| **控制流** | 隐含（Goal-Driven） | 显式（Own your control flow） |
| **上下文** | 项目特定（CLAUDE.md） | 系统级策展（context window 预算） |
| **状态** | 单次会话 | Launch/pause/resume，统一业务状态 |
| **人机协作** | 测试/checkpoint（Rule 9, 10） | Human-in-the-loop 作为一等操作 |
| **规模** | 单 codebase | 跨系统、多触发源 |

两者互补：CLAUDE.md 解决 "单个 agent 如何写代码"，12-Factor 解决 "agent 系统如何在生产中运行"。

---

## 参考链接

- 原文：https://paddo.dev/blog/12-factor-agents/
- HumanLayer：https://www.humanlayer.dev/
- 关联 wiki：concepts/agent-skills.md | concepts/harness.md | sources/karpathy-claude-md-12-rules.md
