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
| **HBM4** | **2026** | **2TB/s+, 16层** | **48GB/颗** | **NVIDIA Rubin/AMD MI400** |
| HBM4E | 2027（预计） | 2.4TB/s+, 16层 | 64GB/颗 | 下一代AI芯片 |
| HBM5 | 2028+（预计） | 3TB/s+ | 96GB+ | Feynman/下一代 |

---

## 🔑 关键技术指标

| 指标 | HBM3E | HBM4 | HBM4E | 提升逻辑 |
|------|-------|------|-------|----------|
| 每颗带宽 | 1.2TB/s | 2.0TB/s+ | 2.4TB/s+ | 更高频率+更多通道 |
| 堆叠层数 | 12层 | **16层** | 16层 | 3D封装技术进步 |
| 单颗容量 | 36GB | **48GB** | 64GB | 每层容量增加 |
| 功耗 | 较高 | 优化 | 更低 | 先进制程+电压优化 |
| 封装技术 | 热压缩键合 | **混合铜键合(HCB)** | HCB优化 | 更薄、散热更好 |

---

## 🏢 厂商竞争格局

| 厂商 | 份额(2025Q3) | 技术特点 | 关键客户 |
|------|-------------|----------|----------|
| **SK海力士** | **53%** | 先发优势，12层HBM3E成熟 | NVIDIA、AMD、Google |
| **三星** | **35%** | HBM4E 16Gbps/pin，HCB技术 | NVIDIA（VeraRubin） |
| **Micron** | **12%** | 追赶中，HBM3E刚量产 | 部分云厂商 |

**来源**：Counterpoint Research, 2025Q3 HBM市场份额报告 [来源链接待补充]

**关键动态**：
- **SK海力士**：VeraRubin HBM4独家供应商（与三星共同供应）
- **三星**：HBM4E 16Gbps/pin（对比HBM4的11.7Gbps），总带宽4TB/s
- **Micron**：未入选NVIDIA VeraRubin供应链，处于劣势

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
| HBM市场规模（2026E） | $300亿+ | 行业估计 [来源：待补充具体报告链接] |
| SK海力士HBM份额 | 53% | Counterpoint Research, 2025Q3 |
| 三星HBM份额 | 35% | Counterpoint Research, 2025Q3 |
| VeraRubin总HBM容量 | 576GB | NVIDIA官方GTC 2026披露 |
| AMD MI450 HBM容量 | 432GB | AMD官方披露 |

---

## 🔗 相关页面
- [entities/sk-hynix.md](../entities/sk-hynix.md) — SK海力士详情
- [entities/samsung.md](../entities/samsung.md) — 三星详情
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA HBM策略
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体（HBM的下一步）

---

*最后更新：2026-05-09*  
*信息来源：SK海力士/三星/Micron官方、Counterpoint、NVIDIA/AMD官方*
