# 先进封装（Advanced Packaging）

**类型**：半导体封装技术 / AI芯片核心基础设施  
**核心作用**：把多个芯片（Chiplet、HBM、逻辑Die）封装在一起，实现高带宽互联

---

## 🧬 技术原理

### 为什么需要先进封装？
摩尔定律放缓：单片大芯片（Monolithic）在3nm以下成本 prohibitively expensive：
- **良率暴跌**：芯片面积越大，缺陷概率指数增长（良率 ∝ e^(-面积)）
- **成本失控**：3nm单片芯片一片晶圆成本极高，且面积受光罩限制（~800mm²）
- **异构需求**：CPU/GPU/IO/内存需要不同制程，无法单片统一

### 先进封装的解法
- **拆分**：大芯片拆成多个小Die（Chiplet）
- **混搭**：每个Die用最合适的制程（核心3nm，IO 7nm，HBM独立）
- **高密度互连**：通过硅中介层/硅桥/有机基板实现Die间高速通信
- **结果**：成本降低、良率提升、性能提升（内存带宽翻倍级）

---

## 🏛️ 三大平台对比

| 平台 | 主导者 | 架构 | 特点 | 适用场景 | 2026状态 |
|------|--------|------|------|----------|----------|
| **CoWoS** | TSMC | 2.5D（硅中介层） | 密度最高、成本最高 | AI加速器（NVIDIA/AMD） | **Gen 6支持8 HBM4 + 双N3 Chiplet** |
| **EMIB** | Intel | 2D+（嵌入式硅桥） | 成本较低、尺寸灵活 | CPU/GPU/FPGA | **EMIB-T 2026投产，支持HBM4/5** |
| **Foveros** | Intel | 3D（有源堆叠） | 垂直密度最高、散热挑战 | 移动端/低功耗 | 3D堆叠，与EMIB组合为Co-EMIB |

---

## TSMC CoWoS（Chip-on-Wafer-on-Substrate）

### 技术原理
- 在硅中介层（Interposer）上放置计算Die和HBM堆叠
- 中介层提供高密度布线（~0.4μm线宽）
- 通过微凸点（Micro-bump）连接Die与中介层
- 整个组合再封装到有机基板上

### 世代演进

| 世代 | 时间 | 规模 | HBM支持 | 计算Die | 备注 |
|------|------|------|---------|---------|------|
| CoWoS-S | 2016-2020 | 1-2x光罩 | 4 HBM2 | 1 | 初代 |
| CoWoS-R | 2021-2022 | 2-4x光罩 | 4-6 HBM2E/3 | 1-2 | 有机中介层降本 |
| CoWoS-L | 2023-2025 | 5.5x光罩 | 6-8 HBM3E | 2 | 局部硅互连（LSI） |
| **CoWoS-L** | **2026** | **5.5x光罩** | **8 HBM3E** | **2** | **当前主力** |
| **CoWoS Gen 6** | **2026+** | **9.5x光罩(2027)** | **8 HBM4** | **双N3 Chiplet** | **2027目标** |

### 产能瓶颈
- **TSMC 2021年投资$2.8B** CoWoS产能
- **2026年宣布TWD 90B（约$3B）**新建专用先进封装厂
- **2026年交期6-9个月**
- Apple/NVIDIA/AMD竞争分配产能
- **100%领先CoWoS产能集中在台湾**——地缘风险巨大

> "Through 2027, HBM and CoWoS capacity allocation will determine AI accelerator market share more than chip architecture." — 行业共识

---

## Intel EMIB / EMIB-T / Foveros

### EMIB（Embedded Multi-die Interconnect Bridge）
- **2017年量产**：Sapphire Rapids Xeon、Ponte Vecchio GPU
- 在有机基板腔体内嵌入小硅桥Die
- **跳过TSV**——桥Die简单廉价
- 功率必须通过有机基板绕桥传输（长路径、高电阻）

### EMIB-T（2026投产）
Intel Foundry的翻身之作：
- **加入TSV**——桥Die支持垂直功率传输
- 集成MIM电容（噪声抑制）+ 铜接地网格（信号隔离）
- **45μm凸点间距**，路线图→35μm→25μm
- 能效：**~0.25 pJ/bit**
- UCIe-A：**32 Gb/s/pin或更高**
- 支持HBM3→HBM3E→**HBM4→HBM5**
- 封装尺寸可达**120mm×180mm**（38+桥接、12+光罩级Die）

### Intel vs TSMC 封装尺寸对标

| 年份 | Intel EMIB-T | TSMC CoWoS-L |
|------|-------------|-------------|
| 2026 | **8x光罩** | 5.5x光罩 |
| 2027 | 12x光罩 | **9.5x光罩** |
| 2028 | **12x+光罩** | — |

### 成本优势
- EMIB封装：**低数百美元/芯片**
- CoWoS（Rubin级）：**$900-1,000/芯片**
- 桥Die晶圆利用率：Intel **~90%** vs TSMC **~60%**

### 概念封装（Intel 2025.12发布）
- 16个计算元素跨8个基Die
- **24个HBM5堆叠**
- **10,296 mm²硅面积**
- **12x光罩尺寸**

### Foveros（3D堆叠）
- 有源芯片垂直堆叠（active-on-active）
- Lakefield处理器首次商用
- 与EMIB组合为**Co-EMIB**：灵活异构架构

---

## Samsung X-Cube

- **3D IC技术**：硅验证完成
- **唯一整合**：Foundry + Memory + 先进封装全在一家
- **劣势**：封装成熟度落后TSMC约一代
- **设计赢单有限**：难以撼动TSMC/NVIDIA的co-optimization关系

---

## 混合键合（Hybrid Bonding）

下一代互连技术：
- **TSMC SoIC**：sub-10μm pitch混合键合
- **Intel Foveros Direct**：sub-10μm pitch
- **优势**：比微凸点更高带宽密度、更低功耗
- **应用**：HBM堆叠、3D Chiplet垂直集成

---

## 玻璃基板（Glass Substrate）

- **Intel和TSMC 2026-2028路线图**
- **优势**：更低信号损耗、更高布线密度（vs有机基板）
- **IEEE研究**：高频互连通道中玻璃封装在信号/电源完整性上优于硅中介层
- **量产时间**：Intel目标3年内商业化就绪

---

## 供应链瓶颈

1. **CoWoS产能**：TSMC交期6-9个月，2027年前难缓解
2. **HBM供应**：SK海力士2026全年产能H1售罄
3. **ABF基板**：味之味积层膜短缺，新工厂2-3年投产
4. **KGD测试**：UCIe链路已知良片测试仍不成熟，Chiplet级良率损失在封装级乘法放大

---

## 地缘风险

- **100%领先CoWoS产能集中在台湾**
- 台湾冲突情景：立即中断80%+先进封装产能
- Intel+Samsung两年内无法吸收该需求
- 美国CHIPS法案、欧盟Chips法案：2027-2028才有意义产能
- 中国受限：ASML/Applied Materials出口管制，限制先进封装设备

---

## 市场数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 先进封装市场(2026E) | **$49-55B** | PatSnap行业分析 |
| 2.5D/3D封装CAGR | **10.1%** | 最快子赛道 |
| HBM市场(2027E) | **$33B** | Morgan Stanley |
| TSMC CoWoS投资 | **$2.8B(2021) + $3B(2026)** | TSMC官方 |
| OSAT CapEx增长 | **+27% YoY** | 2020年$6B |
| Intel EMIB成本 | **低数百美元/芯片** | Bernstein |
| CoWoS成本(Rubin级) | **$900-1,000/芯片** | Investing.com |

---

## 🔗 相关页面
- [concepts/chiplet.md](chiplet.md) — Chiplet设计范式
- [concepts/hbm.md](hbm.md) — HBM（先进封装的核心客户）
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA CoWoS依赖
- [entities/intel.md](../entities/intel.md) — Intel EMIB/Foveros
- [entities/tsmc.md](../entities/tsmc.md) — TSMC CoWoS产能

---

*最后更新：2026-05-10*  
*信息来源：PatSnap Eureka, Tom's Hardware, The Register, Intel/TSMC官方, Bernstein*
