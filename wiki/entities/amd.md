# AMD

**类型**：硬件厂商（GPU/CPU/FPGA）  
**总部**：美国加州Santa Clara  
**关键人物**：Lisa Su（CEO，2014年上任后股价涨50倍+）, Mark Papermaster（CTO）

---

## 🏛️ 时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 1969 | AMD成立，早期为Intel第二供应商 | amd.com |
| 2006 | 收购ATI，进入GPU市场 | AMD官方 |
| 2017 | **Ryzen处理器发布**，Zen架构翻身，Intel垄断被打破 | amd.com |
| 2021 | **EPYC服务器CPU份额突破20%**，数据中心市场站稳 | 市场报告 |
| 2022 | **MI200系列发布**，首款CDNA 2架构数据中心GPU | amd.com |
| 2023 | **MI300X发布**，192GB HBM3，对标NVIDIA H100 | amd.com |
| 2024 | **MI325X发布**，256GB HBM3E，AI推理专用 | amd.com |
| 2025 | **Zen 6 / Zen 7架构确认**，2026-2027年发布 | Financial Analyst Day |
| 2025 | **MI350系列发布**，CDNA 4架构，对标Blackwell | amd.com |
| 2026（预计） | **MI400系列发布**，CDNA 5架构，HBM4 | Financial Analyst Day |
| 2027（预计） | **MI500系列发布**，继续年度更新节奏 | Financial Analyst Day |

---

## 🔑 关键产品矩阵

| 系列 | 定位 | 架构 | 内存 | 对标NVIDIA |
|------|------|------|------|-----------|
| EPYC | 服务器CPU | Zen 5/6/7 | DDR5 | Intel Xeon |
| Instinct MI300X | AI训练 | CDNA 3 | 192GB HBM3 | H100 |
| Instinct MI325X | AI推理 | CDNA 3 | 256GB HBM3E | H100/H200 |
| Instinct MI350 | 新一代AI | CDNA 4 | HBM3E | Blackwell |
| Instinct MI400（2026） | 下一代 | CDNA 5 | **HBM4** | Rubin |
| Instinct MI500（2027） | 再下一代 | CDNA 6（预计） | HBM4E/HBM5 | Feynman |

---

## 🚀 核心技术路线

### 1. CDNA架构演进
- **CDNA 3（MI300系列）**：首次统一CPU+GPU（APC架构），但市场反馈"样样通样样松"
- **CDNA 4（MI350）**：专注GPU，放弃APC思路，算力对标Blackwell
- **CDNA 5（MI400，2026）**：HBM4加持，年度更新节奏，正面竞争Rubin

### 2. 年度更新战略
- **2025 Financial Analyst Day宣布**：数据中心GPU将**每年更新**
- **目的**：打破NVIDIA两年一代的节奏，用快速迭代抢占市场
- **风险**：研发压力大，软件生态（ROCm）仍需追赶CUDA

### 3. ROCm vs CUDA
- **现状**：ROCm支持PyTorch/TensorFlow，但生态成熟度远不及CUDA
- **差距**：大多数AI框架优先优化CUDA，ROCm为"第二优先级"
- **机会**：开源策略+社区贡献，部分云厂商（AWS/Azure）支持ROCm

### 4. MI450 vs Rubin 竞争态势（2026）

| 指标 | AMD MI450 | NVIDIA Rubin (Ultra) | 优势方 |
|------|-----------|---------------------|--------|
| **工艺** | TSMC 2nm | TSMC 3nm | **AMD**（更先进制程） |
| **架构** | CDNA 5 | 未知（新架构） | — |
| **HBM容量** | 432GB | 576GB (Ultra) / 288GB (R100) | **NVIDIA** |
| **带宽** | 19.6 TB/s | ~22 TB/s | 接近 |
| **FP4算力** | 40 PFLOPS | 50 PFLOPS | **NVIDIA** |
| **FP8算力** | 20 PFLOPS | 35 PFLOPS | **NVIDIA** |
| **功耗** | ~1500W | ~1800W (R100) / ~2300W (Ultra) | **AMD** |
| **散热** | 液冷 | 液冷（NVL72/NVL8标准） | 相同 |
| **送样/上市** | 2026H2 | 2026H2 | 相同 |
| **关键客户** | Meta ($100B deal)、OpenAI、Anthropic | 几乎所有云厂商+OpenAI | **NVIDIA**（更广） |

**关键竞争变量**：
- **工艺优势**：AMD MI450采用TSMC 2nm，比Rubin的3nm更先进，晶体管密度和能效比更优。这是AMD首次在工艺节点上领先NVIDIA。
- **内存差距**：Rubin Ultra 576GB vs MI450 432GB，144GB差距在大模型训练中可能是决定性优势。
- **软件生态**：NVIDIA CUDA vs AMD ROCm，差距仍在，但ROCm通过PyTorch/TensorFlow支持已大幅改善。
- **机架级设计**：AMD Helios是首个机架级AI设计（含EPYC CPU + Pensando DPU + 开放网络标准），NVIDIA Rubin依赖NVLink机架方案。
- **市场份额**：NVIDIA仍占~80%，但AMD+Meta $100B deal和Anthropic采用MI400系列正在改变格局。

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 数据中心收入（2025Q4） | 38亿美元 | AMD财报 |
| EPYC服务器份额 | 25%+ | Mercury Research |
| Instinct GPU收入（2025） | 约50亿美元 | 行业估计 |
| Lisa Su任内股价涨幅 | 50倍+（2014-2026） | 股市数据 |
| MI400预计发布时间 | 2026年H2 | Financial Analyst Day |

---

## 🔗 相关页面
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA竞争对比
- [concepts/hbm.md](../concepts/hbm.md) — HBM技术演进
- [concepts/chiplet.md](../concepts/chiplet.md) — AMD chiplet技术
- [weekly-digest/2026-05-09.md](../weekly-digest/2026-05-09.md) — 首日记录

---

*最后更新：2026-05-09*  
*信息来源：amd.com、Financial Analyst Day、财报、行业报告*
