# HBM（高带宽内存）

**类型**：内存技术 / AI芯片关键组件  
**全称**：High Bandwidth Memory  
**核心作用**：解决AI推理的"内存带宽瓶颈"

---

## 🧬 技术原理

### 什么是HBM？
传统DRAM（如DDR4/DDR5）是"平面"布局——芯片平铺在PCB上。HBM采用**3D堆叠**：
- 多颗DRAM芯片垂直堆叠
- 通过**硅通孔（TSV, Through-Silicon Via）**连接
- 与GPU/CPU通过**中介层（Interposer）**紧密封装

### 为什么AI需要HBM？
AI推理是**内存带宽受限**，而非算力受限：
- Transformer模型每次推理需要加载全部权重
- 算力再强，如果内存带宽不够，GPU就在"等数据"
- **关键公式**：推理吞吐量 ∝ 内存带宽 / 模型权重大小

---

## 🏛️ 技术演进时间线

| 代际 | 时间 | 带宽/堆叠 | 容量 | 关键应用 |
|------|------|----------|------|----------|
| HBM1 | 2015 | 128GB/s, 4层 | 1GB | AMD Fiji GPU |
| HBM2 | 2016 | 307GB/s, 4/8层 | 4-8GB | NVIDIA V100 |
| HBM2E | 2020 | 460GB/s, 8层 | 16GB | NVIDIA A100 |
| HBM3 | 2022 | 819GB/s, 12层 | 24GB | NVIDIA H100 |
| HBM3E | 2024 | 1.2TB/s, 12层 | 36GB | NVIDIA H200/B200 |
| **HBM4** | **2026** | **2.0TB/s+, 16层** | **24-36GB/颗** | **NVIDIA Rubin/AMD MI400** |
| **HBM4E** | **2026H2(样品)** | **2.4TB/s+, 16层** | **48GB/颗** | **下一代加速器** |
| HBM5 | 2028+（预计） | 3+ TB/s | 64GB+ | Feynman/下一代 |

---

## 2026年HBM4量产最新动态

### Samsung — 率先宣布量产
- **2026年2月**：Samsung宣布开始HBM4量产出货（首批发货）
- 速度：**11.7 Gbps**（可超频至13 Gbps）
- 单堆叠带宽：最高**3.3 TB/s**
- 容量：24-36 GB（计划扩展至48 GB）
- 热阻改善+10%，散热改善+30%，能效提升+40%
- **HBM4E样品**：2026H2出货
- **销售预测**：2026年HBM销售额较2025年增长**3倍以上**
- **来源**：The Register, 2026-02-13

### Micron — 提前一个季度交付
- **2026年2月**：Micron CFO Mark Murphy宣布HBM4已进入高量产
- 速度：**>11 Gbps**
- **全年产能已预售完毕**
- HBM良率"on track"
- **股价反应**：消息发布后上涨近**10%**
- **来源**：Wolfe Research活动 / The Register, 2026-02-13

### SK海力士 — 市场领导者但未官宣HBM4
- **2025Q2 HBM份额62%**（行业最高）
- **2026全年产能H1 2025即售罄**
- 与Samsung共同供应NVIDIA VeraRubin HBM4
- **尚未宣布HBM4量产**（三大厂中唯一未官宣）
- 可能优先保障大客户（NVIDIA）供应而非公开announcement
- **来源**：PatSnap分析 / The Register

### 新需求方：Tesla Dojo
- Tesla成为HBM4新客户
- 同时向SK海力士和Samsung索取样品
- 用于Dojo超级计算机
- 需求基础从传统NVIDIA/AMD轴心扩大
- **来源**：The Register, 2026-02-13

---

## 🔑 关键技术指标

| 指标 | HBM3E | HBM4 | HBM4E | 提升逻辑 |
|------|-------|------|-------|----------|
| 每颗带宽 | 1.2TB/s | 2.0TB/s+ | 2.4TB/s+ | 更高频率+更多通道 |
| 堆叠层数 | 12层 | **16层** | 16层 | 3D封装技术进步 |
| 单颗容量 | 36GB | **24-36GB** | 48GB | 实际出货容量范围 |
| 功耗 | 较高 | 优化 | 更低 | 先进制程+电压优化 |
| 封装技术 | 热压缩键合 | **混合铜键合(HCB)** | HCB优化 | 更薄、散热更好 |

---

## 🏢 厂商竞争格局

| 厂商 | 份额(2025Q3) | 技术特点 | 关键客户 |
|------|-------------|----------|----------|
| **SK海力士** | **53%(Q3) / 62%(Q2)** | 先发优势，2026全年产能H1售罄 | NVIDIA、AMD、Google、Tesla |
| **三星** | **35%(Q3) / 17%(Q2)** | HBM4E 16Gbps/pin，HCB技术，**HBM4已出货** | NVIDIA（VeraRubin）、Tesla |
| **Micron** | **12%(Q3) / 21%(Q2)** | **HBM4已量产，全年预售完毕** | Tesla、云厂商 |

**来源**：Counterpoint Research, 2025Q3；PatSnap分析, 2026-04；The Register, 2026-02

**关键动态**：
- **SK海力士**：HBM市场绝对领导者，2026全年产能H1即售罄，与Samsung共同供应NVIDIA VeraRubin
- **三星**：率先宣布HBM4量产出货（2026.2），速度11.7 Gbps，散热/能效大幅改善
- **Micron**：HBM4提前一季度量产，全年产能预售完毕，股价涨10%，Tesla成为新客户
- **Tesla Dojo**：新晋HBM4需求方，同时向SK海力士和Samsung索取样品
- **供应紧张**：Samsung/Micron将产能转向高利润HBM，普通DRAM价格上涨

---

## 🚀 前沿技术

### 1. 混合铜键合（Hybrid Copper Bonding, HCB）
- **三星领先**：HCB支持16层以上堆叠，散热降低20%+
- **对比传统**：热压缩键合（TCB）需要高温高压，HCB在室温下完成
- **意义**：为HBM5（20+层）铺路

### 2. 定制化HBM（cHBM）
- **SK海力士**：将GPU/ASIC部分功能集成到HBM基板
- **目的**：减少数据移动，提升推理效率
- **信号**：客户从"纯性能"转向"推理效率+成本优化"

### 3. 容量扩展
- **当前**：16层堆叠 = 48GB/颗（HBM4）
- **未来**：20层+ = 96GB+/颗（HBM5）
- **制约因素**：散热、良率、成本

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| HBM市场规模（2027E） | **$330亿** | Morgan Stanley（PatSnap引用） |
| SK海力士HBM份额(Q2) | **62%** | PatSnap / 供应链 |
| 三星HBM份额(Q2) | **17%** | PatSnap |
| Micron HBM份额(Q2) | **21%** | PatSnap |
| HBM4 Samsung速度 | **11.7 Gbps** | Samsung官方 |
| HBM4 Micron速度 | **>11 Gbps** | Micron CFO |
| Micron股价涨幅(HBM4新闻) | **+10%** | 市场反应 |
| VeraRubin总HBM容量 | 576GB | NVIDIA官方GTC 2026披露 |
| AMD MI450 HBM容量 | 432GB | AMD官方披露 |

---

## 🔗 相关页面
- [entities/sk-hynix.md](../entities/sk-hynix.md) — SK海力士详情
- [entities/samsung.md](../entities/samsung.md) — 三星详情
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA HBM策略
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体（HBM的下一步）

---

*最后更新：2026-05-10*  
*信息来源：PatSnap Eureka, The Register, Tom's Hardware, Samsung/Micron官方, Counterpoint, NVIDIA/AMD官方*
