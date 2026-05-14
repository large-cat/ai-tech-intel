# Karpathy CLAUDE.md 12条规则升级版

> 来源：Antigravity.codes 深度拆解，基于 @mnilax (Mnimiy) 2026-05-09 的 X 长文（270万浏览，18,800 bookmark）  
> 原始4条规则由 Forrest Chang 在 2026-01 基于 Karpathy 的吐槽线程封装，GitHub 首日 5,828 stars，两周 60,000 bookmarks，年中突破 120,000 stars，成为 2026 年增长最快的单文件仓库。

---

## 1. 原始4条规则（Karpathy via Forrest Chang）

| # | 规则 | 核心意图 |
|---|------|---------|
| 1 | **Think Before Coding** | 禁止静默假设；显式陈述假设、权衡；简单方案存在时 push back |
| 2 | **Simplicity First** | 最小代码解决问题；禁止 speculative features；单用途代码不抽象 |
| 3 | **Surgical Changes** | 只碰被要求的部分；不改相邻代码、注释、格式；匹配现有风格 |
| 4 | **Goal-Driven Execution** | 定义成功标准并循环验证；不给步骤指令，给成功画像 |

**效果基线**（Mnimiy 30 codebases × 50 tasks × 6 weeks）：
- 无 CLAUDE.md：**错误率 ~41%**
- 4条规则：**错误率 ~11%，合规率 78%**

---

## 2. 新增8条规则（Mnimiy，2026-05）

每条规则都来自具体的事故：

| # | 规则 | 防止的失败模式 | 典型事故 |
|---|------|--------------|---------|
| 5 | **不让模型做非语言工作** | 确定性决策（重试策略、路由、阈值）交给确定性代码 | "决定是否对 503 重试" 的 LLM 调用两周后因模型读取请求体作为上下文而开始随机化 |
| 6 | **硬 token 预算，无例外** | 循环 spiraling 成 50k token dump | 90 分钟 debug 迭代同一段 8KB 错误信息，最终建议用户 40 条消息前已拒绝的修复 |
| 7 | **暴露冲突，不要平均化** | 代码库两处模式矛盾时，Claude 试图同时取悦双方 | async/await + global error boundary 并用，错误被吞两次 |
| 8 | **写前先读** | 不了解相邻代码就新增，导致冲突 | Claude 在已有函数旁新增同名函数，新函数因 import 顺序胜出，原函数是 6 个月的 source of truth |
| 9 | **测试不是可选的，但也不是目标** | 测试通过但测试本身无用 | 12 个 auth 测试全过，生产环境 auth 挂了——测试只检查 "返回了 something" |
| 10 | **长操作需要 checkpoint** | 多步工作流在第 4 步出错后继续 5、6 步 | 6 步重构第 4 步出错，后续在 broken state 上继续，回滚比重做更耗时 |
| 11 | **约定胜于新奇** | 在已有模式的代码库引入自己的 "更好" 方案 | React hooks 引入 class component 代码库，hooks 能用但测试假设 `componentDidMount` 全部失效 |
| 12 | **失败要可见，不要静默** | 看起来成功但实际上跳过/错误 | DB migration "成功完成"，静默跳过 14% 约束冲突记录，11 天后报表异常才发现 |

---

## 3. 关键数字：12条 vs 4条

| 配置 | 错误率 | 合规率 |
|------|--------|--------|
| 无规则 | ~41% | — |
| 4条 | ~11% | 78% |
| **12条** | **~3%** | **76%** |

**核心洞察**：从 4 条到 12 条，合规率几乎不变（78% → 76%），但错误率再降 8 个百分点。说明新增规则覆盖的是原 4 条**根本没碰到的**失败模式，而非争夺同一注意力预算。

---

## 4. 完整12条模板（可直接复制）

```markdown
# Coding Behavior Contract (12 Rules)

## Core (Karpathy via Forrest Chang)
1. Think before coding. State your assumptions. Surface tradeoffs.
   Ask before guessing. Push back when a simpler approach exists.
2. Simplicity first. Minimum code that solves the problem. No
   speculative features. No abstractions for single-use code.
3. Surgical changes. Touch only what is asked. Do not "improve"
   adjacent code, comments, or formatting. Match existing style.
4. Goal-driven execution. Define success criteria. Loop until
   verified. Do not narrate steps; tell me what success looks like.

## Extended (Mnimiy, May 2026)
5. Do not make the model do non-language work. Retry policies,
   routing, escalation thresholds belong in deterministic code.
6. Hard token budgets, no exceptions. Stop and ask if a task is
   trending past its budget.
7. Surface conflicts, do not average them. If two parts of the
   codebase disagree, flag the disagreement and ask which to follow.
8. Read before you write. Understand adjacent code (the file and
   nearby siblings) before adding new code.
9. Tests are required but are not the goal. A passing test that
   tests nothing useful is a failure. Tests must check behavior.
10. Long-running operations require checkpoints. After every
    significant step, summarize what was done and confirm before
    proceeding.
11. Convention beats novelty. In an established codebase, match
    the existing pattern even if a "better" one exists.
12. Fail visibly, not silently. Surface every skipped record,
    every rolled-back transaction, every constraint violation.
    Never report success when something was bypassed.

## Project-specific rules below this line
# (Add stack, test commands, error patterns specific to this repo.)
# Total file should stay under 200 lines.
```

---

## 5. 原始4条在哪些场景会静默失效

1. **长运行 agent 任务**：无预算、无 checkpoint、无 fail-loud 规则 → pipeline drift
2. **多代码库一致性**："match existing style" 假设只有一种风格，monorepo 12 个服务时随机选或平均化
3. **测试质量**："tests pass" 作为唯一目标 → Claude 写测试了但测试的是 nothing useful
4. **生产 vs 原型**："Simplicity First" 在需要 100 行 speculative scaffolding 的早期代码上 overfire

---

## 6. 被明确排除的失败实验

- **>14 条规则**：测试到 18 条时合规率从 76% 暴跌到 52%，Anthropic 200 行天花板真实存在
- **社交媒体的规则收集**：多为 Karpathy 4 条同义反复或领域特定规则（"always use Tailwind"），不通用
- **工具依赖型规则**："always use eslint" 在 eslint 未安装时静默失效 → 改为 "match the codebase's enforced style"
- **用例子代替规则**：3 个例子消耗 ≈10 条规则的上下文，且 Claude 会 over-fit
- **模糊强化词**："be careful", "think hard", "really focus" — 合规率 ~30%，不可测试
- **身份提示**："act like a senior engineer" 无效，Claude 已自认为 senior；差距在 think vs do，指令式规则才有效

---

## 7. 心智模型

> **CLAUDE.md 不是愿望清单。它是关闭你已观察到的具体失败模式的行为契约。**

每条规则都应回答：**这条规则防止什么错误？**

推荐策略：
- 诚实读完 12 条，保留你**这个月确实犯过**的映射规则
- 丢弃其余。6 条针对你真实失败模式的规则，胜过 12 条里 6 条你永远不触发的规则。
- 项目特定规则追加在底部，总长度保持 <200 行。

---

## 8. 迁移到 OpenClaw / AGENTS.md

Antigravity/OpenClaw 使用 `GEMINI.md` / `AGENTS.md`，形状相同：repo 根目录 Markdown，建议性而非强制，~200 行天花板。12 条几乎可逐字迁移。

OpenClaw 特别需注意：
- **Rule 6 (token budgets)**：OpenClaw quota 消耗比 Claude Code 更快，需配对 token 优化策略
- **Rule 10 (checkpoints)**：多 agent 运行第 4 步出错时，应从之前 artifact 恢复而非从头来
- **Rule 7 (surface conflicts)**：Claude ↔ Gemini 模型切换 mid-session 时，新模型常继承旧模型不兼容的上下文并试图调和
- **Rule 12 (fail visibly)**：auto-accept 模式下静默失败会在多个 Cmd-Enter 周期中累积，强制 agent 暴露每个跳过步骤

---

## 参考链接

- 原始4条仓库：forrestchang/andrej-karpathy-skills（125k+ stars）
- Mnimiy 长文（X，2026-05-09）：@mnilax — 2.7M views，18.8K bookmarks
- 本文拆解来源：https://antigravity.codes/blog/karpathy-claude-md-rules-extended
