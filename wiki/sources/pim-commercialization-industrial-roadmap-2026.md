# 存内计算（PIM）商业化障碍与工业界路线图深度调研

> 来源：arXiv 2401.14428 / arXiv 2310.09385 / Semiconductor Insight / SemiWiki / SK hynix MICRO 2025 Tutorial / Futurum Group / IIT Bombay MT Thesis / 芯智讯 / 极客时间
> 调研时间：2026-05-17

---

## 一、PIM DRAM 市场规模与增长预测

| 指标 | 数值 |
|------|------|
| 2025 年市场规模 | **USD 17.3 亿** |
| 2026 年市场规模 | **USD 21.4 亿** |
| 2034 年市场规模 | **USD 98.7 亿** |
| CAGR（2026–2034）| **18.5%** |

驱动因素：AI/ML 工作负载爆发、LLM 推理内存瓶颈、数据密集型应用（数据库、图计算、推荐系统）对带宽的指数级需求。

---

## 二、三大商业化障碍

### 2.1 制造工艺可及性（Process Accessibility）

PIM 的核心矛盾：**逻辑工艺与存储工艺根本不同**。

- **SRAM-CIM**：可采用标准逻辑工艺（CMOS），这是学术界原型 overwhelmingly 选择 SRAM 的根本原因——PDK 开放、流片门槛低。
- **DRAM-CIM / NVM-CIM**：Samsung、SK hynix、Micron 的 DRAM 工艺为** proprietary（专有）**，外部研究者无法获取 PDK，仅能依赖性能仿真验证架构，无法做物理设计和良率评估。
- 结果：DRAM-PIM 的商业化完全依赖内存原厂内部迭代，生态封闭。

> "Processes for DRAM and non-volatile memory are proprietary and not available to external developers. Without access to these PDKs, researchers struggle to even simulate basic circuits." —— IIT Bombay MT Thesis, 2024

### 2.2 物理面积约束与良率挑战

| 维度 | 具体矛盾 |
|------|---------|
| 面积 | 集成逻辑单元会减少可用存储容量；逻辑功能越通用，面积开销越大 |
| 良率 | DRAM 工艺聚焦 cell density，逻辑电路在 DRAM 工艺上良率显著低于纯逻辑工艺 |
| 热应力 | TSV + 逻辑发热 → 热梯度导致 Keep-out Zone 增大，有效 die area 减少 |
| 量产验证 | Samsung HBM4 曾因 1c DRAM 良率仅 ~65%（pilot run）而推迟量产至 2026；PIM 在 DRAM 上加逻辑，良率挑战更严峻 |

### 2.3 软件栈碎片化与编程模型鸿沟

PIM 不是"更快的 DRAM"，而是**需要全新软件栈的异构计算架构**：

| 层级 | 现状与障碍 |
|------|-----------|
| 编程语言 | 无统一标准；UPMEM 用 C + tasklet，Samsung HBM-PIM 用自定义 API，SK hynix AiM 用类似 CISC 指令集 |
| 编译器 | 需将算法映射为内存内操作序列（位操作、bank 级并行），现有编译器无法自动完成 |
| 驱动/运行时 | 数据搬移（CPU DRAM ↔ PIM MRAM）需显式管理；一致性语义未标准化 |
| 框架集成 | PyTorch/TensorFlow 无原生 PIM 后端；需通过 UPMEM SDK 或 HBM-PIM API 做手动扩展 |

> "The entire software stack must be re-evaluated, including programming languages, compilers, drivers, and runtime environments. Without such changes, CIM will struggle to surpass the performance of existing von Neumann architectures." —— IIT Bombay MT Thesis

**数据一致性语义**是隐藏的大坑：当 NDP 单元直接修改存储阵列时，CPU cache coherence 必须显式失效或写回。Intel 2024 HPCA 论文指出，引入轻量级目录协议可将一致性开销控制在 5% 以内，但需操作系统支持新的 page fault 语义。

---

## 三、三大厂商技术路线与量产进展

### 3.1 Samsung：HBM-PIM + AxDIMM 双线布局

| 产品 | 架构 | 关键参数 | 状态 |
|------|------|---------|------|
| **HBM-PIM** | HBM2 堆叠，每 2 个 bank 共享 1 个 SIMD PU | 带宽 307.2 GB/s，9.6 GFLOPS/PU，支持 MAD/MAC | 原型验证，与 SAP HANA 合作测试 |
| **AxDIMM** | DDR 模组 + FPGA fabric（Near-rank）| 针对推荐系统推理加速 | 原型阶段 |
| **FIMDRAM** | 存内计算 DRAM | 接近商业化，但 HBM 成本高限制普及 | 技术评估中 |

**Samsung 策略特点**：
- 依托自有 HBM 技术栈，走高端路线
- 与 SAP HANA 数据库进行联合优化，瞄准企业级 IMDBMS 市场
- 2026 年 HBM4 量产推迟至 2026（1c DRAM 良率 ~65%），间接影响 HBM-PIM 节奏

### 3.2 SK hynix：AiM（Accelerator-in-Memory）

| 参数 | 数值 |
|------|------|
| 基础内存 | GDDR6（非 HBM，成本更低） |
| 计算单元 | 每 bank 1 个 PU，16 个乘数器 + 加法树 |
| 吞吐 | **32 GFLOPS/PU**（高于 Samsung HBM-PIM 的 9.6 GFLOPS） |
| 数据类型 | INT8 / FP16（推测） |
| 指令集 | 类似 CISC，支持不同粒度运算（1, 4, 16 bank 组合） |
| 横向扩展 | 多播互连（Multicast）+ 路由器 + 指令排序器 |

**AiM 架构关键元件**：
- AiM 控制器
- 可扩展式多播互连
- 路由器
- 计算单元 + 指令排序器

**软件栈**：SK hynix 正在构建完整软件堆叠，但明确承认"**最大难题还是软件要怎么运用有计算能力的内存**"——如何将运算需求"映射"到内存内的执行单元。

**量产状态**：2023 Hot Chips 展示 4Gb GDDR6-AiM 样品照片 + FPGA 验证平台；SK hynix MICRO 2025 Tutorial 继续推进 PIM 研究，但明确处于**技术评估阶段**，尚未宣布量产时间表。

### 3.3 UPMEM：唯一商业化通用 PIM 产品

| 参数 | 数值 |
|------|------|
| 产品形态 | 标准 DDR4 DIMM 模组 |
| DPU 架构 | 32 位 RISC 核心，in-order |
| 每 DPU 私有内存 | 64 MB MRAM（Main RAM） |
| 每 DPU SRAM | 88 KB（24 KB IRAM + 64 KB WRAM） |
| 硬件线程 | 24 个 tasklet（共享 WRAM） |
| 每 8 GB 模组 | 128 个 DPU |
| 最大系统规模 | 20 个模组 = 2,560 DPU，160 GB MRAM，**2 TB/s 聚合带宽** |
| 编程模型 | SPMD（Single Program Multiple Data），类 SIMD |
| 吞吐 | 4.0 GOPS/DPU，仅支持 INT8 |

**UPMEM 商业化意义**：
- **唯一真正可购买的 PIM 硬件**（通过 AWS 云实例或 bare-metal 租赁）
- 证明了 DRAM-PIM 的工程可行性
- 但 INT8-only + 低单核性能限制了应用范围，主要适用于大规模并行内存密集型工作负载（基因组学、图分析、数据库扫描）

---

## 四、技术路线对比矩阵

| 维度 | Samsung HBM-PIM | SK hynix AiM | UPMEM DPU |
|------|-----------------|--------------|-----------|
| **内存类型** | HBM2 | GDDR6 | DDR4 |
| **定位** | 高端 AI 加速器 | 中端 AI/图形 | 通用并行计算 |
| **每 PU 性能** | 9.6 GFLOPS | 32 GFLOPS | 4.0 GOPS |
| **带宽/堆叠** | 307.2 GB/s | GDDR6 标准速率 | 2 TB/s（系统级） |
| **编程模型** | 自定义 API | 类 CISC 指令集 | C + tasklet |
| **软件成熟度** | 低（SAP 合作中） | 低（评估阶段） | 中（有 SDK） |
| **量产状态** | 原型 | 样品/评估 | **已商用** |
| **成本结构** | 高（HBM） | 中（GDDR6） | 低（标准 DDR） |
| **生态开放性** | 封闭 | 封闭 | 相对开放（有 SDK） |

---

## 五、商业化路径预测

### 短期（2026–2028）：利基市场突破

- **UPMEM**：继续服务生物信息学、图数据库等小众高并行场景
- **Samsung HBM-PIM**：若 HBM4 量产顺利，可能随 HBM4 迭代推出 PIM 版本，但仅限超大规模数据中心
- **SK hynix AiM**：若 GDDR6-AiM 验证成功，可能先进入图形/AI 推理加速器市场（成本低于 HBM-PIM）

### 中期（2028–2032）：软件生态决定胜负

- 关键变量：**能否出现类似 CUDA 的统一 PIM 编程框架**
- 当前碎片化的 SDK/API 是最大 adoption barrier
- 若 CXL 3.0 + PIM 融合成功，可能通过标准化内存池化接口降低编程门槛

### 长期（2032+）：架构融合

- Processing-in-Memory → Processing-in-Storage（Kioxia CD6-C SSD 已集成 128×128 INT8 MAC）
- PIM 与 CXL、Chiplet、3D DRAM 深度整合，成为计算架构的"默认选项"而非"特殊加速器"

---

## 六、关键结论

1. **PIM 不是技术问题，是生态问题**：三家厂商的技术路线都已验证可行，但软件栈碎片化、编程模型门槛、工艺封闭性构成"三重锁"。
2. **Samsung 走高端、SK hynix 走中端、UPMEM 走通用**——三条路径互补，但短期内不会互相替代。
3. **良率和成本是量产生死线**：Samsung HBM4 推迟已经证明，在 DRAM 工艺上叠加逻辑的良率挑战远超预期。
4. **市场规模 CAGR 18.5% 看似乐观，但基数极小**（$1.73B），2034 年 $9.87B 也仅相当于 2025 年 HBM 市场的几分之一。
5. **最大的隐性风险**：如果 CXL + 标准 DRAM 就能解决 80% 的带宽瓶颈，PIM 的"必要性"会被削弱——PIM 必须证明其**不可替代性**，而非仅"更快一点点"。

---

## 参考来源

- arXiv:2401.14428 "The Landscape of Compute-near-memory and Compute-in-memory"
- arXiv:2310.09385 "PIM-GPT: A Hybrid Process-in-Memory Accelerator"
- Semiconductor Insight: "Processing In Memory (PIM) DRAM Market, Trends, Business Strategies 2026-2034"
- SemiWiki: "Samsung delays HBM4 rollout to 2026 due to yield challenges"
- SK hynix MICRO 2025 Tutorial — PIM (AiM) Session
- IIT Bombay MT Thesis: "Challenges of CIM Architecture"
- 芯智讯: "三星与SK海力士的存内计算布局"
- 极客时间 / MBA智库: "AI存储系统需求研究"
- TransPIMLib (ISPA 2023): "Processor performance increasing more rapidly than memory performance"
