# OpenAI

**类型**：模型厂商 / 平台型公司  
**总部**：美国旧金山  
**关键人物**：Sam Altman (CEO), Greg Brockman, Ilya Sutskever (前首席科学家), Mark Chen (VP Research), Noam Brown (推理研究)

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2015-12 | OpenAI成立，非营利AI研究机构 | openai.com |
| 2018-06 | GPT-1发布（1.17亿参数），无监督预训练+微调范式确立 | arxiv.org |
| 2019-02 | GPT-2发布（15亿参数），因"太危险"暂缓完整开源 | openai.com |
| 2019-07 | 从非营利转为"利润上限"模式，获微软10亿美元投资 | openai.com |
| 2020-06 | GPT-3发布（1750亿参数），API商业化启动 | arxiv.org |
| 2022-11 | ChatGPT发布（基于GPT-3.5），5天用户破百万 | openai.com |
| 2023-03 | GPT-4发布，多模态能力、更可靠但闭源 | openai.com |
| 2023-11 | GPT-4 Turbo + GPTs（自定义Agent）+ Assistants API | openai.com/devday |
| 2024-05 | GPT-4o（"omni"）发布，原生多模态，延迟大幅降低 | openai.com |
| 2024-09 | o1-preview / o1-mini 发布，测试时计算扩展（Test-Time Compute） | openai.com |
| 2024-12 | o3 / o3-mini 发布，推理能力大幅跃升，ARC-AGI突破 | openai.com |
| 2025-01 | ChatGPT Operator发布，AI Agent可自主浏览网页执行任务 | openai.com |
| 2025-03 | GPT-4.5发布，"情商最高"的模型，规模巨大但推理成本极高 | openai.com |
| 2025-05 | Codex CLI / Codex Agent 发布，终端AI编码助手 | openai.com |
| 2026-02 | **Harness Engineering方法论公开**：100万行AI编写生产代码，零手写 | OpenAI工程博客 |
| 2026-03 | **GPT-OSS-120B开源**：MoE架构（117B总量/5.1B激活），RL训练 | arxiv.org |
| 2026-04 | o4-mini 发布，低成本推理模型，API定价$1.10/$4.40 per 1M tokens | openai.com |
| 2026-05 | Stargate项目推进，与SK海力士/三星签署90万片DRAM晶圆/月供应意向 | 供应链消息 |

---

## 🔑 关键模型矩阵

| 系列 | 定位 | 架构特点 | 最新版本 | 开源状态 |
|------|------|----------|----------|----------|
| GPT系列 | 通用对话 | Dense Transformer | GPT-4.5 | 闭源 |
| o系列 | 深度推理 | Test-Time Compute Scaling | o4-mini | 闭源 |
| Codex | 代码Agent | Agentic Coding | Codex CLI | 闭源（产品） |
| GPT-OSS | 开源旗舰 | MoE（117B/5.1B激活） | GPT-OSS-120B | **开源** |

---

## 🚀 核心技术路线

### 1. Test-Time Compute Scaling（测试时计算扩展）
- **核心思想**：在推理阶段投入更多计算资源（更多思考步骤、更多验证），而非仅扩大模型规模
- **o系列模型**：o1→o3→o4，每次迭代都在推理时"多想一会"
- **关键论文**："Scaling LLM Test-Time Compute Optimally"（2024）
- **影响**：改变了"更大模型=更好性能"的单一范式

### 2. Harness Engineering
- **2026年2月公开**：团队交付100万行生产代码，零手写
- **人类角色**：设计约束、反馈循环、文档结构、依赖规则
- **Agent角色**：写代码、生成测试、部署
- **核心公式**：`Agent = Model + Harness`
- **与Anthropic差异**：OpenAI走"Raw Power"路线，Anthropic走"结构化可靠性"路线

### 3. MoE架构探索（GPT-OSS-120B）
- **参数规模**：117B总量 / 5.1B激活
- **架构细节**：
  - 36层Transformer
  - 128个专家 (experts)，top-4 routing
  - Hidden dimension 2880
  - 64个attention heads
  - Grouped Query Attention (group size 8)
  - 128K context window
- **量化**：原生MXFP4量化（仅MoE权重），BF16用于其他tensor
- **训练方法**：RL（强化学习）而非SFT+DPO
- **开源许可**：Apache 2.0 license（可商用、可修改、可分发）
- **可配置推理**：reasoning effort可调（low/medium/high）
- **意义**：OpenAI首次开源Tier 2旗舰模型，验证MoE+RL的可行性

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| ChatGPT周活用户 | 5亿+（2026年初） | OpenAI官方 |
| API开发者 | 300万+ | OpenAI官方 |
| o4-mini定价 | $1.10/$4.40 per 1M tokens | openai.com |
| GPT-4.5定价 | $75/$150 per 1M tokens | openai.com |
| Stargate项目预算 | $5000亿（10年计划） | 公开报道 |

---

## 🔗 相关页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — Harness方法论深度分析
- [concepts/test-time-compute.md](../concepts/test-time-compute.md) — 测试时计算扩展详解
- [concepts/rlhf.md](../concepts/rlhf.md) — RLHF训练方法
- [weekly-digest/2026-05-09.md](../weekly-digest/2026-05-09.md) — 首日Harness Engineering记录

---

*最后更新：2026-05-09*  
*信息来源：OpenAI官方博客、arxiv.org、infoq.com、工程博客*
