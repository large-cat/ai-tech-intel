# Near-Memory Computing（近存计算）

**类型**：存算一体子方向  
**别名**：Processing-Near-Memory (PNM) / Near-Data Processing  
**核心思想**：**把计算逻辑搬到内存旁边，而不是让数据跑来跑去**

---

## 🧬 技术原理深度版

### 冯·诺依曼瓶颈量化

传统计算机架构中，数据搬运消耗的能量远大于计算：

$$E_{total} = E_{compute} + E_{data\_movement}$$

其中：
- $E_{compute}$：算术运算能耗（~1 pJ/op，28nm工艺）
- $E_{data\_movement}$：数据从DRAM到CPU的搬运能耗（~100-1000 pJ/word）

**关键比例**：
$$\frac{E_{data\_movement}}{E_{compute}} \approx 100 \sim 1000 \times$$

来源：Horowitz et al. "Computing's Energy Problem (and what we can do about it)", ISSCC 2014；arxiv.org/abs/2511.22889

**AI推理中的数据搬运占比**：
- Transformer推理：60%+ 系统能耗用于权重/激活值搬运
- 来源：eyeriss.mit.edu/2020_efficient_dnn_excerpt.pdf

### Near-Memory Computing的解法

**核心公式**：推理吞吐量 ∝ 内存带宽 / 模型权重大小

- **把计算逻辑放在内存控制器/内存旁边**
- **减少数据移动距离**：从"去CPU计算"变成"在内存旁边算"
- **带宽优势**：内存旁边的计算单元可以直接访问HBM/DRAM的宽总线

---

## 🏛️ 与Processing-in-Memory的关系

Near-Memory Computing是**存算一体的三大子方向之一**：

| 子方向 | 计算位置 | 成熟度 | 主要玩家 |
|--------|----------|--------|----------|
| **Near-Memory Computing** | 逻辑层紧邻DRAM/HBM | **最接近产品化** | NVIDIA、SK海力士、Google、UPMEM |
| **Compute-in-Memory (CIM)** | 在内存位单元内执行运算 | 实验室→原型 | 清华、Stanford、SK海力士(CuD) |
| **Logic-in-Memory (LIM)** | 存储单元内嵌入布尔逻辑 | 早期研究 | 高校为主 |

---

## 🔑 技术实现方式深度版

### 1. HBM基板集成（cHBM / Compute-on-Base）

**SK海力士 cHBM（Compute HBM）**：

架构细节：
```
┌─────────────────────────────┐
│  HBM DRAM Die Stack         │  ← 8层DRAM，每层2GB
│  ├── TSV垂直互联（40μm直径） │
│  └── 1024-bit/channel总线    │
├─────────────────────────────┤
│  Base Die（逻辑层）          │  ← **计算单元集成于此**
│  ├── 内存控制器 + PHY        │
│  ├── 小型计算引擎（MAC阵列） │
│  └── UCIe/CXL接口           │
└─────────────────────────────┘
```

- **计算单元位置**：在HBM的Base Die（最底层逻辑Die）上添加MAC阵列
- **总线宽度**：1024-bit/2048-bit（HBM3E为2048-bit，4通道）
- **理论带宽**：819 GB/s（HBM3E）→ 计算单元可直接消费
- **优势**：无需数据出HBM封装即可完成部分计算（如注意力Softmax前的部分累加）

**cHBM效率提升**：
- 预计2-5倍 vs 传统HBM（数据不出封装）
- 来源：SK海力士 CES 2026展示（待官方技术白皮书补充）

---

### 2. UPMEM（商用近存计算处理器）

> UPMEM是目前**唯一量产的近存计算处理器**，由法国UPMEM公司开发。

**架构**：
```
┌─────────────────────────────────────┐
│  标准DDR4/DIMM接口                  │
├─────────────────────────────────────┤
│  UPMEM DIMM × N                     │
│  ├─ 每个DIMM含 8/16 颗 UPMEM芯片    │
│  └─ 每颗芯片：DRAM + 集成处理器      │
├─────────────────────────────────────┤
│  UPMEM芯片内部                      │
│  ├─ 64MB DRAM（标准工艺）            │
│  ├─ 1个DPU（Data Processing Unit）  │
│  │   ├── 32-bit RISC核心             │
│  │   ├── 24个硬件线程                │
│  │   └── 专用指令集（SIMD）          │
│  └─ 内存带宽：DPU直接访问本地64MB    │
└─────────────────────────────────────┘
```

**关键参数**：
| 参数 | 数值 |
|------|------|
| 每芯片DRAM容量 | 64MB |
| DPU核心数 | 1（24线程） |
| 指令集 | 32-bit RISC，SIMD扩展 |
| 内存带宽（每芯片） | ~10 GB/s（本地访问） |
| 峰值性能（INT8 MAC） | ~1 TOPS/芯片 |
| 能耗效率 | ~10× vs GPU（数据密集型任务） |

**编程模型**：
```c
// UPMEM SDK：数据并行，每DPU处理本地数据
dpu_for_each(dpu, rank) {
    // DPU本地DRAM中的数据
    int *input = DPU_MRAM_HEAP_POINTER;
    // DPU本地计算，无需与CPU交互
    for (int i = 0; i < local_size; i++) {
        result[i] = input[i] * 2;  // 本地MAC
    }
}
```

**适用场景**：
- 数据库索引扫描（SELECT WHERE）
- 基因组序列比对（k-mer匹配）
- 稀疏矩阵运算（本地数据无需搬运）

---

### 3. SK海力士 AiMX（AI Memory Accelerator）

**CES 2026发布**：基于GDDR6-AiM（AI Memory）芯片的LLM专用加速器卡。

**架构**：
```
┌─────────────────────────────────────┐
│  AiMX Accelerator Card              │
│  ├─ 4× AiM芯片（GDDR6接口）          │
│  ├─ 每AiM芯片集成计算单元           │
│  │   └── 面向Transformer优化        │
│  └─ PCIe 5.0 ×16 连接主机           │
└─────────────────────────────────────┘
```

**关键信号**：
- 客户从"纯性能"转向"推理效率+成本优化"
- AiM芯片在内存旁边执行部分注意力计算，减少主机GPU负载
- 目标市场：边缘推理、中小模型serving

---

### 4. 3D-DRAM Chiplet（Google专利）

**Google专利（2024）**：计算-内存3D堆叠Chiplet

架构概念：
```
┌─────────────────────────────┐
│  计算Die（3nm逻辑）          │  ← CPU/GPU/TPU核心
│  └── 底部：Cu-Cu Hybrid Bond│
├─────────────────────────────┤  ← 亚10μm间距混合键合
│  内存Die（DRAM）             │  ← HBM/3D-DRAM
└─────────────────────────────┘
```

- **设计目标**：LLM serving优化，低功耗、高带宽
- **连接方式**：混合键合（Hybrid Bonding）
- **状态**：专利阶段，未商用

---

### 5. CXL内存+计算（CMM-Ax）

**SK海力士 CMM（CXL Compute Memory Module）**：

CXL（Compute Express Link）协议栈：
```
┌─────────────────────────────────────┐
│  应用层：AI框架（PyTorch/TensorFlow）│
├─────────────────────────────────────┤
│  CXL.mem协议：内存一致性访问        │
├─────────────────────────────────────┤
│  CXL.io协议：I/O兼容PCIe 5.0        │
├─────────────────────────────────────┤
│  物理层：PCIe 5.0/6.0（32/64 GT/s） │
└─────────────────────────────────────┘
```

CMM-Ax在CXL内存模块上集成计算：
- **标准化接口**：CXL 3.0，兼容现有服务器架构
- **应用场景**：服务器扩展内存 + 近端计算
- **优势**：无需修改CPU架构，即插即用

---

### 6. SmartNIC/DPU（广义近存计算）

**NVIDIA BlueField-3**：
- 在网卡上集成ARM核心 + 加速引擎
- 数据在到达CPU前就被处理（网络包解析、加密、压缩）
- **归类**：广义近存计算（数据在"进入系统"前就被处理）

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 数据搬运能耗占比 | 60%+（传统架构） | Horowitz et al. 2014; arxiv 2511.22889 |
| HBM基板带宽 | 1024-bit × 4 = 4096-bit总线 | HBM标准规范 |
| cHBM效率提升 | 预计2-5倍（vs传统HBM） | SK海力士 CES 2026展示 |
| UPMEM每芯片容量 | 64MB DRAM + 1 DPU | UPMEM官方 |
| UPMEM每芯片性能 | ~1 TOPS INT8 | UPMEM官方 |
| UPMEM能耗效率 | ~10× vs GPU | UPMEM benchmark |
| SRAM vs DRAM面积比 | 5-10倍 | 半导体工艺数据 |
| CXL 3.0带宽 | 64 GT/s ×16 = 128 GB/s | CXL Consortium |
| AiM芯片数量/卡 | 4×（AiMX设计） | SK海力士 CES 2026 |

---

## 🔗 相关页面
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体全景
- [entities/sk-hynix.md](../entities/sk-hynix.md) — cHBM/AiMX/CuD
- [entities/nvidia.md](../entities/nvidia.md) — SRAM探索/BlueField
- [concepts/hbm.md](hbm.md) — HBM技术基础
- [entities/google-deepmind.md](../entities/google-deepmind.md) — 3D-DRAM专利

---

*最后更新：2026-05-12*  
*信息来源：SK海力士CES 2026, UPMEM官方文档, Google 3D-DRAM专利, Horowitz et al. ISSCC 2014, CXL Consortium规范*