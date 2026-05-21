# 存算一体 / Processing-in-Memory (PIM)

> 类型：硬件架构 | 别名：近存运算、Compute-in-Memory | 最后更新：2026-05-12
> **本文档为深度技术版。技术细节覆盖电路级实现、物理机制、学术原型与产业瓶颈。**

---

## 一、冯·诺依曼瓶颈：为什么需要PIM

在传统冯·诺依曼架构中，CPU与DRAM物理分离，数据通过总线搬运。

### 量化代价

| 指标 | 数值 | 来源 |
|------|------|------|
| 数据移动占系统能耗 | **60%+** | Horowitz et al., IEEE ISSCC 2014 |
| 虚拟内存页管理开销 | **50%执行时间** | 内存子系统研究共识 |
| AI推理带宽瓶颈 | 算力利用率常低于**30%** | MLPerf/MLSys社区 |

**核心矛盾**：算力增长遵循摩尔定律（~2×/2年），但内存带宽增长慢得多（~1.4×/2年）。当带宽成为瓶颈，再强的算力也只能"等数据"。

---

## 二、三大子方向：从远到近

| 方向 | 英文 | 计算位置 | 数据移动距离 | 成熟度 | 代表 |
|------|------|---------|-------------|--------|------|
| **近存处理** | Near-Memory Processing (NMP) | 逻辑层紧邻DRAM/HBM | 微米级 | **产品化** | NVIDIA、SK海力士、UPMEM |
| **存内计算** | Compute-in-Memory (CIM) | 在内存位单元内执行运算 | **零**（原位） | 实验室→原型 | 清华、Stanford、ETH Zurich |
| **存内逻辑** | Logic-in-Memory (LIM) | 存储单元内嵌入布尔逻辑 | 零 | 早期研究 | 高校为主 |

**关键区分**：NMP把计算单元放在内存控制器/基板旁边（如HBM的Base Die加计算逻辑），数据仍需移动但距离极短；CIM直接在存储单元内部利用物理特性执行运算，数据**不需要离开存储阵列**。

---

## 三、集群1：基于DRAM的Processing-Using-Memory (PuM)

**核心洞察**：标准DRAM的读操作本身就是一次模拟计算——电荷共享（Charge Sharing）。

### 3.1 DRAM读操作即计算

DRAM单元结构：
- **存储电容**：存储电荷代表1（VDD）或0（0V）
- **访问晶体管**：由字线（Wordline）控制，连接电容到位线（Bitline）
- **位线预充电**：读操作前，位线预充到VDD/2

当字线使能（ACTIVATE命令），存储电容与位线电容并联，电荷重新分配：

> **V_bitline = (C_cell × V_cell + C_bitline × VDD/2) / (C_cell + C_bitline)**

若V_cell = VDD（存储1），V_bitline 会被拉高到 VDD/2 + δ
若V_cell = 0（存储0），V_bitline 会被拉低到 VDD/2 - δ

感测放大器（Sense Amplifier）检测δ并放大到全摆幅——**这一整个过程就是一次模拟比较**。

### 3.2 Triple-Row Activation：多数表决门

ETH Zurich的Ambit（MICRO 2017）发现：**同时激活三个DRAM行**，可以在位线上实现**多数表决（Majority, MAJ）**：

- 三个存储电容同时与位线共享电荷
- 位线电压 = 三个电容电压的**平均值**
- 若≥2个电容为VDD（1），位线电压 > VDD/2 → 感测为1
- 若≥2个电容为0V，位线电压 < VDD/2 → 感测为0

**MAJ(A,B,C) = AB + AC + BC**（布尔代数）

用MAJ + NOT（通过感测放大器的互补输出）可以合成**任意布尔函数**：
- AND = MAJ(A, B, 0)
- OR = MAJ(A, B, 1)
- NOT = 感测放大器的互补输出

### 3.3 SIMDRAM：端到端的位串行SIMD框架

ETH Zurich的SIMDRAM（ASPLOS 2021）将上述机制工程化为完整框架：

**三层架构**：

```
┌─────────────────────────────────────────┐
│  Layer 3: SIMDRAM Control Unit          │
│  （内存控制器内，解析bbop指令→μProgram）   │
├─────────────────────────────────────────┤
│  Layer 2: μProgram Generator             │
│  （将任意操作编译为ACT/PRE命令序列）        │
├─────────────────────────────────────────┤
│  Layer 1: DRAM Subarray                  │
│  （标准DRAM芯片，仅需时序参数微调）        │
└─────────────────────────────────────────┘
```

**μProgram 示例**：N-bit加法
1. 为操作数分配DRAM行
2. 生成ACT/PRE序列执行MAJ/NOT操作
3. 按位串行（bit-serial）方式逐位计算

**性能基准**：
- RowClone（行复制）：**14.6×** 加速 vs CPU memcpy
- 批量初始化：**12.6×** 加速
- 复杂操作（乘法/除法）：需多个μProgram步骤，但受益于DRAM内部带宽

**关键局限**：
- 每个位线一次只能做一个操作 → 并行度限于跨位线（A维度），无法跨字线（B维度）
- 多位运算需串行多轮 → 吞吐量低于SRAM/ReRAM-CIM
- **破坏性操作**：计算会覆盖原始数据，需提前复制

### 3.4 PiDRAM：真实DRAM芯片验证框架

ETH Zurich的PiDRAM（2022）是首个在**未修改商用DRAM芯片**上验证PuM的框架：

**核心发现**：
- 商用DRAM的时序参数（tRCD、tRAS、tRP）存在**安全裕度**
- 适当缩短时序间隔仍可正确执行操作
- RowClone在真实DDR4芯片上验证成功

**技术意义**：PuM不需要定制DRAM芯片，利用现有硬件即可实现——**零额外硬件成本**。

---

## 四、集群2：SRAM-based Compute-in-Memory（边缘AI主流）

SRAM的访问速度比DRAM快一个数量级，且不需要刷新，是边缘AI推理的首选PIM基底。

### 4.1 为什么6T SRAM不够

标准6T SRAM单元：
- 两个交叉耦合反相器存储1bit
- 读操作通过位线（BL/BLB）进行

**问题**：同时激活多行读时，多个单元同时驱动同一条位线 → **读干扰（Read Disturbance）**，可能破坏存储值。

### 4.2 8T/9T/10T：读写分离结构

| 结构 | 额外晶体管 | 关键改进 | 面积代价 |
|------|-----------|---------|---------|
| **8T** | +2T（专用读端口） | 读写路径完全分离，可多行同时激活 | 中等（~1.3× 6T） |
| **9T** | +3T | 双读端口，支持CAM操作 | 较大 |
| **10T** | +4T | 更复杂逻辑（XNOR、点积） | 较大 |

**核心原理**：增加专用读字线（RWL）和读位线（RBL），与写字线/位线物理隔离 → 读操作不再干扰存储节点。

### 4.3 Analog CIM：电荷共享实现MAC

**典型电路**（基于2025年论文的8T SRAM IMC设计）：

```
写入路径: WL → BL/BLB → 6T存储单元
读取路径: RWL → RBL → 额外2T读端口

MAC操作:
1. 将操作数B的各位写入不同行的同一列
2. RBL预充电到VDD（如1.8V）
3. 同时激活对应RWL，操作数A的位作为RWL使能信号
4. RBL电压下降 ∝ 激活的SRAM单元数量
   → 电压降 = f(MAC count)
5. MAC Decoder（8个电压比较器）将模拟电压→数字MAC结果
```

**实测数据**（90nm CMOS工艺，1.8V）：
- 8-bit MAC + 逻辑运算
- 频率：142.85 MHz
- 延迟：**0.7 ns**
- 能耗：**56.56 fJ/bit/MAC**
- 吞吐量：15.8 M ops/s

### 4.4 Digital CIM：电流求和实现MAC

与电荷共享的模拟方案不同，Digital CIM在SRAM阵列内直接实现数字乘法：

**映射方式**：
- 权重W存储在SRAM阵列中（每行一个权重位）
- 输入IN同时施加到各列的位线
- 乘法通过位线电流/电压模式实现
- 累加通过感测放大器阵列或数字加法树完成

**两种主流拓扑**：

| 类型 | 机制 | 精度 | 能效 | 面积 |
|------|------|------|------|------|
| **Current-based ACIM** | 利用位线电流求和，欧姆定律乘法 | 中（受PVT影响） | 高 | 小 |
| **Charge-based ACIM** | MOM电容电荷再分配 | 高（MOM电容线性度好至12bit） | 高 | 略大 |
| **Digital CIM** | 纯数字AND+加法树 | 最高 | 中 | 大 |

**典型数字CIM性能**（65nm工艺，0.8V/1.2V双电压）：
- 8×72阵列，64-Bite点积
- 能效：**1.69 GOPS/W**
- 精度：平均偏差**1.05%**
- 3-bit ADC + 8-bit比较输出

### 4.5 SRAM-CIM的产业化瓶颈

| 瓶颈 | 具体表现 | 当前进展 |
|------|---------|---------|
| **阵列规模** | 演示多限于128Kb以下 | 128Kb-1Mb宏单元已 tape-out |
| **ADC overhead** | 模拟→数字转换消耗面积/功耗 | 多路复用ADC、精简参考列方案 |
| **PVT变异** | 工艺/电压/温度影响模拟精度 | 7nm FinFET已验证98.3% CNN精度 |
| **数据布局** | 矩阵权重需特殊排列（转置） | DualityCache等框架支持自动布局 |

---

## 五、集群3：阻变/非易失存储器CIM（学术前沿）

### 5.1 ReRAM Crossbar：欧姆定律的硬件实现

ReRAM（阻变存储器）Crossbar阵列是CIM最优雅的物理实现：

**物理结构**：
```
        Wordline 0 ──┬──┬──┬──┬──┐
                     │R₀₀│R₀₁│R₀₂│R₀₃│
        Wordline 1 ──┼──┼──┼──┼──┤
                     │R₁₀│R₁₁│R₁₂│R₁₃│
        Wordline 2 ──┼──┼──┼──┼──┤
                     │R₂₀│R₂₁│R₂₂│R₂₃│
        Wordline 3 ──┴──┴──┴──┴──┘
                      │  │  │  │
                   Bitline0 1  2  3
```

每个交叉点是一个ReRAM单元，电阻值可编程为R（高阻态=0）或R/α（低阻态=1），对应电导G = 1/R。

**运算原理**：
1. **输入向量x**作为电压{V₀, V₁, V₂, ...}施加到各行Wordline
2. **权重矩阵W**作为电导{Gᵢⱼ}编程到各ReRAM单元
3. **欧姆定律**：每个单元的电流 Iᵢⱼ = Vᵢ × Gᵢⱼ
4. **基尔霍夫电流定律**：每列Bitline的电流 Iⱼ = Σᵢ Iᵢⱼ = Σᵢ Vᵢ × Gᵢⱼ

> **Iⱼ = dot_product(x, W[:,j])** —— 整个矩阵-向量乘法在一个模拟步骤内完成

**延迟**：从O(n²)降到**O(1)**（信号建立时间决定实际延迟）

### 5.2 ReRAM单元物理机制

ReRAM器件结构：金属电极 / 金属氧化物层（如HfOₓ）/ 金属电极

**阻变机制**：
- **SET（低阻态=LRS=1）**：施加正电压 → 氧空位向阴极迁移 → 形成导电细丝 → 电阻骤降
- **RESET（高阻态=HRS=0）**：施加负电压 → 氧离子返回 → 导电细丝断裂 → 电阻恢复

**关键参数**：
- HRS/LRS电阻比：**1-3个数量级**（典型：10kΩ vs 100kΩ）
- 多电平状态：中间阻态支持模拟权重（非仅二进制）
- 非易失性：断电后保持阻态

### 5.3 外围电路：ADC/DAC开销

ReRAM Crossbar是纯模拟计算，需要混合信号接口：

```
数字输入向量 → DAC → Wordline电压
                    ↓
              ReRAM Crossbar（模拟MVM）
                    ↓
Bitline电流 → TIA（跨阻放大器）→ 电压 → ADC → 数字输出
```

**ADC是面积/功耗瓶颈**：高精度ADC面积可达Crossbar本身的30-50%。

### 5.4 PCM与STT-MRAM

| 技术 | 存储机制 | 优势 | 劣势 |
|------|---------|------|------|
| **PCM** | 相变材料（GST合金）晶态/非晶态电阻差 | 多级状态、成熟工艺 | 写入能耗高、耐久性有限 |
| **STT-MRAM** | 磁性隧道结自旋转移矩 | 无限耐久、高速 | 电阻比低、面积较大 |
| **FeFET** | 铁电栅极极化 | 3-terminal可单独访问 | 工艺成熟度低 |

---

## 六、集群4：3D堆叠与Chiplet封装

通过TSV（硅通孔）和2.5D中介层物理缩短逻辑与内存距离。

### 6.1 HBM本身就是3D PIM

HBM的堆叠结构：
```
┌─────────┐
│ DRAM层8 │  ← TSV垂直贯穿所有层
├─────────┤
│ DRAM层7 │
├─────────┤
│   ...   │
├─────────┤
│ DRAM层1 │
├─────────┤
│ Base Die│ ← 逻辑层（控制器、PHY）
└─────────┘
     ↓
  Interposer → GPU/CPU
```

- **TSV直径**：~10μm
- **TSV间距**：~40-50μm
- **每颗HBM有数千个TSV**提供垂直数据通道

### 6.2 cHBM：在Base Die上加计算

SK海力士CES 2026展示的cHBM（Custom HBM）：
- 将轻量级计算单元（如累加器、激活函数）集成到HBM的Base Die
- 利用HBM的宽总线（1024-bit × 4 = 4096-bit）实现高带宽近存计算
- 目标：推理效率提升**2-5×**（减少数据从HBM→GPU的搬运）

---

## 七、产业痛点与128Kb上限

### 7.1 为什么演示多限于128Kb以下？

| 瓶颈 | 128Kb以下 | 扩大规模时 |
|------|----------|-----------|
| **模拟非理想性** | 位线电阻/电容可忽略 | IR压降、寄生电容导致信号失真 |
| **PVT变异** | 单元间匹配性好 | 工艺角差异累积，计算精度下降 |
| **热管理** | 散热均匀 | 中心单元温度高，阻态漂移 |
| **布线复杂度** | ADC可每列一个 | ADC数量线性增长，面积爆炸 |
| **权重编程** | 逐单元调阻可行 | 大规模阵列调阻时间不可接受 |

### 7.2 软件-硬件协同设计缺口

- **缺少CIM编译器**：没有LLVM/MLIR级别的CIM后端
- **缺少模拟工具链**：SPICE级仿真只能处理小阵列（<1K单元）
- **算法-硬件映射不透明**：CNN层如何最优映射到CIM阵列仍是研究问题
- **没有标准化编程接口**：每个研究团队用不同的自定义指令集

---

## 八、学术原型的实测性能对比

| 架构 | 基底 | 阵列规模 | 能效 | 精度 | 年份/来源 |
|------|------|---------|------|------|----------|
| SIMDRAM | 商用DDR4 | 全芯片 | N/A（带宽提升为主） | 100%（数字） | 2021/ETH |
| 8T SRAM IMC | 90nm CMOS | 8×8 | 56.56 fJ/bit/MAC | 仿真验证 | 2025/arXiv |
| 65nm SRAM CIM | 65nm CMOS | 8×72 | 1.69 GOPS/W | 偏差1.05% | 2023/GUET |
| 7nm SRAM CIM | 7nm FinFET | 宏单元 | 50× GPU能效 | 98.3% CNN | 2022/IMEC |
| ReRAM Crossbar | 实验器件 | 64×64 | N/A | 受限于器件变异 | 多组 |

---

## 九、2026年产业信号

### SK海力士 CES 2026
- **cHBM**：Base Die集成计算，面向推理优化
- **AiMX**：GDDR6-AiM芯片的LLM加速器卡
- **CuD (Compute-using-DRAM)**：在DRAM单元内执行简单运算
- **CMM-Ax**：CXL内存模块+计算能力

### NVIDIA GTC 2026
- 探索SRAM-based推理架构作为HBM补充
- Rubin平台HBM4 + 3D堆叠提升有效带宽

### Samsung
- HBM4E展示：16Gbps/pin，总带宽4TB/s
- HCB技术：16层+堆叠
- 计划2028年HBM5（1c DRAM + 2nm工艺）

---

## 十、关键技术公式总结

| 场景 | 公式 | 含义 |
|------|------|------|
| DRAM电荷共享 | V_bl = (C_cell·V_cell + C_bl·VDD/2)/(C_cell+C_bl) | 位线电压=存储电容与位线电容的加权平均 |
| MAJ门 | MAJ(A,B,C) = AB+AC+BC | 三输入多数表决，可合成任意布尔函数 |
| ReRAM MVM | Iⱼ = Σᵢ Vᵢ·Gᵢⱼ | 基尔霍夫电流定律实现矩阵-向量乘法 |
| SRAM MAC | ΔV_RBL ∝ Σ(Aᵢ ∧ Bᵢ) | 读位线电压降 ∝ 激活单元数量 = MAC结果 |
| 推理吞吐 | Throughput ∝ Memory_Bandwidth / Model_Size | AI推理内存带宽决定论 |

---

## 相关实体
- [NVIDIA](../entities/nvidia.md)
- [三星](../entities/samsung.md)
- [SK海力士](../entities/sk-hynix.md)
- [HBM](../concepts/hbm.md)
- [Near-Memory Computing](near-memory-computing.md)

## 引用来源
- [SIMDRAM: End-to-End Bit-Serial SIMD, ASPLOS 2021](https://people.inf.ethz.ch/omutlu/pub/SIMDRAM_asplos21-talk.pdf) — ETH Zurich, Onur Mutlu组
- [PiDRAM: FPGA-based PuM Framework](https://www.researchgate.net/publication/355841864) — ETH Zurich
- [Ambit: In-Memory Accelerator, MICRO 2017](https://arxiv.org/abs/1708.01348) — V. Seshadri et al.
- [8T SRAM IMC Architecture, arXiv 2512.00441](https://arxiv.org/html/2512.00441v1) — 2025
- [SRAM-based CIM Review](https://arxiv.org/html/2411.06079v1) — Tutorial & Review, 2024
- [SRAM CIM Review (中文)](https://www.researching.cn/ArticlePdf/m00098/2022/43/3/031401.pdf) — 2022
- [ReRAM CIM Survey](https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5193/make-01-00005.pdf) — Make journal
- [ReRAM Crossbar DATE 2026](https://perso.lip6.fr/Theofilos.Spyrou/resources/DATE_2026.pdf) — 模拟器与器件建模
- [Compute-in-Memory PatSnap 2026](https://www.patsnap.com/resources/blog/rd-blog/compute-in-memory-neural-networks-2026-patsnap-eureka/) — 产业专利全景
- [Horowitz et al. ISSCC 2014](https://eyeriss.mit.edu/2020_efficient_dnn_excerpt.pdf) — 数据移动能耗分析
- [CIM Architecture Overview](https://no-1.pro/research/15-compute-in-memory/) — Ohm/Kirchhoff定律实现MVM

*最后更新：2026-05-12*  
*本文档从概述级拓展到电路级技术实现，涵盖物理机制、学术原型、产业瓶颈与实测数据。*