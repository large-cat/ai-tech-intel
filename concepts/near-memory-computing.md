# Near-Memory Computing（近存计算）

**类型**：存算一体子方向  
**别名**：Processing-Near-Memory (PNM) / Near-Data Processing  
**核心思想**：**把计算逻辑搬到内存旁边，而不是让数据跑来跑去**

---

## 🧬 技术原理

### 冯·诺依曼瓶颈
传统计算机架构：
- CPU和内存分离，数据通过总线搬运
- **AI推理中**：数据搬运消耗60%+系统能耗，延迟远高于计算本身
- **关键矛盾**：算力增长快于内存带宽（"内存墙"）

### Near-Memory Computing的解法
- **把计算逻辑放在内存控制器/内存旁边**
- **减少数据移动距离**：从"去CPU计算"变成"在内存旁边算"
- **带宽优势**：内存旁边的计算单元可以直接访问HBM/DRAM的宽总线

**关键公式**：推理吞吐量 ∝ 内存带宽 / 模型权重大小 [来源：AI推理性能分析经典公式，NVIDIA/MLSys社区共识]

---

## 🏛️ 与Processing-in-Memory的关系

Near-Memory Computing是**存算一体的三大子方向之一**：

| 子方向 | 计算位置 | 成熟度 | 主要玩家 |
|--------|----------|--------|----------|
| **Near-Memory Computing** | 逻辑层紧邻DRAM/HBM | **最接近产品化** | NVIDIA、SK海力士、Google |
| **Compute-in-Memory (CIM)** | 在内存位单元内执行运算 | 实验室→原型 | 清华、Stanford、SK海力士(CuD) |
| **Logic-in-Memory (LIM)** | 存储单元内嵌入布尔逻辑 | 早期研究 | 高校为主 |

---

## 🔑 技术实现方式

### 1. HBM基板集成（cHBM）
- **SK海力士**：将GPU/ASIC部分功能集成到HBM基板
- **原理**：在HBM的逻辑层（Base Die）上添加计算单元
- **优势**：利用HBM的宽总线（1024-bit/2048-bit），带宽极高
- **成熟度**：产品化中，CES 2026展示

### 2. 3D-DRAM Chiplet
- **Google专利（2024）**：计算-内存3D堆叠Chiplet
- **设计**：针对LLM serving优化，低功耗、高带宽
- **状态**：专利阶段，未商用

### 3. CXL内存+计算（CMM-Ax）
- **SK海力士**：CXL接口内存模块 + 计算能力集成
- **应用场景**：服务器扩展内存+近端计算
- **优势**：标准化接口（CXL），兼容现有服务器架构

### 4. SmartNIC/DPU
- **NVIDIA BlueField**：在网卡上集成计算，减少CPU参与
- **归类**：广义近存计算（数据在到达CPU前就被处理）

---

## 🚀 2026年产业信号

### SK海力士 CES 2026
- **cHBM**：将GPU/ASIC功能集成到HBM基板
- **AiMX**：基于GDDR6-AiM芯片的LLM专用加速器卡
- **信号**：客户从"纯性能"转向"推理效率+成本优化"

### NVIDIA SRAM探索
- **片上SRAM**：将大型SRAM块置于芯片内部，减少数据移动
- **定位**：HBM的补充（小容量、超高速缓存）
- **限制**：SRAM面积是DRAM的5-10倍，只能做小容量

### Google 3D-DRAM
- **专利**：2024年申请，计算-内存3D堆叠
- **目标**：LLM serving优化
- **状态**：早期研究

---

## 📊 关键数据

| 指标 | 数据 | 来源 |
|------|------|------|
| 数据搬运能耗占比 | 60%+（传统架构） | Horowitz et al. 2014; arxiv 2511.22889 |
| HBM基板带宽 | 1024-bit × 4 = 4096-bit总线 | HBM标准规范 |
| cHBM效率提升 | 预计2-5倍（vs传统HBM） | SK海力士 CES 2026展示 [来源：待补充官方技术白皮书] |
| SRAM vs DRAM面积比 | 5-10倍 | 半导体工艺数据 [来源：NVIDIA/SK海力士公开技术讨论] |

---

## 🔗 相关页面
- [concepts/processing-in-memory.md](processing-in-memory.md) — 存算一体全景
- [entities/sk-hynix.md](../entities/sk-hynix.md) — cHBM/AiMX/CuD
- [entities/nvidia.md](../entities/nvidia.md) — SRAM探索
- [concepts/hbm.md](hbm.md) — HBM技术基础

---

*最后更新：2026-05-09*  
*信息来源：SK海力士CES 2026、学术论文、专利数据库*
