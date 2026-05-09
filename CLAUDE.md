# LLM Wiki - AI Tech Intel 知识库

## 这是什么

这是一个持续更新的AI前沿技术知识库，聚焦：
- **模型厂商**：Anthropic、Google、OpenAI、月之暗面、DeepSeek、Meta等
- **硬件厂商**：NVIDIA、三星、SK海力士、AMD、Intel等
- **关键技术方向**：
  - LLM Training & Inference Harness方法论
  - 存算一体 / 近存运算 (Processing-in-Memory / Near-Memory Computing)
  - 新架构、新芯片、新训练范式

## 目录结构

```
wiki/
├── index.md          # 总索引
├── log.md            # 操作日志（按时间线）
├── raw/              # 原始资料（文章、论文、报告）
├── entities/         # 实体页面（公司、产品、技术）
├── concepts/         # 概念页面（技术概念、方法论）
├── sources/          # 源文件摘要
└── weekly-digest/    # 每日/周摘要
```

## 页面格式

### 实体页面 (entities/)
- 公司名/产品名作为文件名
- 包含：简介、最新动态、技术栈、关键产品、时间线
- 示例：`entities/nvidia.md`、`entities/anthropic.md`

### 概念页面 (concepts/)
- 技术概念/方法论
- 包含：定义、原理、关键论文/产品、相关厂商
- 示例：`concepts/harness-methodology.md`、`concepts/processing-in-memory.md`

### 源文件摘要 (sources/)
- 每篇读过的文章/论文
- 包含：标题、来源、日期、关键要点、关联实体

## 工作流程

### 每日Ingest流程
1. 搜索当日/近期各厂商技术动态
2. 读取关键文章/论文
3. 创建/更新 sources/ 下的摘要
4. 更新相关 entities/ 页面
5. 更新相关 concepts/ 页面
6. 更新 index.md
7. 在 log.md 追加记录
8. 生成每日摘要到 weekly-digest/

### Lint规则
- 每周检查一次：orphan页面、过期声明、缺失交叉引用
- 确保所有实体页面都有最新动态时间戳

## 数据来源偏好

- **排除来源**：CSDN（信息质量不稳定）
- **优先来源**：
  - 厂商官方博客、arxiv、IEEE
  - 知名科技媒体（The Verge、TechCrunch、InfoQ、虎嗅等）
  - **行业大佬博客**（Andrew Ng, Andrej Karpathy, Yann LeCun, swyx, Simon Willison, Addy Osmani等）
  - **GitHub Trending / 特定仓库**（agent-skills, agent frameworks, ds4, llm-wiki等）
  - **社区论坛**（Hacker News, Reddit r/MachineLearning）
- **次选来源**：知乎高赞技术回答（需交叉验证）
