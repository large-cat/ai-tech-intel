# 先进封装（Advanced Packaging）

**类型**：半导体封装技术 / AI芯片核心基础设施  
**核心作用**：把多个芯片（Chiplet、HBM、逻辑Die）封装在一起，实现高带宽互联

---

## 🧬 技术原理深度版

### 为什么需要先进封装？

摩尔定律放缓：单片大芯片（Monolithic）在3nm以下成本 prohibitively expensive：
- **良率暴跌**：芯片面积越大，缺陷概率指数增长（良率 $\propto e^{-D_0 \cdot A}$，$D_0$ = 缺陷密度）
- **成本失控**：3nm单片芯片一片晶圆成本极高，且面积受光罩限制（~800mm²，Reticle Limit）
- **异构需求**：CPU/GPU/IO/内存需要不同制程，无法单片统一

### 先进封装的解法

$$C_{total} = \sum_{i} C_{die,i} + C_{packaging} + C_{yield\_loss}$$

当 $C_{packaging} + C_{yield\_loss} < C_{monolithic\_yield\_loss}$ 时，Chiplet划算。

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

### 技术原理深度版

**结构层次**：
```
┌─────────────────────────────────────────┐
│  计算Die + HBM堆叠（顶部）               │  ← C4凸点（~150μm）
├─────────────────────────────────────────┤
│  硅中介层（Silicon Interposer）          │  ← 核心创新层
│  ├── 亚微米布线（0.4μm线宽/间距）        │
│  ├── TSV穿透（10-20μm直径）              │
│  └── 光罩拼接（Reticle Stitching）       │
├─────────────────────────────────────────┤
│  有机基板（Organic Substrate）            │  ← C4凸点（~150μm）
│  └── PCB级布线（~10μm线宽）              │
└─────────────────────────────────────────┘
```

**中介层制造关键工艺**：

1. **硅片准备**：300mm SOI或bulk硅片
2. **前段FEOL**：CMOS兼容工艺制造TSV和互连线
3. **TSV刻蚀**：Bosch DRIE工艺，深宽比 10:1
   - 刻蚀深度：~100μm
   - TSV直径：10-20μm
   - 侧壁角度：~89°（接近垂直）
4. **绝缘层沉积**：TEOS氧化物 liner，厚度 ~1μm
5. **阻挡层/种子层**：Ti/TiN阻挡层 + Cu种子层（PVD）
6. **Cu电镀填充**：自下而上填充（Bottom-up plating），防止空洞
7. **CMP平坦化**：化学机械抛光，暴露TSV顶部
8. **后段BEOL**：多层Cu互连（~4层），线宽 0.4μm
9. **凸点制备**：UBM（Under Bump Metallurgy）+ 焊球（SAC305）

**世代演进**

| 世代 | 时间 | 中介层尺寸 | HBM支持 | 计算Die | 布线层数 | 光罩拼接 | 备注 |
|------|------|-----------|---------|---------|----------|----------|------|
| CoWoS-S | 2016-2020 | 1-2x光罩 | 4 HBM2 | 1 | 2层 | 无 | 初代 |
| CoWoS-R | 2021-2022 | 2-4x光罩 | 4-6 HBM2E/3 | 1-2 | 2层 | 有 | 有机中介层降本 |
| CoWoS-L | 2023-2025 | 5.5x光罩 | 6-8 HBM3E | 2 | 3层 | 有 | 局部硅互连（LSI） |
| **CoWoS-L** | **2026** | **5.5x光罩** | **8 HBM3E** | **2** | **3层** | **有** | **当前主力** |
| **CoWoS Gen 6** | **2027** | **9.5x光罩** | **8 HBM4** | **双N3 Chiplet** | **4层+** | **有** | **2027目标** |

**光罩拼接技术**：
- 单片光罩面积 ~858mm²（26mm × 33mm）
- 5.5x光罩 = ~4700mm²中介层
- 拼接精度要求：亚微米级对准（~0.5μm overlay accuracy）

---

## Intel EMIB / EMIB-T / Foveros

### EMIB（Embedded Multi-die Interconnect Bridge）

**结构**：
```
┌─────────────────────────────────────┐
│  Die A    │ Bridge │    Die B       │  ← 计算Die
│  (CPU)    │(Silicon│   (GPU)        │
├───────────┴────────┴────────────────┤
│  有机基板（Organic Substrate）         │
│  └── EMIB桥嵌入基板腔体内            │
└─────────────────────────────────────┘
```

- **2017年量产**：Sapphire Rapids Xeon、Ponte Vecchio GPU
- 在有机基板腔体内嵌入小硅桥Die
- **跳过TSV**——桥Die简单廉价（面积小，良率高）
- 功率必须通过有机基板绕桥传输（长路径、高电阻）

### EMIB-T（2026投产）—— Intel的翻身之作

关键改进（加入TSV）：
```
┌─────────────────────────────────────┐
│  Die A    │ Bridge │    Die B       │
├───────────┴─TSV────┴────────────────┤  ← TSV穿透桥Die
│  有机基板                            │
│  └── 桥Die含TSV：垂直功率传输        │
└─────────────────────────────────────┘
```

- **加入TSV**：桥Die支持垂直功率传输（解决EMIB功率绕路问题）
- 集成MIM电容（噪声抑制）+ 铜接地网格（信号隔离）
- **45μm凸点间距**，路线图→35μm→25μm
- 能效：**~0.25 pJ/bit**
- UCIe-A：**32 Gb/s/pin或更高**
- 支持HBM3→HBM3E→**HBM4→HBM5**
- 封装尺寸可达**120mm×180mm**（38+桥接、12+光罩级Die）

**Intel vs TSMC 封装尺寸对标**

| 年份 | Intel EMIB-T | TSMC CoWoS-L/Gen6 |
|------|-------------|-------------------|
| 2026 | **8x光罩** | 5.5x光罩 |
| 2027 | 12x光罩 | **9.5x光罩** |
| 2028 | **12x+光罩** | — |

**成本优势**：
- EMIB封装：**低数百美元/芯片**
- CoWoS（Rubin级）：**$900-1,000/芯片**
- 桥Die晶圆利用率：Intel **~90%** vs TSMC **~60%**

**概念封装（Intel 2025.12发布）**：
- 16个计算元素跨8个基Die
- **24个HBM5堆叠**
- **10,296 mm²硅面积**
- **12x光罩尺寸**

### Foveros（3D堆叠）

**有源芯片垂直堆叠**（active-on-active）：
- Lakefield处理器首次商用
- 混合键合（Hybrid Bonding）连接上下Die
- 与EMIB组合为**Co-EMIB**：灵活异构架构

---

## 混合键合（Hybrid Bonding）深度版

**下一代互连技术**，替代微凸点（Micro-bump）：

### 物理原理

传统微凸点 vs 混合键合：

| 属性 | 微凸点（C4/μbump） | 混合键合（HCB） |
|------|---------------------|-----------------|
| 连接方式 | 焊球熔化焊接 | Cu-Cu直接键合 + SiO₂-SiO₂熔融 |
| 凸点间距 | 150μm → 55μm → 40μm | **<10μm**（可达亚微米） |
| 电容 | 较高（焊球体积大） | **极低**（Cu盘面积小） |
| 信号速率 | ~2-4 Gb/s/pin | **>10 Gb/s/pin** |
| 功耗 | ~0.5-1.0 pJ/bit | **~0.1 pJ/bit** |
| 散热 | 焊球热阻较高 | Cu直接导热，热阻低 |

### 混合键合工艺流程

```
[1] 晶圆制备
    ├─→ 顶部Die：Cu pad + SiO₂ passivation
    └─→ 底部Die：Cu pad + SiO₂ passivation

[2] 表面活化（Surface Activation）
    ├─→ Ar/N₂等离子体清洗
    └─→ 去除表面氧化层，暴露洁净Cu和SiO₂

[3] 室温预键合（Room Temp Pre-bonding）
    ├─→ 两晶圆对准（精度 <0.5μm）
    └─→ 施加轻压，SiO₂-SiO₂ van der Waals键合

[4] 退火强化（Annealing）
    ├─→ 300-400°C，N₂氛围
    ├─→ Cu原子互扩散 → Cu-Cu晶粒生长
    └─→ SiO₂-SiO₂熔融 → 共价键合

[5] 晶圆减薄（Grinding）
    └─→ 顶部晶圆磨薄至目标厚度（通常 <50μm）

[6] TSV/布线（可选）
    └─→ 若需垂直互联，继续TSV工艺
```

**TSMC SoIC**：
- sub-10μm pitch混合键合
- 已实现量产（AMD 3D V-Cache使用SoIC）

**Intel Foveros Direct**：
- sub-10μm pitch
- 3D Foveros堆叠的核心互连技术

---

## 玻璃基板（Glass Substrate）

- **Intel和TSMC 2026-2028路线图**
- **优势**：
  - 更低信号损耗（vs有机基板，介电常数更低）
  - 更高布线密度（玻璃通孔TGV，~10μm直径）
  - 热膨胀系数匹配硅（CTE ~3.5 ppm/K，接近Si的2.6 ppm/K）
- **IEEE研究**：高频互连通道中玻璃封装在信号/电源完整性上优于硅中介层
- **量产时间**：Intel目标3年内商业化就绪

---

## 供应链瓶颈

1. **CoWoS产能**：TSMC交期6-9个月，2027年前难缓解
2. **HBM供应**：SK海力士2026全年产能H1售罄
3. **ABF基板**：味之素积层膜（ABF）短缺，新工厂2-3年投产
4. **KGD测试**：UCIe链路已知良片测试仍不成熟，Chiplet级良率损失在封装级乘法放大

---

## 地缘风险

- **100%领先CoWoS产能集中在台湾**
- 台湾冲突情景：立即中断80%+先进封装产能
- Intel+Samsung两年内无法吸收该需求
- 美国CHIPS法案、欧盟Chips法案：2027-2028才有意义产能
- 中国受限：ASML/Applied Materials出口管制，限制先进封装设备

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 先进封装市场(2026E) | **$49-55B** | PatSnap行业分析 |
| 2.5D/3D封装CAGR | **10.1%** | 最快子赛道 |
| HBM市场(2027E) | **$33B** | Morgan Stanley |
| TSMC CoWoS投资 | **$2.8B(2021) + $3B(2026)** | TSMC官方 |
| OSAT CapEx增长 | **+27% YoY** | 2020年$6B |
| Intel EMIB成本 | **低数百美元/芯片** | Bernstein |
| CoWoS成本(Rubin级) | **$900-1,000/芯片** | Investing.com |
| 混合键合间距 | **<10μm**（SoIC/Foveros Direct） | TSMC/Intel官方 |
| 混合键合功耗 | **~0.1 pJ/bit** | 论文估算 |
| 玻璃基板CTE | **3.5 ppm/K**（接近Si 2.6） | Corning/Intel |

---

## 🔗 相关页面
- [concepts/chiplet.md](chiplet.md) — Chiplet设计范式
- [concepts/hbm.md](hbm.md) — HBM（先进封装的核心客户）
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA CoWoS依赖
- [entities/intel.md](../entities/intel.md) — Intel EMIB/Foveros
- [entities/tsmc.md](../entities/tsmc.md) — TSMC CoWoS产能

---

*最后更新：2026-05-12*  
*信息来源：PatSnap Eureka, Tom's Hardware, The Register, Intel/TSMC官方, Bernstein, IEEE封装论文, ChipStrat分析*