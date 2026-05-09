# RLHF（人类反馈强化学习）

**类型**：训练方法 / 对齐技术  
**全称**：Reinforcement Learning from Human Feedback  
**核心作用**：让LLM"学会"人类的偏好和价值观

---

## 🧬 技术原理

### 三步流程
1. **预训练（Pre-training）**：海量文本自监督学习，模型学会语言规律
2. **SFT（Supervised Fine-Tuning）**：人类编写的"理想回答"训练，模型学会格式
3. **RLHF**：人类比较两个回答哪个更好 → 训练Reward Model → 用PPO算法优化策略

### 为什么需要RLHF？
- **SFT的局限**：人类标注成本高，模型只是"模仿"而非"理解"偏好
- **RLHF的突破**：让模型主动学习"什么回答人类更喜欢"
- **应用**：减少有害输出、提升 helpfulness、对齐人类价值观

---

## 🏛️ 发展时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2017 | OpenAI首次提出RLHF概念，用于游戏和机器人 | OpenAI博客 |
| 2020 | "Learning to Summarize from Human Feedback"论文 | arxiv.org |
| 2022-03 | InstructGPT发布，RLHF首次用于LLM对齐 | OpenAI论文 |
| 2022-11 | ChatGPT发布，RLHF成为行业标配 | OpenAI |
| 2023 | Claude、Llama 2等全面采用RLHF | 各厂商 |
| 2024 | **DPO（Direct Preference Optimization）**兴起，简化RLHF流程 | arxiv.org |
| 2025 | **RLAIF（AI Feedback）**：用AI替代人类标注，降低成本 | Google/Anthropic |
| 2026 | **DeepSeek-R1纯RL路线**：无需SFT，直接用RL训练推理能力 | DeepSeek |

---

## 🔑 关键变体方法

| 方法 | 原理 | 优势 | 代表模型 |
|------|------|------|----------|
| **PPO-RLHF** | 传统RL，训练Reward Model+PPO优化 | 效果稳定，广泛验证 | GPT-4、Claude 3 |
| **DPO** | 直接用偏好数据优化，无需Reward Model | 简单高效，训练快 | Llama 2、Mistral |
| **RLAIF** | 用AI（而非人类）生成反馈 | 成本低，可扩展 | Gemini、Claude |
| **纯RL（R1）** | 完全跳过SFT，RL从头训练 | 推理能力涌现 | DeepSeek-R1 |

---

## 🚀 前沿进展

### 1. DeepSeek-R1的纯RL突破
- **传统**：Pre-train → SFT → RLHF
- **R1**：Pre-train → **纯RL**（无SFT！）
- **结果**：推理能力（数学/代码）直接涌现
- **意义**：证明"推理可以通过自我强化获得，不需要昂贵的人类标注"
- **代价**：通用对话能力需后续SFT补充（R1-Zero → R1）

### 2. RLAIF（AI Feedback替代人类）
- **Google**：Constitutional AI（Claude的前身思路），用规则指导AI自我批评
- **优势**：人类标注 bottleneck 消除，可扩展
- **局限**：AI反馈质量取决于基础模型能力

### 3. 多模态RLHF
- **Gemini 2.5**：图像+文本+视频的联合偏好学习
- **挑战**：多模态偏好标注更复杂，成本更高

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| InstructGPT人类标注成本 | 数百万美元 | OpenAI论文 |
| DPO训练时间 | 比PPO快2-3倍 | 论文 |
| R1纯RL训练成本 | 远低于传统RLHF | DeepSeek |
| RLAIF降低标注成本 | 70%+ | Google论文 |

---

## 🔗 相关页面
- [entities/openai.md](../entities/openai.md) — InstructGPT/ChatGPT
- [entities/deepseek.md](../entities/deepseek.md) — R1纯RL路线
- [entities/anthropic.md](../entities/anthropic.md) — Constitutional AI
- [concepts/harness-methodology.md](harness-methodology.md) — Agent对齐

---

*最后更新：2026-05-09*  
*信息来源：OpenAI/DeepSeek/Google论文、arxiv.org*
