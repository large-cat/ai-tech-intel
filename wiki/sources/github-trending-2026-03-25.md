# GitHub Trending Weekly 2026-03-25 — Agent Skills Ecosystem Explosion

> **来源**: [ShareUHack Weekly Report](https://www.shareuhack.com/en/posts/github-trending-weekly-2026-03-25)
> **数据周期**: 2026-03-17 ~ 2026-03-25（滚动7天）
> **收集时间**: 2026-05-12

## 本周三大叙事线

1. **Skills 生态爆发** — Anthropic 开放标准后，5/10 新仓库与 skills 相关
2. **Flash-MoE** — 纯 C/Metal 推理引擎在 MacBook 上跑 397B 参数模型，HN 393 points
3. **Agent Harness 竞赛白热化** — everything-claude-code 与 superpowers 双双破 100K stars

---

## 🏆 Fastest Growing 周增速 Top 10

| # | 项目 | +Stars/周 | 总 Stars | 语言 |
|---|---|---|---|---|
| 1 🔁 | **affaan-m/everything-claude-code** | **+21,490** | 104,819 | JavaScript |
| 2 🔁 | **obra/superpowers** | **+19,621** | 110,358 | Shell |
| 3 🔁 | 666ghj/MiroFish | +11,768 | 41,818 | Python |
| 4 | Crosstalk-Solutions/project-nomad | +10,479 | 15,248 | TypeScript |
| 5 🔁 | bytedance/deer-flow | +10,201 | 43,085 | Python |
| 6 | jarrodwatts/claude-hud | +7,069 | 12,626 | JavaScript |
| 7 | FujiwaraChoki/MoneyPrinterV2 | +6,512 | 24,759 | Python |
| 8 | TauricResearch/TradingAgents | +6,234 | 40,792 | Python |
| 9 | unslothai/unsloth | +3,719 | 58,019 | Python |
| 10 | harry0703/MoneyPrinterTurbo | +1,637 | 52,574 | Python |

---

## 🆕 Top New Repos 本周新仓库 Top 15

| # | 项目 | Stars | 说明 |
|---|---|---|---|
| 1 | **MiniMax-AI/skills** | 3,867 | MiniMax 官方 Skills 包 |
| 2 | **HKUDS/ClawTeam** | 3,383 | Agent Swarm 智能，HKU 数据智能实验室 |
| 3 | VoltAgent/awesome-codex-subagents | 2,421 | 130+ Codex Subagent 精选列表 |
| 4 | danveloper/flash-moe | 1,847 | 纯 C/Metal 推理引擎 |
| 5 | dontbesilent2025/dbskill | 1,413 | 商业诊断 Skills |
| 6 | louislva/claude-peers-mcp | 1,109 | 多 Claude Code 实例通信 |
| 7 | math-inc/OpenGauss | 1,076 | Lean 工作流编排器 |
| 8 | lxf746/any-auto-register | 1,065 | 自动注册工具 |
| 9 | zarazhangrui/codebase-to-course | 1,055 | 代码库转互动课程 Skill |
| 10 | **slavingia/skills** | 1,038 | Sahil Lavingia (Gumroad 创始人) Skills |

---

## 重点深度

### everything-claude-code
- 起源于 Cerebral Valley × Anthropic Hackathon (2026年2月)
- 1,282 测试，98% 覆盖率，102 条静态分析规则
- 核心亮点：**内置 AgentShield 安全扫描器**
- 代表信号：开发者更想要"开箱即用"的 Agent Harness

### obra/superpowers
- 维护者：Jesse Vincent (Prime Radiant 团队)
- 最高总星数 Agent Harness (110K+)
- **方法论优先**：spec → plan → TDD red/green
- 社区活跃：已 fork 解决 amnesia、bloat、safety rails

### DeerFlow 2.0 (bytedance/deer-flow)
- 字节跳动2026年2月完全重写（与v1无共享代码）
- 企业级基础设施：Docker sandbox、文件系统、内存、技能、子Agent
- 持续多周进入月度趋势 → 长期维护信心

### MiroFish (666ghj)
- 作者 10 天 vibe-coding 构建
- 盛大集团 24 小时内承诺 $4.1M 天使投资
- "群集智能预测"：千个有记忆和行为的数字人自由交互
- 已接入 Polymarket 交易机器人，338 笔交易盈利 $4,266

### Flash-MoE (danveloper)
- 作者：Dan Woods，CVS Health VP of AI Platforms
- 纯 C + Objective-C + 手写 Metal shader
- MacBook Pro M3 Max (48GB RAM) 跑 Qwen3.5-397B-A17B
- 利用 MoE 特性：4/128 专家激活，专家 ~3.9MB，M3 Max SSD 17.5 GB/s
- 209GB 模型全存 SSD，非专家部分 5.5GB 常驻内存
- HN 核心讨论：非实时批处理场景 5.5 tokens/sec 完全可用

### ClawTeam (HKUDS)
- 香港大学数据智能实验室
- 核心设计：leader agent 调用 `clawteam spawn` 创建 worker
- 每个 worker 自动分配 git worktree + tmux window + identity
- demo：8 H100 GPU 协调 8 个专业子Agent
- 兼容：Claude Code、Codex、OpenClaw、nanobot、Cursor

---

## 🔑 本周核心洞察

**Skills Ecosystem: 从工具到知识分发基础设施**
> "Skills are quietly becoming the fundamental unit of AI agent knowledge — much like npm packages for the JavaScript ecosystem"
> — HN 讨论 "Skills are quietly becoming the unit of agent knowledge"

**本地推理边界快速扩展**
- Flash-MoE 397B 本地运行 + Unsloth Studio 本地微调
- Apple Silicon SSD 带宽 + 统一内存架构是技术底座
- 隐私敏感场景和推理成本敏感用户的"重新评估年"

**Agent Harness 竞赛：即插即用 vs 方法论**
- everything-claude-code = 工具优先（安装即用）
- superpowers = 方法论优先（spec → TDD）
- 两者不互斥，多数开发者同时使用
- 信号："如何让 AI Agent 做对" 已成为软件开发的一流问题
