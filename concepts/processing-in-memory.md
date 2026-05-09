# 存算一体 / Processing-in-Memory (PIM)

> 类型：硬件架构 | 别名：近存运算、Compute-in-Memory | 最后更新：2026-05-09

## 问题：内存墙 (Memory Wall)

在传统冯·诺依曼架构中，数据在CPU和DRAM之间搬运：
- 现代工作负载中，**数据移动消耗超过60%的系统能耗**
- 50%的执行时间浪费在基于页的虚拟内存开销上
- AI推理是**内存带宽受限**，而非算力受限

## 三大子方向

| 方向 | 英文 | 原理 | 距离 |
|------|------|------|------|
| **近存处理** | Near-Memory Processing (NMP) | 逻辑层紧邻DRAM/HBM/SSD | 最近 |
| **存内计算** | Compute-in-Memory (CIM) | 在内存位单元内执行运算 | 在内部 |
| **存内逻辑** | Logic-in-Memory (LIM) | 在存储单元内嵌入布尔逻辑 | 在内部 |

## 技术集群

### 集群1：基于DRAM的Processing-Using-Memory (PuM)
- 利用DRAM的电荷共享和位线感应物理特性
- 无需修改硬件即可在标准DRAM中执行位运算
- 代表：ETH Zurich的SIMDRAM、PiDRAM

### 集群2：SRAM-based CIM（边缘AI主流）
- 修改6T/8T SRAM阵列，在位单元内执行乘累加(MAC)
- 无需片外数据移动
- 代表：Purdue IMAC、Rice CAP-RAM

### 集群3：阻变/非易失存储器CIM
- ReRAM/RRAM/MRAM/PCM多电平模拟存储
- 利用欧姆定律和基尔霍夫电流定律执行向量矩阵乘法
- 代表：Stanford RRAM-CIM、清华Beijing Innovation Center

### 集群4：3D堆叠与Chiplet封装
- 通过TSV、2.5D中介层物理缩短逻辑与内存距离
- 代表：Carnegie Mellon FPGA+HBM、Google 3D-DRAM chiplet

## 2026年产业动态

### NVIDIA GTC 2026
- 探索SRAM-based推理架构（HBM的补充）
- Rubin平台采用HBM4，通过3D堆叠提升带宽

### SK海力士 CES 2026
- **cHBM (Custom HBM)**：将GPU/ASIC部分功能集成到HBM基板
- **AiMX**：基于GDDR6-AiM芯片的LLM加速器卡
- **CuD (Compute-using-DRAM)**：在DRAM单元内执行简单计算
- **CMM-Ax**：CXL内存模块+计算能力

### 三星 GTC 2026
- HBM4E展示：16Gbps/pin，总带宽4TB/s
- 混合铜键合(HCB)技术：支持16层以上堆叠
- 计划2028年推出HBM5（1c DRAM + 2nm工艺）

### 产业痛点
- 大多数CIM演示仍限于**128Kb以下阵列**
- 模拟非理想性随规模扩大而恶化
- 缺乏CIM编译器和模拟工具链（软件-硬件协同设计缺口）

## 关键数字
- **60%+**：数据移动占系统能耗比例
- **2×**：近存储处理端到端延迟降低（Harvard RecSSD）
- **98.34%**：FeFET MCAM少样本学习准确率
- **4.7×**：ReCAM vs GPU的DNA比对吞吐量提升

## 相关实体
- [NVIDIA](../entities/nvidia.md)
- [三星](../entities/samsung.md)
- [SK海力士](../entities/sk-hynix.md)
- [HBM](../concepts/hbm.md)
