# 月之暗面 (Moonshot AI)

**类型**：模型厂商（中国）  
**总部**：中国北京  
**关键人物**：杨植麟（创始人&CEO，清华+CMU背景）, 张宇韬（联合创始人）

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2023-03 | 月之暗面成立，获红杉中国、真格基金等投资 | 公开报道 |
| 2023-10 | **Kimi Chat发布**，长文本（20万字上下文）为核心卖点 | moonshot.cn |
| 2024-03 | Kimi智能助手App上线，支持联网搜索、文件阅读 | 应用商店 |
| 2024-05 | 完成超10亿美元融资，估值约25亿美元 | 36氪/彭博 |
| 2024-07 | **Kimi K1.5发布**，多模态推理模型，对标GPT-4o | moonshot.cn |
| 2024-10 | 支持200万字超长上下文 | moonshot.cn |
| 2025-01 | **Kimi k1.5深度思考版发布**，推理能力大幅提升 | moonshot.cn |
| 2025-03 | 完成新一轮融资，估值超30亿美元 | 36氪 |
| 2025-06 | **Kimi K2发布**，MoE架构（1T总量/32B激活），32B上下文 | moonshot.cn |
| 2026-01 | Kimi开放平台API 2.0发布，支持Function Calling、代码解释器 | moonshot.cn |
| 2026-04 | **Kimi K2.5发布**，推理能力再升级，多模态原生支持 | moonshot.cn |

---

## 🔑 关键模型矩阵

| 系列 | 定位 | 架构特点 | 上下文长度 | 最新版本 |
|------|------|----------|------------|----------|
| Kimi Chat | 通用对话 | Dense Transformer | 200万字 | Kimi Chat Pro |
| Kimi K1.5 | 多模态 | 视觉-语言联合训练 | 128K | K1.5 |
| Kimi K2 | 旗舰模型 | MoE（1T/32B激活） | 32K | K2 |
| Kimi K2.5 | 推理增强 | 测试时计算扩展 | 32K | K2.5 |

### Kimi K2.5 深度分析（2026-04发布）

**核心定位**：开源、原生多模态、Agent Swarm编排的推理增强模型

**技术架构**：
- **1.5T混合token预训练**：视觉token + 文本token联合预训练，非后期对齐
- **零视觉监督微调（Zero-shot Vision SFT）**：仅用文本数据微调就能激活视觉推理能力
- **Agent Swarm（智能体集群）**：最多100个子Agent并行运行，单任务1500次并行工具调用
- **PARL训练**：Parallel-Agent Reinforcement Learning，端到端时间减少80%，效率提升4.5倍
- **Kimi Code**：终端运行 + VSCode/Cursor/Zed IDE集成，SWE-Bench Verified 76.8%

**关键数据**：

| 指标 | 数据 | 来源 |
|------|------|------|
| 总参数量 | 1T（激活32B，MoE架构） | 官方 |
| 上下文长度 | 32K | 官方 |
| SWE-Bench Verified | 76.8% | 官方benchmark |
| Agent Swarm并行数 | 最多100个子Agent | 官方 |
| 并行工具调用 | 1500次/任务 | 官方 |
| 端到端效率提升 | 4.5×（vs传统串行Agent） | PARL训练 |
| API输入价格 | $0.6/M tokens | 官方定价（降价48%） |
| API输出价格 | $3/M tokens | 官方定价（降价60%+） |
| License | Modified MIT（非完全开源，限制大型商业平台直接使用） | 官方 |
| 公司估值 | $50亿 | 2026年报道 |

**战略意义**：
- **价格屠夫**：API定价比OpenAI/Anthropic低一个数量级，直接冲击商业模式
- **开源但不完全开放**：Modified MIT license允许自托管，但限制AWS/Azure/GCP等大型云平台直接转售
- **Agent原生设计**：不是"模型+Agent wrapper"，而是模型本身为Agent Swarm优化
- **IDE生态**：Kimi Code直接嵌入主流IDE，挑战Cursor/Windsurf等独立Agent IDE

---

## 🚀 核心技术路线

### 1. 超长上下文（Long Context）
- **核心差异化**：从诞生起就以"长文本"为卖点
- **技术演进**：20万字 → 200万字 → 无损长上下文
- **应用场景**：论文阅读、法律合同分析、小说创作、代码库理解
- **关键技术**：稀疏注意力、滑动窗口+全局注意力混合、上下文压缩

### 2. MoE架构（Kimi K2系列）
- **参数规模**：1T总量 / 32B激活（K2）
- **设计思路**：用更大总参数量换取更强知识容量，但保持推理成本可控
- **与DeepSeek对比**：月之暗面MoE更偏重消费级应用，DeepSeek更偏重推理效率

### 3. 多模态原生（K1.5/K2.5）
- **训练方式**：视觉-语言联合预训练，而非后期对齐
- **能力范围**：图像理解、视频分析、图表阅读、OCR
- **对标**：GPT-4o、Gemini 2.5 Flash

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| Kimi Chat用户数 | 数千万（2025年） | 公开报道 |
| 估值 | 30亿美元+（2025年） | 36氪/彭博 |
| K2训练算力 | 数万张GPU集群 | 行业估计 |
| 核心团队 | 清华+CMU+Google Brain背景 | 公开信息 |

---

## 🔗 相关页面
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — 对比中国厂商Agent策略
- [concepts/test-time-compute.md](../concepts/test-time-compute.md) — K2.5推理技术
- [weekly-digest/2026-05-09.md](../weekly-digest/2026-05-09.md) — 首日记录

---

*最后更新：2026-05-09*  
*信息来源：moonshot.cn、36氪、彭博、公开报道*
