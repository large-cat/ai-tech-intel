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
| 2026 | **UCIe联盟达120+成员**（Intel/AMD/TSMC/Samsung/ARM/Meta/Google），专有Die-to-Die链路走向过时 | PatSnap |
| 2026 | **Chiplet互连专利达1,070件/年**（2017年仅152件，7倍增长） | PatSnap专利数据库 |
| 2026 | **先进封装市场$49-55B**（2020年$24B翻倍） | 行业分析 |
| 2026 | **2.5D/3D封装增速10.1% CAGR** — 最快子赛道 | PatSnap |
| 2026H1 | SK海力士2026全年HBM产能售罄 | 供应链 |
| 2026Q1 | Samsung、Micron开始出货HBM4 | The Register |
| 2026 | Intel EMIB-T进入生产工厂投产，支持HBM4/HBM5 | Tom's Hardware |
| 2026 | TSMC CoWoS Gen 6支持8颗HBM4 + 双计算Chiplet(N3) | 供应链 |
| 2026 | Tesla成为HBM4新客户（Dojo超算） | The Register |
| 2026 | UCIe 2.0预计引入：64 Gbps + 光学Die-to-Die | UCIe联盟路线图 |

---

## 🔑 关键技术标准

### UCIe（Universal Chiplet Interconnect Express）

UCIe是2022年3月由Intel/AMD/ARM/TSMC/Google/Meta/Microsoft/Qualcomm/Samsung/ASE联合发起的开放标准，目标是让不同厂商、不同工艺的Chiplet能在同一个封装内互操作。

#### 三层协议栈

```
┌─────────────────────────────────────────┐
│  Protocol Layer                         │
│  PCIe 6.0 / CXL 2.0~3.0 / Streaming    │
│  （兼容现有生态，即插即用）               │
├─────────────────────────────────────────┤
│  Die-to-Die Adapter Layer               │
│  • 链路初始化与参数协商                  │
│  • 多协议复用（Arb/Mux）                 │
│  • CRC + Retry 错误恢复                  │
│  • 链路状态/功耗管理                     │
├─────────────────────────────────────────┤
│  Physical Layer                         │
│  • 电气AFE（Tx/Rx）                      │
│  • 时钟转发（Clock Forward）             │
│  • 边带通道（Sideband）参数交换          │
│  • 链路训练/校准/修复（Lane Repair）     │
└─────────────────────────────────────────┘
```

#### 核心KPI

| 指标 | 标准封装(2D) | 先进封装(2.5D) | 对比基准(PCIe) |
|------|------------|--------------|--------------|
| **带宽密度(线性)** | 28-224 GB/s/mm | 165-1317 GB/s/mm | PCIe: ~10 GB/s/mm |
| **带宽密度(面积)** | 1.5-6.5 TB/s/mm² | 9-38 TB/s/mm² | — |
| **单pin数据率** | 最高32 Gbps | 最高64 Gbps | PCIe 5.0: 32 GT/s |
| **端到端延迟** | <2 ns | <2 ns | PCIe: ~20 ns |
| **功耗效率** | 0.5 pJ/bit | 0.25 pJ/bit | PCIe: ~5-10 pJ/bit |
| **误码率(BER)** | <1e-15 | <1e-15 | — |

#### 封装类型支持

- **UCIe-S（Standard）**：2D有机基板，成本低，距离长（~25mm），凸点间距25-55μm
- **UCIe-A（Advanced）**：2.5D硅中介层/EMIB，距离短（~2mm），凸点间距25-45μm
- **UCIe 3D**：垂直堆叠（开发中），通过TSV实现

#### 版本演进

| 版本 | 时间 | 关键新增 |
|------|------|---------|
| **UCIe 1.0** | 2022-03 | 首发，支持2D/2.5D，PCIe/CXL/Streaming协议 |
| **UCIe 1.1** | 2024 | 链路健康监控、运行时parity、合规性改进 |
| **UCIe 2.0** | 2025-08 | **3D封装支持**、可管理性、调试/测试架构 |
| **UCIe 3D** | 开发中 | 垂直堆叠，简化Chiplet连接 |

#### 物理层细节

- **Lane模块**：1个Module = 16条SE（单端）Lane或64条差分Lane（先进封装）
- **Link组成**：1、2或4个Module组成一个双向Link
- **Bump-out规格**：规范明确定义凸点布局，支持Die旋转/镜像，确保即使未来凸点间距缩小仍能互操作
- **Lane Repair**：支持坏Lane自动屏蔽和重映射，提升良率

#### 与专有互连的对比

| 标准 | 数据率/lane | 带宽密度 | 延迟 | 开放/专有 |
|------|-----------|---------|------|----------|
| **UCIe** | 最高64 GT/s | >20 Tbps/mm² | <4 ns | **开放** |
| AIB (Intel) | 2 GT/s | 504 Gbps/mm | 5 ns | 专有 |
| Lipincon (TSMC) | 8-16 GT/s | 536 Gbps/mm | 14 ns | 专有 |
| Bunch of Wires | 2-16 GT/s | 1280 Gbps/mm | 5 ns | 开放(OCP) |
| XSR/USR (Rambus) | 16-56 GT/s | N/A | N/A | 专有 |

#### 产业意义

- **打破专有壁垒**：Intel的AIB、AMD的Infinity Fabric、TSMC的Lipincon互不兼容 → UCIe统一
- **Chiplet民主化**：小公司可以设计专用Chiplet（如AI加速器、射频、传感器），大厂提供互连/封装
- **代工灵活性**：AMD可以用TSMC工艺做计算Die + Intel Foundry做IO Die，通过UCIe封装在一起
- **2026年首批UCIe兼容产品**：首批基于UCIe的Chiplet系统上市

### 其他专有互连

| 标准 | 主导者 | 带宽 | 用途 |
|------|--------|------|------|
| **Infinity Fabric** | AMD | 定制 | AMD内部Chiplet互联（EPYC/MI系列） |
| **EMIB** | Intel | 高密度 | 2D/2.5D封装（Sapphire Rapids/Ponte Vecchio） |
| **Foveros** | Intel | 3D堆叠 | 垂直方向Chiplet堆叠（Lakefield） |
| **CoWoS** | TSMC | 高密度 | AI加速器封装（NVIDIA/AMD GPU+HBM） |
| **SoIC** | TSMC | sub-10μm pitch | 3D Chiplet垂直集成（混合键合） |



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

*最后更新：2026-05-10*  
*信息来源：AMD/Intel/TSMC官方、UCIe联盟、供应链*
