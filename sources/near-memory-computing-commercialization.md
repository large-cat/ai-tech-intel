# 近存计算（Near-Memory Computing）商业化全景 2026

> 来源：PatSnap Eureka 研究报告（2026-04-24）+ 产业专利/产品动态  
> 覆盖：技术架构、商业化产品、关键玩家、能耗量化、编程模型障碍

---

## 一、为什么近存计算是 ML 的理想场景

传统冯·诺依曼架构的 **"memory wall"** 在 ML  workload 中尤为突出：
- 数据搬运能耗可占系统总能耗的 **80%**
- 推理延迟可通过近存架构降低 **2-5×**

ML workload 的独特适配性：
- 高内存带宽需求
- 重复计算模式（矩阵乘、卷积、激活）
- 显著的数据重用机会

---

## 二、现有商业化产品矩阵

### 2.1 Processing-in-Memory（PIM）

| 产品 | 厂商 | 技术方案 | 关键指标 |
|------|------|---------|---------|
| **HBM-PIM** | Samsung | HBM2 内嵌 DRAM-based 计算单元 | 1.2 TB/s 带宽，能耗降低 **70%** vs GPU |
| **GDDR6-AiM** | SK hynix | GDDR6 内嵌加速器（AiMX） | 推理优化 |
| **AiMX 加速器** | SK hynix | 4 芯片加速器方案 | 边缘/推理场景 |

**HBM-PIM 细节**：
- 每个 memory bank 嵌入计算单元
- 支持向量运算、矩阵乘法、激活函数
- 专用指令集：convolution、pooling、normalization
- 优化方向：transformer、CNN

### 2.2 Near-Data Computing

| 产品 | 厂商 | 架构特点 |
|------|------|---------|
| **DPU（UPMEM）** | UPMEM | DRAM 模块集成处理核心，64MB + 24 线程 |
| **CXL 3.0 CMM-Ax** | 行业标准 | 内存池化 + 近端加速 |

**UPMEM DPU 编程模型**：
- 类 C 语言（DPU-C）
- 数据并行：每个 DPU 独立处理本地 64MB DRAM
- 主机 offload 任务到 DPU array
- 限制：单 DPU 计算能力有限，复杂运算仍需回传主机

### 2.3 3D-DRAM / 混合键合方向

- **Google 专利**：3D-DRAM 混合键合方案（wafer-to-wafer）
- 目标：将计算层与存储层通过 Hybrid Bonding 直接堆叠
- 优势：消除 TSV 电阻/电容，带宽密度数量级提升

---

## 三、关键玩家技术路线对比

| 厂商 | 技术路线 | 优势 | 劣势 |
|------|---------|------|------|
| **Samsung** | HBM-PIM（PIM-DRAM） | 业界领先带宽，与 GPU 生态整合强 | 可编程性受限，新算法支持慢 |
| **SK hynix** | GDDR6-AiM / AiMX | 推理能效比优异，边缘市场切入 | 训练场景覆盖弱 |
| **Intel** | Optane DC + PIM | 数据中心可扩展性成熟，软件栈完整 | 功耗高 vs 专用方案，Optane 已停产 |
| **UPMEM** | DPU-DRAM | 近存架构纯粹，编程模型相对开放 | 生态小，单 DPU 算力弱 |
| **Google** | 3D-DRAM 混合键合（专利阶段） | 带宽密度理论上限最高 | 商业化时间不确定 |

---

## 四、商业化障碍（2026 现状）

### 4.1 良率与可靠性
- 存储 die 内嵌计算单元 → 面积增加 → 良率下降
- 热管理：高密度配置下额外热源叠加，存储器件温度容限通常比处理器更严格
- 长期可靠性数据不足：PIM 产品大规模部署 <3 年

### 4.2 编程模型复杂度
- **当前痛点**：需 specialized programming interfaces，手动优化
- **缺乏标准化 API**：不像 CUDA 有统一生态
- **框架集成缺口**：PyTorch/TensorFlow 自动 offloading 到 PIM 尚未成熟

### 4.3 计算复杂度天花板
- 现有方案仅支持 elementary operations（向量加、矩阵乘）
- 复杂 ML 运算（attention mechanism 中的 softmax、layer norm）仍需与主机频繁交互
- 部分抵消了近存收益

### 4.4 规模化协调挑战
- 多 PIM/Near-Memory 处理器协同 → 一致性管理、单元间通信
- 当前方案未完全解决

---

## 五、能耗量化公式

> 数据搬运 vs 计算的能耗比：**100-1000×**

```
E_total = E_compute + E_data_movement

传统架构：
  E_data_movement ≈ 0.8 × E_total  (内存墙极限)

近存架构目标：
  E_data_movement ≈ 0.2 × E_total  (降低 60-75%)
  → 对应系统级能效提升 2-5×
```

PatSnap 专利分析显示：
- **非易失性近存 ML 加速器**（US20250130805A1）：权重直接从 NVM 读取，ping-pong buffer 最小化数据总线占用
- **模拟 MAC 近存方案**（WO2021126706A1）：用电容替代数字加法器，分段阵列优化 bitline 电容 → 更快、更低能耗

---

## 六、市场驱动与需求结构

| 细分市场 | 需求特征 | 近存适配度 |
|----------|---------|-----------|
| **数据中心/云** | 大模型推理/训练，性能 per watt | ⭐⭐⭐⭐⭐ |
| **边缘/嵌入式** | 电池/热约束，低延迟 | ⭐⭐⭐⭐⭐ |
| **移动设备** | 功耗极度敏感，AI 功能化 | ⭐⭐⭐⭐ |
| **汽车/自动驾驶** | 实时推理，可靠性要求 | ⭐⭐⭐⭐ |
| **AR/VR** | 超低延迟，传感器融合 | ⭐⭐⭐⭐⭐ |
| **高频交易** | 微秒级延迟 | ⭐⭐⭐⭐ |

---

## 七、标准与生态进展

- **IEEE**：制定多层级能效标准，涵盖 TDP、DVFS、idle 功耗管理
- **MLPerf**：引入 energy-aware benchmarking，评估加速器能效
- **EU Energy Efficiency Directive**：强制能效报告，创造市场激励
- **CXL 3.0**：内存扩展 + 池化协议栈，为 Near-Memory 提供互联基础

---

## 八、硬件-软件协同设计趋势

近存 ML 成功的必要条件是 **co-design**：
1. 工作负载特征分析（数据访问模式、计算强度、带宽需求）
2. 联合设计：定制指令集、专用数据通路、内存层次
3. 编译器优化：自动划分传统处理器 ↔ 近存计算单元
4. 智能内存控制器：预取训练数据、管理梯度更新、协调多处理单元

**神经形态计算**是 co-design 的极端案例：
- 硬件模仿神经网络结构
- 软件适配算法以利用固有并行性和低功耗特性

---

## 参考链接

- PatSnap Eureka 报告：https://eureka.patsnap.com/report-how-to-enhance-machine-learning-capacities-in-near-memory-setups
- 关联 wiki：concepts/processing-in-memory.md | concepts/near-memory-computing.md | entities/samsung.md | entities/sk-hynix.md
