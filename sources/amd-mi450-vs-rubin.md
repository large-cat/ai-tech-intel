# AMD MI450 vs NVIDIA Rubin 竞争分析

> 来源：Tom's Hardware, Wccftech, HotHardware, AMD Financial Analyst Day  
> 日期：2026-05  
> 关联：[entities/amd.md](../entities/amd.md) | [entities/nvidia.md](../entities/nvidia.md) | [concepts/hbm.md](../concepts/hbm.md)

---

## 核心对比

| 指标 | AMD MI450 | NVIDIA Rubin (R100) | NVIDIA Rubin Ultra |
|------|-----------|---------------------|---------------------|
| **架构** | CDNA 5 | 新一代 | 新一代 |
| **工艺** | **TSMC 2nm** | TSMC 3nm | TSMC 3nm |
| **HBM容量** | **432GB** | 288GB | **576GB** |
| **HBM带宽** | 19.6 TB/s | ~15 TB/s | **~22 TB/s** |
| **FP4算力** | 40 PFLOPS | 35 PFLOPS | **50 PFLOPS** |
| **FP8算力** | 20 PFLOPS | 25 PFLOPS | **35 PFLOPS** |
| **功耗** | **~1500W** | ~1800W | ~2300W |
| **散热** | 液冷 | 液冷 (NVL72/NVL8) | 液冷 (NVL72/NVL8) |
| **送样时间** | 2026H1 | 2026H2 | 2026H2 |
| **量产时间** | 2026H2 | 2026H2 | 2026H2 |

---

## AMD关键优势

### 1. 工艺领先

**TSMC 2nm vs 3nm**：
- AMD MI450采用TSMC 2nm，比Rubin的3nm更先进一代。
- 晶体管密度更高，同性能下功耗更低。
- **这是AMD首次在工艺节点上领先NVIDIA**。

### 2. 功耗效率

- MI450约1500W vs Rubin Ultra 2300W。
- 在数据中心功耗预算固定的情况下，MI450可部署更多卡。
- 对于推理工作负载（功耗敏感），MI450可能更优。

### 3. 机架级设计（Helios）

- AMD Helios是**首个机架级AI设计**。
- 包含：EPYC CPU + Pensando DPU + 开放网络标准（OCP）。
- 对比NVIDIA NVLink机架：更开放，不锁定在NVIDIA生态。

### 4. 关键客户

- **Meta**：签署$100B deal（多年期，多代GPU）。
- **Anthropic**： reportedly 使用MI400系列。
- **OpenAI**：也签署MI400部署协议。
- 这些客户的采购量足以支撑AMD生态。

---

## NVIDIA关键优势

### 1. 内存容量

- Rubin Ultra **576GB** vs MI450 **432GB**。
- 144GB差距在大模型训练中可能**决定性**。
- 更大的模型/更长的上下文需要更多HBM。

### 2. 算力领先

- FP4：50 vs 40 PFLOPS（+25%）。
- FP8：35 vs 20 PFLOPS（+75%）。
- 对于训练工作负载，NVIDIA仍领先。

### 3. 软件生态

- **CUDA**：20年积累，几乎所有AI框架优先优化CUDA。
- **ROCm**：支持PyTorch/TensorFlow，但仍是"第二优先级"。
- 大多数AI团队更熟悉NVIDIA工具链。

### 4. 市场份额

- NVIDIA仍占**~80%**数据中心GPU市场。
- 但AMD正在快速蚕食（从<5%到~15%）。

---

## 竞争动态

### NVIDIA的防御策略

- **提升Rubin功耗**：从1800W提升到2300W（Ultra版本），用功耗换性能来竞争MI455X。
- **锁定HBM供应**：与三星/SK海力士签署独家供应协议，限制AMD的HBM获取。
- **机架级整合**：NVL72/NVL8机架标准，提供完整解决方案而非单卡。

### AMD的进攻策略

- **工艺领先**：2nm工艺是长期技术优势。
- **开放生态**：ROCm开源，支持开放标准（OCP、UCIe）。
- **价格竞争**：MI450定价预计比Rubin低20-30%。
- **客户绑定**：Meta $100B deal确保长期收入。

---

## 市场影响

| 场景 | 赢家 | 原因 |
|------|------|------|
| 大模型训练 | NVIDIA | 576GB HBM + 更高FP8算力 |
| 推理部署 | AMD | 更低功耗 + 2nm工艺效率 |
| 开放生态 | AMD | ROCm开源 + OCP标准 |
| 软件成熟度 | NVIDIA | CUDA 20年积累 |
| 价格敏感客户 | AMD | 定价低20-30% |
| 超大规模云 | 两者共存 | Meta用AMD，Google/Microsoft继续NVIDIA |

---

## 引用来源
- Tom's Hardware：tomshardware.com（2026-05，AMD MI450规格分析）
- Wccftech：wccftech.com（2026-05，MI450 vs Rubin对比）
- HotHardware：hothardware.com（2026-05，AMD GPU路线图）
- AMD Financial Analyst Day：amd.com（2025，CDNA 5架构预告）
- 供应链消息：Digitimes（2026-01，MI400系列时间线）
