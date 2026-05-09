# 🤖 AI Tech Intel

每日AI前沿技术情报知识库。自动追踪主流AI厂商、GitHub热门项目、行业大佬博客，增量式更新。

## 📅 每日摘要

| 日期 | 摘要 |
|------|------|
| [2026-05-09](weekly-digest/2026-05-09.md) | 首轮调研：Harness工程化、NVIDIA GTC 2026、存算一体 |

> 每天早上9:30推送微信简报，完整版在此。

## 📁 知识库结构

```
wiki/
├── index.md                  ← 总索引
├── CLAUDE.md                 ← 知识库schema与规则
├── log.md                    ← 操作日志
├── entities/                 ← 厂商/产品实体档案
│   ├── anthropic.md
│   ├── nvidia.md
│   ├── sk-hynix.md
│   └── samsung.md
├── concepts/                 ← 技术概念深度分析
│   ├── harness-methodology.md
│   ├── processing-in-memory.md
│   ├── agent-skills.md
│   ├── ds4.md
│   └── llm-wiki-pattern.md
├── sources/                  ← 源文件摘要（按日期）
└── weekly-digest/            ← 每日摘要（历史存档）
    ├── 2026-05-09.md
    └── _template.md
```

## 🔭 信息源

### 厂商
Anthropic · OpenAI · Google DeepMind · 月之暗面 · DeepSeek · Meta · NVIDIA · 三星 · SK海力士

### GitHub热门项目
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — AI编程Agent技能库
- [antirez/ds4](https://github.com/antirez/ds4) — DeepSeek V4 Flash专用推理引擎
- [Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki) — LLM Wiki模式实现
- [ruvnet/Ruflo](https://github.com/ruvnet/Ruflo) — Claude Agent编排平台
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) — 字节SuperAgent框架

### 行业大佬
Andrej Karpathy · Addy Osmani · swyx · Simon Willison · Andrew Ng

## ⏰ 更新节奏

| 时间（北京时间） | 动作 |
|------------------|------|
| 08:00 | 调研亚洲/欧洲时段更新 |
| 20:00 | 调研美国时段更新 |
| 09:30 | 微信推送当日简报 |

## 📜 方法论

基于 [Andrej Karpathy的LLM Wiki模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：
- **增量式维护** — 知识随时间增长，每次查询不从零推导
- **结构化页面** — 实体(厂商) + 概念(技术) + 源文件(单篇摘要)
- **AI可读导出** — 支持MCP server、JSON-LD图谱查询

## 🔗 相关链接

- 知识库模式参考：[Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki)
- 本仓库由 [OpenClaw](https://openclaw.ai) 自动维护
