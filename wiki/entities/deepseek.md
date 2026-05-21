# DeepSeek

**类型**：模型厂商（中国）/ 开源先锋  
**总部**：中国杭州  
**关键人物**：梁文锋（创始人，幻方量化背景）, 高华佐（首席科学家）

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2023-07 | DeepSeek成立，由幻方量化孵化 | 公开报道 |
| 2024-01 | **DeepSeek-V2发布**，MoE架构（236B总量/21B激活），性价比轰动 | deepseek.com |
| 2024-05 | **DeepSeek-Coder-V2发布**，代码能力对标GPT-4 | deepseek.com |
| 2024-08 | **DeepSeek-V2.5发布**，对齐能力大幅提升 | deepseek.com |
| 2024-12 | **DeepSeek-V3发布**，671B参数MoE，训练成本仅557.6万美元 | deepseek.com |
| 2025-01 | **DeepSeek-R1发布**，推理模型，性能对标o1，开源MIT协议 | deepseek.com |
| 2025-02 | R1引发全球震动，NVIDIA股价单日跌17% | 股市数据 |
| 2025-03 | DeepSeek-V3-0324发布，编程能力大幅提升 | deepseek.com |
| 2025-05 | **DeepSeek-R1-0528发布**，推理更强，幻觉更少 | deepseek.com |
| 2025-06 | DeepSeek-V3.1发布，混合思考/非思考模式 | deepseek.com |
| 2026-01 | **DeepSeek-V4发布**，下一代MoE，性能再升级 | deepseek.com |
| 2026-03 | DeepSeek持续迭代，R1系列更新频率加快 | deepseek.com |
| 2026-04 | **DeepSeek-R1-0528升级版**，AIME 2025/GPQA/LCB_v6提升 | deepseek.com |

---

## 🔑 关键模型矩阵

| 系列 | 定位 | 架构 | 规模 | 开源状态 |
|------|------|------|------|----------|
| DeepSeek-V3 | 通用对话 | MoE（671B/37B激活） | 671B | **开源(MIT)** |
| DeepSeek-R1 | 深度推理 | 基于V3基座，RL训练 | 671B | **开源(MIT)** |
| DeepSeek-Coder | 代码专用 | 代码数据专门训练 | 33B | **开源** |
| DeepSeek-VL | 多模态 | 视觉-语言联合 | 7B/13B | **开源** |

---

## 🚀 核心技术路线

### 1. MoE（混合专家）架构
- **设计**：236B/671B总量，但每次只激活21B/37B参数
- **优势**：知识容量大（总参数多），推理成本低（激活参数少）
- **对比Dense模型**：用MoE实现"大模型能力，小模型成本"
- **DeepSeek创新**：多头潜在注意力（MLA）、无辅助损失的负载均衡

### 2. 极致成本优化
- **V3训练成本**：557.6万美元（对比GPT-4的1亿美元+）
- **方法**：
  - FP8混合精度训练
  - 专家并行+数据并行优化
  - 自研训练框架（非PyTorch/TensorFlow）
- **影响**：证明"好模型不一定需要天价训练成本"

### 3. 开源策略（MIT协议）
- **最宽松协议**：可商用、可修改、无需 attribution
- **与Meta对比**：Llama 2也有商用限制，DeepSeek完全放开
- **社区影响**：
  - 衍生模型数百个（Hugging Face）
  - 本地部署方案爆发（ds4、Ollama等）
  - 全球开发者免费获得SOTA模型

### 4. R1（推理模型）
- **训练方法**：纯RL（强化学习），无SFT（监督微调）
- **能力**：数学、代码、逻辑推理，对标OpenAI o1
- **R1-0528升级**：AIME 2025、GPQA、LCB_v6提升，幻觉减少
- **行业影响**：证明"推理能力可以通过RL获得，不需要昂贵的人类标注"

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| V3训练成本 | $557.6万 | deepseek.com |
| R1引发NVIDIA股价跌幅 | 17%（单日） | 股市数据 |
| Hugging Face下载量 | 数百万 | Hugging Face |
| API定价 | 比OpenAI低90%+ | deepseek.com |
| 团队规模 | 约200人（极精简） | 公开报道 |

---

## 🔗 相关页面
- [concepts/ds4.md](../concepts/ds4.md) — 本地部署方案
- [concepts/harness-methodology.md](../concepts/harness-methodology.md) — 对比Harness策略
- [entities/pratiyush.md](../entities/pratiyush.md) — ds4项目作者
- [entities/antirez.md](../entities/antirez.md) — Redis作者，ds4贡献者
- [concepts/processing-in-memory.md](../concepts/processing-in-memory.md) — 内存优化技术

---

*最后更新：2026-05-09*  
*信息来源：deepseek.com、GitHub、arxiv.org、公开报道*
