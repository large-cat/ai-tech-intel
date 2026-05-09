# Chiplet（芯粒）

**类型**：半导体封装技术 / 芯片设计范式  
**核心思想**：**把大芯片拆成小芯片（Chiplet），再封装在一起**

---

## 🧬 技术原理

### 为什么需要Chiplet？
传统单片芯片（Monolithic）的困境：
- **良率问题**：芯片越大，制造缺陷概率越高（良率 ∝ e^(-面积)）
- **成本问题**：大芯片需要最先进的制程，但先进制程每片晶圆成本极高
- **灵活性问题**：CPU/GPU/内存/IO需要不同制程，单片设计被迫统一

### Chiplet的解法
- **拆分**：大芯片拆成多个小Chiplet（如CPU核心、GPU核心、IO接口、内存控制器）
- **混搭**：每个Chiplet用最合适的制程（核心用3nm，IO用7nm）
- **封装**：通过高速互连（UCIe、Infinity Fabric）封装在一起
- **结果**：成本降低、良率提升、灵活性增加

---

## 🏛️ 发展时间线

| 时间 | 事件 | 来源 |
|------|------|------|
| 2017 | AMD首次大规模使用Chiplet：EPYC Naples（4个Die） | AMD |
| 2019 | AMD Ryzen 3000：CPU Chiplet + IO Die分离 | AMD |
| 2021 | Intel提出IDM 2.0，Chiplet为核心战略 | Intel |
| 2022 | **UCIe联盟成立**（Intel/AMD/ARM/TSMC等），统一Chiplet互连标准 | ucie.org |
| 2023 | Apple M3 Ultra：2个M3 Max拼接，112核GPU | Apple |
| 2024 | AMD MI300X：CPU+GPU+HBM的"超级Chiplet" | AMD |
| 2025 | Intel Panther Lake：全Chiplet设计 | Intel |
| 2026 | **AMD MI400**：CDNA 5 + HBM4 Chiplet | AMD |
| 2026 | **NVIDIA Rubin**：可能采用Chiplet架构（细节未公开） | 供应链 |

---

## 🔑 关键技术标准

| 标准 | 主导者 | 带宽 | 用途 |
|------|--------|------|------|
| **UCIe** | Intel（联盟） | 2-4TB/s/mm | Chiplet间互连行业标准 |
| **Infinity Fabric** | AMD | 定制 | AMD内部Chiplet互联 |
| **EMIB** | Intel | 高密度 | 2D/2.5D封装 |
| **Foveros** | Intel | 3D堆叠 | 垂直方向Chiplet堆叠 |
| **CoWoS** | TSMC | 高密度 | NVIDIA/AMD GPU+HBM封装 |

---

## 🏢 厂商策略

### AMD
- **最激进的Chiplet玩家**：从2017年起全线产品使用Chiplet
- **EPYC**：CPU核心Chiplet + IO Die分离，良率从30%提升到70%+
- **MI300X**：APU架构（CPU+GPU统一内存），但被批评"样样通样样松"
- **MI400**：回归纯GPU Chiplet，CDNA 5 + HBM4

### Intel
- **UCIe联盟主导者**：推动行业标准，打破 proprietary 互连
- **Foveros 3D**：Lakefield处理器首次商用3D Chiplet堆叠
- **Panther Lake（2025）**：全Chiplet设计，CPU+GPU+NPU分离
- **代工战略**：Intel Foundry对外提供Chiplet封装服务

### NVIDIA
- **相对保守**：GPU传统单片设计（Hopper/Blackwell）
- **Blackwell架构**：已有双Die拼接（GB200），但非全Chiplet
- **Rubin（2026）**：可能采用更多Chiplet设计（传闻）
- **优势**：单片设计内存带宽更高，但成本/良率压力大

### Apple
- **M系列Ultra**：2个Max Die拼接，GPU核心数翻倍
- **策略**：相对简单的2-Die拼接，非复杂多Chiplet
- **优势**：统一内存架构（UMA），CPU/GPU共享内存

---

## 🚀 前沿方向

### 1. 3D Chiplet堆叠
- **Intel Foveros**：上下两层芯片垂直堆叠，密度更高
- **TSMC SoIC**：更先进的3D封装，用于HBM堆叠
- **应用**：HBM本身就是3D Chiplet（DRAM层堆叠）

### 2. Optical I/O Chiplet
- **概念**：用光互连替代电互连，带宽提升10倍+
- **玩家**：Ayar Labs（Intel投资）、NVIDIA Research
- **瓶颈**：光电转换效率、成本

### 3. UCIe生态成熟
- **2026年**：首批UCIe兼容Chiplet产品上市
- **意义**：Chiplet从" proprietary 游戏"变为"开放生态"
- **影响**：小公司也能设计Chiplet，大厂提供互连/封装

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| AMD EPYC良率提升 | 30% → 70%+（Chiplet vs Monolithic） | AMD官方 |
| UCIe联盟成员 | 100+公司 | ucie.org |
| MI300X Die数量 | 13个Die（CPU+GPU+HBM） | AMD |
| CoWoS封装产能 | TSMC 2026年扩产50%+ | 供应链 |

---

## 🔗 相关页面
- [entities/amd.md](../entities/amd.md) — AMD Chiplet策略
- [entities/intel.md](../entities/intel.md) — Intel UCIe/Foveros
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA封装策略
- [concepts/hbm.md](hbm.md) — HBM本身就是3D Chiplet

---

*最后更新：2026-05-09*  
*信息来源：AMD/Intel/TSMC官方、UCIe联盟、供应链*
