# HBM（高带宽内存）

**类型**：内存技术 / AI芯片关键组件  
**全称**：High Bandwidth Memory  
**核心作用**：解决AI推理的"内存带宽瓶颈"  
> **本文档为深度技术版。覆盖TSV制造工艺、3D堆叠物理结构、封装技术细节、电气特性与产业演进。**

---

## 一、为什么AI需要HBM：内存带宽瓶颈

AI推理是**内存带宽受限**，而非算力受限。

### 量化分析

Transformer模型每次推理需要加载全部权重到GPU寄存器：
- **GPT-4级别模型**：权重约1.8TB，每次forward pass需读取全部权重
- **关键公式**：推理吞吐量 ∝ 内存带宽 / 模型权重大小
- 算力再强（TFLOPS再高），如果内存带宽不够，GPU就在"等数据"——利用率常低于**30%**

| 对比项 | DDR5 | GDDR6X | HBM3E |
|--------|------|--------|-------|
| 单通道带宽 | ~51 GB/s | ~100 GB/s | **~1.2 TB/s** |
| 与GPU距离 | PCB走线（cm级） | PCB走线 | 硅中介层（μm级） |
| 功耗效率 | 低 | 中 | **高**（近距+宽总线） |
| 容量/封装 | 大/标准DIMM | 中/标准BGA | 小/2.5D封装 |

> 来源：NVIDIA H100白皮书、JEDEC HBM3标准、MLPerf推理基准

---

## 二、HBM物理结构：3D堆叠 + TSV + 中介层

### 2.1 整体封装架构

```
┌─────────────────────────────────────────────────┐
│                  散热盖 / 导热材料                 │
├─────────────────────────────────────────────────┤
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐               │
│  │HBM4 │ │HBM4 │ │HBM4 │ │HBM4 │  ← 4-8颗HBM  │
│  │堆叠  │ │堆叠  │ │堆叠  │ │堆叠  │               │
│  └─────┘ └─────┘ └─────┘ └─────┘               │
│       ↓ TSV ↓ TSV ↓ TSV ↓ TSV                   │
│  ┌─────────────────────────────────────────┐     │
│  │           硅中介层 (Silicon Interposer)   │     │
│  │     微米级布线，连接HBM与GPU             │     │
│  │     RDL重布线层 + TSV垂直通孔            │     │
│  └─────────────────────────────────────────┘     │
│       ↓ μbump ↓ μbump ↓ μbump ↓ μbump          │
│  ┌─────────────────────────────────────────┐     │
│  │              GPU/ASIC 逻辑Die             │     │
│  │        (如NVIDIA H100的GH100芯片)         │     │
│  └─────────────────────────────────────────┘     │
│       ↓ C4 bump ↓ C4 bump                        │
│  ┌─────────────────────────────────────────┐     │
│  │            有机基板 (Organic Substrate)   │     │
│  │         PCB级走线 → 主板连接器             │     │
│  └─────────────────────────────────────────┘     │
└─────────────────────────────────────────────────┘
```

### 2.2 TSV：3D堆叠的核心

TSV（Through-Silicon Via，硅通孔）是HBM的**定义性技术**——没有TSV就没有3D堆叠。

#### TSV关键参数

| 参数 | HBM3 | HBM4 | 说明 |
|------|------|------|------|
| **TSV直径** | ~5-10 μm | ~5-8 μm | 越小越难刻蚀 |
| **TSV间距(pitch)** | 40-55 μm | 30-40 μm | 决定布线密度 |
| **TSV深宽比** | 10:1 ~ 15:1 | 15:1 ~ 20:1 | 越深越难填充 |
| **每堆叠TSV数** | >5,000 | >10,000 | 含冗余 |
| **TSV电阻** | 50-200 mΩ | 30-150 mΩ | 影响信号完整性 |
| **TSV电容** | 20-50 fF | 15-40 fF | 影响RC延迟 |
| **TSV占面积** | ~1% | ~0.5% | 越小越好 |

#### TSV完整制造流程

TSV制造是HBM生产的**最大瓶颈**，良率直接影响HBM成本。

**Step 1：光刻定义**
- 涂布光刻胶 → 光刻图案化（定义TSV位置）
- TSV密度：每mm²数百个通孔

**Step 2：DRIE Bosch刻蚀**（最关键步骤）
```
Bosch工艺 = 刻蚀-钝化循环：

刻蚀阶段：SF₆等离子体 → 各向同性刻蚀Si
         ↓
钝化阶段：C₄F₈等离子体 → 沉积氟碳聚合物保护层
         ↓
重复循环数百次 → 形成高深宽比垂直孔

关键挑战：
• 深孔底部反应物排出困难 → 刻蚀速率下降（ARDE效应）
• 侧壁粗糙度（scalloping）→ 后续薄膜覆盖不均
• 孔底剖面控制 → 影响填充质量
```

| 参数 | 典型值 | 挑战 |
|------|--------|------|
| 刻蚀气体 | SF₆ + C₄F₈ | 副产物排出 |
| 孔径 | 5-10 μm | 侧壁粗糙度 |
| 深度 | 50-100 μm | ARDE（深宽比依赖刻蚀）|
| 深宽比 | 10:1 ~ 20:1 | 孔底平坦化 |

**Step 3：绝缘层沉积**
- 材料：SiO₂（热氧化或PECVD）
- 厚度：1-2 μm
- 作用：隔离TSV铜与硅基底，防止漏电
- 挑战：高深宽比孔内**阶梯覆盖**——孔底薄膜厚度仅为顶部的30-50%

**Step 4：阻挡层 + 种子层**
- 阻挡层：TiN / TaN（5-20nm，PVD或ALD）
  - 防止Cu扩散到Si中（Cu是Si中的快扩散杂质）
- 种子层：Cu（PVD溅射，~100-200nm）
  - 为电镀提供导电基底
- 挑战：高深宽比孔的**PVD覆盖均匀性**

**Step 5：铜电镀填充（ECD）**
```
电镀方式：
├─ 均匀电镀（Conformal）：侧壁+底部同时沉积
│   → 适合大孔径、低深宽比
│   → 风险：孔口封闭前底部未填满 → 空洞(void)
│
└─ 底部向上电镀（Bottom-up）：底部优先沉积
    → 添加剂（加速剂/抑制剂/整平剂）控制生长
    → 适合小孔径、高深宽比
    → 最优选择，但化学控制极难
```

- 电镀后**过填充**（Overburden）：TSV顶部铜凸起

**Step 6：CMP（化学机械抛光）**
- 磨除过填充铜 + 阻挡层 + 多余绝缘层
- 目标：表面平整如镜，暴露TSV顶部
- 后续：标准BEOL（后段金属化）工艺继续

**Step 7：背面暴露（Backside Reveal）**（仅Via-Last TSV）
```
流程：
1. 临时键合：Device wafer → 载体wafer（粘合剂）
2. 背面研磨：粗磨 → 中磨 → 精磨 → 接近TSV底部
3. CMP抛光：镜面表面
4. 干法刻蚀暴露TSV：等离子体精确去除剩余Si
5. 沉积Si₃N₄止蚀层 → SiO₂ → CMP回蚀暴露TSV
6. 背面RDL（重布线层）+ μbump
```

**TSV暴露是最脆弱的步骤之一**：研磨深度控制精度需达到微米级，过深损伤TSV，过浅暴露不完全。

---

### 2.3 HBM堆叠结构

```
┌─────────────────────────┐ ← 最顶层DRAM Die
│    DRAM Die N (第N层)   │
│  ┌─────────────────┐    │
│  │ 存储阵列         │    │
│  │ (Bank/Row/Col)  │    │
│  └─────────────────┘    │
│  ↓ TSV贯穿              │
├─────────────────────────┤
│    DRAM Die N-1         │
│  ┌─────────────────┐    │
│  │ 存储阵列         │    │
│  └─────────────────┘    │
│  ↓ TSV贯穿              │
├─────────────────────────┤
│         ...             │  ← 重复N-2次
├─────────────────────────┤
│    DRAM Die 1 (第1层)   │
│  ┌─────────────────┐    │
│  │ 存储阵列         │    │
│  └─────────────────┘    │
│  ↓ TSV贯穿              │
├─────────────────────────┤
│    **Base Die**          │  ← 不是DRAM！
│  ┌─────────────────┐    │
│  │ PHY (物理层)     │    │
│  │ • SerDes串并转换 │    │
│  │ • 时钟分配       │    │
│  │ • 信号调理       │    │
│  ├─────────────────┤    │
│  │  Repair Logic    │    │
│  │ • 冗余行/列管理   │    │
│  ├─────────────────┤    │
│  │ BIST (内建自测试)│    │
│  ├─────────────────┤    │
│  │ Mode Registers   │    │
│  │ • 时序参数配置   │    │
│  └─────────────────┘    │
│  ↓ μbump到中介层        │
└─────────────────────────┘
```

**关键设计决策**：
- Base Die用**逻辑工艺**（28nm-12nm），不用DRAM工艺
  - 原因：DRAM工艺优化存储单元密度，逻辑速度/IO差；Base Die需要高速PHY和复杂逻辑
- TSV**贯穿所有DRAM层**，在Base Die终止
- 每层DRAM Die的厚度：~30-50 μm（研磨减薄后）

### 2.4 堆叠键合技术演进

| 技术 | 温度 | 压力 | 适用层数 | 精度 | 状态 |
|------|------|------|---------|------|------|
| **热压缩键合(TCB)** | 250-300°C | 高压 | ≤12层 | ±1-2 μm | HBM3/HBM3E主流 |
| **热压+非导电胶(TCNCP)** | 250°C | 中压 | ≤16层 | ±1 μm | 过渡方案 |
| **混合铜键合(HCB)** | **室温** | 无 | **≥16层** | **±0.5 μm** | HBM4主流 |
| **晶圆级键合** | 室温 | 无 | 无上限 | ±0.2 μm | 研发中 |

**HCB（Hybrid Copper Bonding）技术细节**：
- 原理：两片wafer的Cu焊盘直接面对面键合，无需中间材料
- 工艺：
  1. 表面CMP抛光至原子级平整（Ra < 0.5nm）
  2. 等离子体激活表面
  3. 对准精度：亚微米级
  4. 室温键合 → Cu-Cu扩散形成金属键合
- 优势：
  - 无填充材料 → 热阻降低20%+
  - 间距可缩至**10 μm以下**
  - 支持20+层堆叠
- 挑战：表面平整度要求极高，任何颗粒/缺陷都导致键合失败

---

### 2.5 硅中介层（Silicon Interposer）

**作用**：在HBM堆叠和GPU之间提供高密度布线层。

```
硅中介层结构：
┌─────────────────────────────┐
│     μbump层（连接HBM/GPU）   │  ← 顶部凸点阵列
├─────────────────────────────┤
│     金属层 N（最细）         │  ← 线宽/间距 ~0.8 μm
│     金属层 N-1              │
│         ...                 │  ← 共4-6层金属
│     金属层 1（最粗，供电）   │
├─────────────────────────────┤
│     TSV（贯穿中介层）        │  ← 连接上下表面
├─────────────────────────────┤
│     C4 bump（连接基板）      │  ← 底部焊球阵列
└─────────────────────────────┘
```

**关键参数**：
- 中介层面积：可达reticle尺寸（~800mm²）或更大（TSMC CoWoS-L支持多reticle拼接）
- 金属层线宽：~0.8-2 μm（比芯片内金属粗得多，但比PCB细两个数量级）
- 中介层厚度：~100 μm
- TSV直径：~10 μm（比HBM TSV大，但深宽比更低）

---

## 三、HBM电气接口：JEDEC标准

### 3.1 接口架构

HBM采用**宽总线、低速率**策略，与GDDR的窄总线、高速率形成对比：

| 参数 | GDDR6X | HBM3E | HBM4 |
|------|--------|-------|------|
| 数据总线宽度 | 32-bit × 1 | 1024-bit × 1 | **2048-bit** |
| 每pin数据率 | 19-24 Gbps | 9.6 Gbps | 11.7+ Gbps |
| 等效总带宽 | ~1 TB/s | ~1.2 TB/s | ~2.4 TB/s |
| 信号完整性 | 挑战极大 | 较易 | 较易 |
| 功耗 | 高 | 较低 | 更低 |

**HBM3E引脚组织**：
- 1024-bit数据总线 = 16个**独立通道**（每通道64-bit）
- 每通道独立时序控制 → 可部分关闭未用通道省电
- 每个通道有独立的Command/Address总线

### 3.2 信号类型

| 信号组 | 数量 | 作用 |
|--------|------|------|
| **DQ** | 1024 (HBM3) / 2048 (HBM4) | 数据 |
| **DBI** | 按字节 | 数据总线翻转（降低功耗） |
| **DMI** | 按字节 | 数据掩码/数据总线翻转 |
| **CA** | 每通道独立 | Command/Address |
| **CK/CK#** | 差分时钟 | 全局时钟分配 |
| **CKE** | 每通道 | 时钟使能 |
| **RAS/CAS/WE** | 隐含在CA中 | 行/列地址选通、写使能 |

### 3.3 关键时序参数

| 参数 | HBM3 | HBM3E | HBM4 | 说明 |
|------|------|-------|------|------|
| tCK (时钟周期) | ~1.04 ns | ~1.04 ns | ~0.85 ns | 频率倒数 |
| CL (CAS延迟) | 32 | 32 | 待定 | 列选通到数据 |
| tRCD (行到列延迟) | 32 ns | 32 ns | 待定 | ACT到READ/WRITE |
| tRAS (行激活时间) | 33 ns | 33 ns | 待定 | 行保持激活 |
| tREFI (刷新间隔) | 1.95 μs | 1.95 μs | 待定 | 每行刷新间隔 |

---

## 四、技术演进时间线

| 代际 | 时间 | 堆叠 | 带宽/堆叠 | 单颗容量 | 制程 | 关键应用 |
|------|------|------|----------|----------|------|----------|
| **HBM1** | 2015 | 4层 | 128 GB/s | 1 GB | 2x nm | AMD Fiji |
| **HBM2** | 2016 | 4/8层 | 307 GB/s | 4-8 GB | 2x nm | NVIDIA V100 |
| **HBM2E** | 2020 | 8层 | 460 GB/s | 16 GB | 1x nm | NVIDIA A100 |
| **HBM3** | 2022 | 12层 | 819 GB/s | 24 GB | 1x nm | NVIDIA H100 |
| **HBM3E** | 2024 | 12层 | 1.2 TB/s | 36 GB | 1β nm | H200/B200 |
| **HBM4** | **2026量产** | **16层** | **2.0 TB/s+** | **24-36 GB** | 1c nm | Rubin/MI400 |
| **HBM4E** | 2026H2样品 | 16层 | 2.4 TB/s+ | 48 GB | 1c nm | 下一代 |
| **HBM5** | 2028+ | 20+层 | 3+ TB/s | 64 GB+ | 1c/2nm | Feynman |

**制程说明**：
- 1x nm = 10-19nm级DRAM工艺（如1y, 1z）
- 1α nm = 第四代10nm级
- 1β nm = 第五代10nm级
- 1c nm = 第六代10nm级（~12nm等效）
- DRAM工艺命名与逻辑工艺（3nm, 5nm）不同，数字不直接可比

---

## 五、2026年HBM4量产动态

### 5.1 Samsung — 率先宣布量产
- **2026年2月**：宣布HBM4量产出货（首批发货）
- 速度：**11.7 Gbps**（可超频至13 Gbps）
- 单堆叠带宽：最高**3.3 TB/s**
- 容量：24-36 GB（计划扩展至48 GB）
- **技术亮点**：HCB混合铜键合、散热改善+30%、能效提升+40%
- **HBM4E样品**：2026H2出货，16Gbps/pin
- **销售预测**：2026年HBM销售额较2025年增长**3倍以上**
- **来源**：Samsung官方 / The Register, 2026-02-13

### 5.2 Micron — 提前一个季度交付
- **2026年2月**：CFO Mark Murphy宣布HBM4已进入高量产
- 速度：**>11 Gbps**
- **全年产能已预售完毕**
- HBM良率"on track"
- **股价反应**：消息发布后上涨近**10%**
- **新客户**：Tesla Dojo超级计算机
- **来源**：Wolfe Research活动 / The Register

### 5.3 SK海力士 — 市场领导者
- **2025Q2 HBM份额62%**
- **2026全年产能H1 2025即售罄**
- 与Samsung共同供应NVIDIA VeraRubin HBM4
- **尚未宣布HBM4量产**——可能优先保障大客户（NVIDIA）供应而非PR
- **来源**：PatSnap分析 / 供应链

### 5.4 新需求方：Tesla Dojo
- Tesla成为HBM4新客户
- 同时向SK海力士和Samsung索取样品
- 用于Dojo超级计算机
- **信号**：HBM需求从NVIDIA/AMD轴心扩大
- **来源**：The Register

---

## 六、产业竞争格局

| 厂商 | 2025Q3份额 | 技术路线 | 关键客户 | 产能状态 |
|------|-----------|----------|----------|----------|
| **SK海力士** | **53%** | 1α→1β→1c DRAM | NVIDIA、AMD、Google | 2026全年H1售罄 |
| **三星** | **35%** | HCB技术领先、HBM4E 16Gbps | NVIDIA(VeraRubin)、Tesla | HBM4已出货 |
| **Micron** | **12%** | HBM4提前量产、全年预售完毕 | Tesla、云厂商 | 产能紧张 |

**关键趋势**：
- **产能紧张**：三大厂将产能转向高利润HBM，普通DRAM价格上涨
- **技术竞赛**：从"谁先量产"转向"HCB良率"和"散热方案"
- **需求扩大**：从AI训练卡扩展到推理卡、Dojo、云厂商定制

---

## 七、前沿技术方向

### 7.1 混合铜键合（HCB）
- **三星率先采用**，支持16层以上堆叠
- 散热降低20%+，间距可缩至10 μm以下
- 表面平整度要求：Ra < 0.5 nm（原子级）
- 为HBM5（20+层）铺路

### 7.2 定制化HBM（cHBM）
- **SK海力士**：将轻量级计算单元集成到Base Die
- 功能：累加器、激活函数、数据预处理
- 目标：推理效率提升2-5×（减少HBM→GPU数据搬运）
- 信号：从"纯性能竞争"转向"推理效率+TCO优化"

### 7.3 面板级封装（PLP）
- 从晶圆级（300mm/450mm）转向面板级（600mm×600mm或更大）
- **优势**：面积利用率更高、适合大面积中介层
- **挑战**：面板平整度控制、热膨胀系数匹配
- Applied Materials收购ASMPT NEXX即为此布局

### 7.4 CXL内存扩展
- HBM容量受限（单GPU最多8颗 = 192-576GB）
- CXL.mem协议允许GPU通过PCIe访问远端DRAM
- 延迟惩罚：~100-200 ns（vs HBM ~10 ns）
- 适用场景：大模型推理权重卸载、KV Cache扩展

---

## 八、关键公式与数据

| 指标 | 数值 | 来源 |
|------|------|------|
| 推理吞吐量公式 | ∝ 内存带宽 / 模型权重大小 | NVIDIA/MLSys共识 |
| HBM3 TSV数量 | >5,000/堆叠 | JEDEC规范 |
| HBM4 TSV深宽比 | 15:1 ~ 20:1 | SemiEngineering |
| TSV电阻 | 30-200 mΩ | 工艺实测 |
| TSV电容 | 15-50 fF | 工艺实测 |
| DRIE刻蚀速率 | ~5-10 μm/min | Bosch工艺典型值 |
| Cu电镀填充速率 | ~0.5-2 μm/min | ECD工艺 |
| HCB对准精度 | ±0.5 μm | 混合键合要求 |
| HBM市场规模(2027E) | **$330亿** | Morgan Stanley |
| VeraRubin总HBM容量 | 576 GB | NVIDIA GTC 2026 |
| AMD MI450 HBM容量 | 432 GB | AMD官方 |
| HBM4 Samsung速度 | 11.7 Gbps | Samsung官方 |
| HBM4 Micron速度 | >11 Gbps | Micron CFO |

---

## 九、TSV制造瓶颈分析

### 为什么TSV是HBM产能瓶颈？

| 步骤 | 瓶颈原因 | 缓解方向 |
|------|---------|---------|
| **DRIE刻蚀** | 高深宽比孔底部副产物排出困难 | 优化气体配比、脉冲刻蚀 |
| **绝缘层沉积** | 阶梯覆盖差，孔底薄膜薄 | ALD替代PECVD、多步沉积 |
| **阻挡层沉积** | PVD高深宽比覆盖差 | ALD原子层沉积 |
| **Cu电镀** | 孔口先封闭→空洞(void) | 底部向上电镀、添加剂优化 |
| **CMP** | 全局平整度控制 | 终点检测、选择性抛光 |
| **背面暴露** | 研磨深度精度（μm级） | 在线厚度监测、智能研磨 |
| **热应力** | Cu/Si热膨胀系数差(17×) | 退火工艺优化、保持区设计 |

**TSV热应力**：Cu的热膨胀系数(~17 ppm/°C)是Si(~2.6 ppm/°C)的**6.5倍**。温度循环时：
- Cu膨胀/收缩比Si多 → 界面剪切应力
- 影响：
  1. 附近晶体管性能偏移（Keep-out Zone，通常5-10 μm范围内电路受影响）
  2. 长期可靠性：界面分层、空洞形成
  3. 翘曲：整片wafer变形

---

## 十、相关实体与引用

### 相关实体
- [entities/sk-hynix.md](../entities/sk-hynix.md) — SK海力士
- [entities/samsung.md](../entities/samsung.md) — 三星
- [entities/nvidia.md](../entities/nvidia.md) — NVIDIA
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体
- [concepts/chiplet.md](chiplet.md) — Chiplet封装
- [concepts/advanced-packaging.md](advanced-packaging.md) — 先进封装

### 引用来源
- [TSV Complexity Leads to Manufacturing Bottleneck](https://semiengineering.com/tsv-complexity-leads-to-manufacturing-bottleneck/) — SemiEngineering, 2026-04-22
- [AI Memory Crisis: HBM3E/HBM4 Deep Analysis](https://www.enostech.com/the-ai-memory-crisis-a-deep-technical-analysis-of-hbm3e-hbm4-dram-process-technology-and-the-bandwidth-wall-constraining-ai/) — EnoSTech, 2026-02-25
- [Through-Silicon Via (TSV) Manufacturing](https://anysilicon.com/semipedia/through-silicon-via-tsv/) — AnySilicon, 2025-12
- [TSV Process: TU Delft](https://pure.tudelft.nl/ws/portalfiles/portal/73507610/Through_Package_Via_A_bottom_up_approach_Hengqian_Yi.pdf) — 学术论文
- [Hybrid Bonding Process Flow](https://semianalysis.com/2024/02/09/hybrid-bonding-process-flow-advanced/) — SemiAnalysis, 2024-02
- [Reliability of TSV Under Thermal Cycling](https://aaltodoc.aalto.fi/server/api/core/bitstreams/8c7673c9-c9a5-4b88-8d54-9a46a8c8fe19/content) — Aalto University
- [JEDEC HBM3 Standard](https://www.jedec.org/) — JEDEC官方
- [Samsung HBM4 Announcement](https://www.theregister.com/2026/02/13/samsung_hbm4_mass_production/) — The Register, 2026-02-13
- [Micron HBM4 Mass Production](https://www.theregister.com/2026/02/13/micron_hbm4_mass_production/) — The Register, 2026-02-13
- [PatSnap HBM Analysis](https://www.patsnap.com/) — PatSnap Eureka, 2026
- [NVIDIA VeraRubin HBM Details](https://www.nvidia.com/) — NVIDIA GTC 2026

*最后更新：2026-05-12*  
*本文档从概括版拓展到TSV制造工艺细节、物理结构、电气特性与产业动态。*
