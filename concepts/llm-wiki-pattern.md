# LLM Wiki (Karpathy Pattern)

- **类型**: 概念 / 知识管理方法论
- **提出者**: Andrej Karpathy (OpenAI联合创始人, ex-Tesla AI总监)
- **发布时间**: 2026-04-04
- **最后更新**: 2026-05-09

## 一句话定义

**LLM Wiki** 是Andrej Karpathy提出的使用LLM增量构建和维护个人知识库的模式——不是每次查询重新检索（RAG），而是让LLM持续编译、结构化、更新知识，实现"知识随时间增长而非每次归零"。

---

## 核心思想

### 传统RAG的问题

```
RAG流程：
用户提问 → 检索文档片段 → LLM基于片段回答 → 回答完即丢弃

问题：
- 每次回答都从零开始推导
- 没有跨会话积累
- 相同知识点反复检索
```

### LLM Wiki的模式

```
LLM Wiki流程：
读取源材料 → LLM分析 → 生成结构化wiki页面 → 持续更新维护 → 查询时直接读取wiki

优势：
- 知识编译一次，持续复用
- 增量更新，跨会话积累
- LLM消费自己的产出（AI-consumable exports）
```

---

## 架构分层

Karpathy原始设计（llm-wiki.md gist）:

| 层级 | 内容 | 作用 |
|------|------|------|
| **Layer 1: raw/** | 原始材料（文章、对话、论文摘要） | 不可变的输入层 |
| **Layer 2: wiki/** | LLM生成的结构化页面（实体、概念、合成） | 可更新的知识层 |
| **Layer 3: site/** | 导出的静态HTML/JSON-LD | 可消费的输出层 |

---

## 开源实现生态

| 项目 | 作者 | 特点 | Stars |
|------|------|------|-------|
| **Pratiyush/llm-wiki** | Pratiyush | 最完整实现，MCP server, Obsidian集成, 16 lint规则, confidence scoring | 快速增长中 |
| **nashsu/llm_wiki** | nashsu | 跨平台桌面应用，2-step ingest, 4-signal知识图谱, Louvain社区检测 | 新兴 |
| **domleca/llm-wiki** | domleca | Obsidian插件，Ollama本地运行，隐私优先 | Obsidian社区热门 |
| **本知识库** | ClawTest | OpenClaw cron驱动，AI Tech Intel专用，微信推送 | 定制版 |

---

## 关键特性（以Pratiyush/llm-wiki为例）

### 质量治理
- **4-factor confidence scoring** — 来源数量、来源质量、时效性、交叉引用
- **5-state lifecycle** — draft → reviewed → verified → stale → archived（90天自动stale）
- **16 lint rules** — 8结构规则 + 3 LLM规则 + 5 freshness规则

### AI消费接口
- `llms.txt` / `llms-full.txt` — 标准AI可读格式
- `graph.jsonld` — 知识图谱JSON-LD
- MCP server — 12个工具供任何MCP客户端查询

### 自动化
- SessionStart hook — 每次Claude Code启动自动同步
- Auto-build — 后台自动构建
- Auto Dream — 24h+5sessions后自动整理MEMORY.md

---

## 技术洞察

### 为什么这个模式重要？

1. **从"查询即计算"到"编译后查询"**
   - RAG = JIT编译（每次查询现场编译）
   - LLM Wiki = AOT编译（提前编译好，查询直接读取）

2. **AI agent的"长期记忆"基础设施**
   - Agent需要记住跨会话的知识
   - LLM Wiki提供结构化的外部记忆

3. **人机协作的新界面**
   - 人类提供源材料
   - LLM整理成wiki
   - 人类审查、纠正、补充
   - 其他AI查询wiki完成新任务

### 与当前知识库的对比

| 维度 | Karpathy原始 | Pratiyush实现 | 本知识库 (AI Tech Intel) |
|------|-------------|---------------|------------------------|
| 驱动方式 | 手动运行脚本 | CLI工具 | OpenClaw cron自动 |
| 内容来源 | 个人笔记/对话 | 多Agent适配器 | kimi_search + 网络 |
| 更新频率 | 按需 | 手动/自动可选 | 每日自动 |
| 推送渠道 | 本地浏览 | 静态网站/GitHub Pages | 微信推送 |
| 专注领域 | 通用个人知识 | 通用个人知识 | AI行业技术情报 |

---

## 相关页面

- [entities/andrej-karpathy.md](../entities/andrej-karpathy.md) — 模式提出者（待创建）
- [entities/pratiyush.md](../entities/pratiyush.md) — 主要实现者（待创建）
- [concepts/harness-methodology.md](harness-methodology.md) — 与Harness的关系（知识库是Harness的一部分）
- [index.md](../index.md) — 本知识库总览

## 外部链接

- Karpathy原始gist: https://gist.github.com/karpathy/llm-wiki.md
- Pratiyush实现: https://github.com/Pratiyush/llm-wiki
- nashsu桌面应用: https://github.com/nashsu/llm_wiki
- domleca Obsidian插件: https://github.com/domleca/llm-wiki
