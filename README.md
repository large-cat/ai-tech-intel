# 🤖 AI Tech Intel

**每日AI前沿技术情报知识库** — 追踪主流AI厂商动态、GitHub热门项目、行业大佬博客，增量式维护。

> 由 [OpenClaw](https://openclaw.ai) 自动维护，每天早上推送简报。

---

## 📦 仓库结构（llm-wiki 模式）

```
ai-tech-intel/
├── raw/              # 只读：原始事实来源（会话记录、原始资料）
├── wiki/             # LLM 读写：生成的知识页
│   ├── sources/      # 源文件摘要
│   ├── entities/     # 实体档案（公司、人物、产品）
│   ├── concepts/     # 技术概念（方法论、架构、算法）
│   ├── syntheses/    # 综合综述
│   ├── comparisons/  # 对比分析
│   ├── questions/    # 知识问答（中文Q&A）
│   ├── digest/       # 每日速递
│   ├── weekly-digest/# 每周摘要
│   └── ...           # 层级内容（agent-engineering/, hardware/ 等）
├── site/             # 只读：mdBook 构建产物（HTML）
├── tool/             # 读写：构建工具与脚本
│   └── knowledge_compiler.py
├── book.toml         # mdBook 配置
├── CLAUDE.md         # LLM 工作指引
├── HANDBOOK.md       # 使用手册
├── index.md          # 机器可读索引
├── log.md            # 操作日志
└── .github/workflows/# GitHub Pages 自动部署
```

## 📖 在线阅读

👉 [https://large-cat.github.io/ai-tech-intel/](https://large-cat.github.io/ai-tech-intel/)

---

## 🧭 快速导航

| 你想做什么 | 去哪 |
|-----------|------|
| **浏览知识** — 按主题/场景查找 | 👉 [HANDBOOK.md](HANDBOOK.md) |
| **了解项目** — 背景、方法论、信息源 | 👉 [ABOUT.md](ABOUT.md) |
| **AI查阅** — 结构化索引，机器可读 | 👉 [index.md](index.md) |
| **看今日摘要** — 当天重点 | 👉 [wiki/weekly-digest/](wiki/weekly-digest/) |
| **知识编译索引** — 目录→内容映射 | 👉 [wiki/knowledge-compiler/index.md](wiki/knowledge-compiler/index.md) |

---

## 📁 目录速览

### 🏢 厂商档案（19个）
Anthropic · OpenAI · Google DeepMind · 月之暗面 · DeepSeek · Meta · NVIDIA · AMD · 三星 · SK海力士 · Intel · Andrej Karpathy · Addy Osmani · antirez · Pratiyush · … → [全部](HANDBOOK.md#厂商档案)

### 🔬 技术概念（11个）
Harness方法论 · 存算一体 · 近存运算 · HBM · Chiplet · Agent Skills · RLHF · 测试时计算 · DS4 · LLM Wiki模式 → [全部](HANDBOOK.md#技术概念)

### 📄 源文件摘要（36篇）
Stripe Minions Blueprint · LangChain Terminal Bench 2.0 · AMD MI450对比 · Kimi K2.5 · NVIDIA Feynman · … → [全部](HANDBOOK.md#源文件摘要)

### 🧩 综合综述（3篇）
2026 AI行业趋势 · Agent工程全景 · 半导体硬件趋势 → [全部](wiki/syntheses/)

### ⚖️ 对比分析（2篇）
闭源vs开源厂商 · NVIDIA vs AMD → [全部](wiki/comparisons/)

### ❓ 知识问答（中文Q&A）
Harness方法论 · HBM4升级 · 2026范式转移 · Kimi K2.5 · … → [全部](wiki/questions/)

---

## 🔗 外部链接

- 知识库模式参考：[Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki)
- 本仓库由 [OpenClaw](https://openclaw.ai) 自动维护
- GitHub：[large-cat/ai-tech-intel](https://github.com/large-cat/ai-tech-intel)
