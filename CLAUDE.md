# LLM Wiki - AI Tech Intel 知识库

## 这是什么

这是一个持续更新的AI前沿技术情报知识库，聚焦：
- **模型厂商**：Anthropic、Google、OpenAI、月之暗面、DeepSeek、Meta等
- **硬件厂商**：NVIDIA、三星、SK海力士、AMD、Intel等
- **关键技术方向**：
  - LLM Training & Inference Harness方法论
  - 存算一体 / 近存运算 (Processing-in-Memory / Near-Memory Computing)
  - 新架构、新芯片、新训练范式

## 仓库结构（llm-wiki 模式）

```
ai-tech-intel/
├── raw/              # 只读 — 原始事实来源（会话记录、原始资料）
├── wiki/             # LLM 读写 — 生成的知识页
│   ├── sources/      # 源文件摘要（文章、论文、报告）
│   ├── entities/     # 实体页面（公司、产品、人物、技术）
│   ├── concepts/     # 概念页面（技术概念、方法论）
│   ├── syntheses/    # 综合综述（跨实体/概念的主题分析）
│   ├── comparisons/  # 对比分析（产品对比、技术路线对比）
│   ├── questions/    # 知识问答（中文Q&A系统）
│   ├── digest/       # 每日速递
│   ├── weekly-digest/# 每周/日摘要
│   ├── knowledge-compiler/  # 知识编译输出
│   │   ├── index.md      # 目录→内容映射索引
│   │   ├── graph.jsonld  # 机器可读知识图谱
│   │   └── stats.json    # 统计数据
│   └── ...           # 层级内容（agent-engineering/, hardware/, vendors/ 等）
├── site/             # 只读 — mdBook 构建产物（HTML）
├── tool/             # 读写 — 构建工具与脚本
│   └── knowledge_compiler.py
├── book.toml         # mdBook 配置
├── index.md          # 机器可读总索引
├── log.md            # 操作日志
└── README.md         # 项目总览
```

## 六层知识架构（Karpathy Pattern）

```
Layer 1: raw/          — 原始事实（只读）
Layer 2: wiki/sources/ — 源文件摘要
Layer 3: wiki/entities/ — 实体档案
Layer 4: wiki/concepts/ — 技术概念
Layer 5: wiki/syntheses/ + comparisons/ — 综合与对比
Layer 6: wiki/questions/ — 中文Q&A（面向用户）
```

## 页面格式

### 实体页面 (wiki/entities/)
- 公司名/产品名/人物名作为文件名
- 包含：简介、最新动态、技术栈、关键产品、时间线
- 示例：`wiki/entities/nvidia.md`、`wiki/entities/anthropic.md`

### 概念页面 (wiki/concepts/)
- 技术概念/方法论
- 包含：定义、原理、关键论文/产品、相关厂商
- 示例：`wiki/concepts/harness-methodology.md`

### 源文件摘要 (wiki/sources/)
- 每篇读过的文章/论文
- 包含：标题、来源、日期、关键要点、关联实体/概念的 [[wikilink]]

### 综合综述 (wiki/syntheses/)
- 跨实体/概念的主题分析
- 包含：核心判断、证据矩阵、演进路线、待回答问题

### 对比分析 (wiki/comparisons/)
- 产品对比、技术路线对比、厂商对比
- 包含：差异矩阵、具体指标对比、关键变量

### 知识问答 (wiki/questions/)
- 中文Q&A，基于现有 sources/ 综合生成
- 格式：一句话回答 → 详细解释 → 延伸阅读
- 引用格式：关联实体/概念 + 来源链接

## 工作流程

### 每日Ingest流程
1. 搜索当日/近期各厂商技术动态
2. 读取关键文章/论文
3. 创建/更新 wiki/sources/ 下的摘要（添加 [[wikilinks]] 指向相关实体/概念）
4. 更新相关 wiki/entities/ 页面
5. 更新相关 wiki/concepts/ 页面
6. 运行 `python3 tool/knowledge_compiler.py` 重新编译知识索引
7. 更新 wiki/index.md 和 log.md
8. 生成每日摘要到 wiki/weekly-digest/
9. mdbook build 构建 site/

### 知识编译（Knowledge Compiler）
- 运行 `python3 tool/knowledge_compiler.py`
- 输出：
  - `wiki/knowledge-compiler/index.md` — 人类可读索引（目录→内容映射）
  - `wiki/knowledge-compiler/graph.jsonld` — 机器可读知识图谱
  - `wiki/knowledge-compiler/stats.json` — 统计数据
- 自动识别 sources/ 中对 entities/ 和 concepts/ 的引用关系
- 生成反向索引：每个实体/概念被哪些来源引用

### 知识问答生成流程
1. 用户提问
2. 查 `wiki/knowledge-compiler/index.md` 或 `graph.jsonld` 定位覆盖度
3. 如有答案 → 综合现有 sources/ 生成回答，记录到 wiki/questions/
4. 如发现缺口（实体/概念无来源引用）→ 创建调研任务 → 补充 sources/ → 更新实体/概念 → 重新编译 → 知识树自动生长

## Lint规则
- 每周检查一次：orphan页面、过期声明、缺失交叉引用
- 确保所有实体页面都有最新动态时间戳
- 运行 `mdbook build` 前检查 {{#include}} 路径有效性

## 数据来源偏好

- **排除来源**：CSDN（信息质量不稳定）
- **优先来源**：
  - 厂商官方博客、arxiv、IEEE
  - 知名科技媒体（The Verge、TechCrunch、InfoQ、虎嗅等）
  - **行业大佬博客**（Andrew Ng, Andrej Karpathy, Yann LeCun, swyx, Simon Willison, Addy Osmani等）
  - **GitHub Trending / 特定仓库**（agent-skills, agent frameworks, ds4, llm-wiki等）
  - **社区论坛**（Hacker News, Reddit r/MachineLearning）
- **次选来源**：知乎高赞技术回答（需交叉验证）
