# EDA 厂商竞逐台积电埃米时代路线图（2026 TSMC Symposium）

> 来源：Futurum Group（2026-04-24）  
> 新思（Synopsys）、楷登（Cadence）、西门子 EDA 在台积电北美技术论坛的对齐动作

---

## 核心事件

2026 年台积电北美技术论坛上，三大 EDA 巨头同时发布与台积电最新工艺/封装节点的深度协作：

| EDA 厂商 | 发布内容 | 与台积电的绑定点 |
|----------|---------|-----------------|
| **Synopsys** | AI 驱动设计全流程 + 3nm/2nm 签核工具 | Angstrom-era 工艺签核 |
| **Cadence** | 先进封装 + 3D-IC 设计平台 | CoWoS / SoIC / 3D 堆叠 |
| **Siemens EDA** | 数字孪生 + 良率提升平台 | 晶圆厂数据闭环 |

---

## 关键趋势：COUPE 共封装光学重塑 EDA 竞争

**COUPE（Co-Packaged Optics / 共封装光学）** 正在成为 EDA 工具的新战场：
- 光 I/O 与电 I/O 的协同设计
- 光子器件仿真 + 电子设计自动化融合
- 封装级光学布线规则

这对 EDA 厂商的要求：
1. 跨域仿真能力（光学 + 电气 + 热学）
2. 先进封装物理验证（3D 堆叠、hybrid bonding、硅光）
3. 与台积电 PDK（Process Design Kit）的原生集成

---

## 台积电 Angstrom-Era 路线图的 EDA 含义

| 技术节点 | EDA 挑战 | 厂商响应 |
|----------|---------|---------|
| **2nm / 18A** | GAA 晶体管仿真复杂度 | Synopsys AI 驱动 SPICE / TCAD |
| **CoWoS-L / Gen6** | 12 层中介层、光罩拼接 | Cadence 3D-IC 集成平台 |
| **SoIC（3D）** | 芯片堆叠 + 热-电协同 | Siemens 数字孪生 + 热仿真 |
| **硅光 / COUPE** | 光子器件 + 封装级光学 | 三厂均在布局 |

---

## 竞争格局变化

- **Synopsys**：在 AI 驱动设计（DSO.ai 扩展）和 2nm 签核保持领先
- **Cadence**：押注先进封装/3D-IC，与台积电 CoWoS/SoIC 深度绑定
- **Siemens EDA**：以数字孪生和良率优化差异化，工厂数据闭环是独特优势

**共同压力**：
- 台积电客户（NVIDIA、Google、AMD）的 chiplet/3D 设计越来越复杂
- 设计-工艺-封装的协同优化（DTCO）成为刚需
- EDA 工具如果不能在台积电 PDK 发布首日就绪，客户会流失

---

## 对 Chiplet 生态的支撑

EDA 工具链成熟度直接决定 chiplet 设计门槛：
- **Chiplet 架构探索**：需快速评估不同 partition 方案的 PPAC（功耗-性能-面积-成本）
- **Die-to-Die 接口验证**：UCIe / AIB 的电气/协议一致性检查
- **3D 堆叠热-机械协同**：Hybrid bonding + TSV 的热应力仿真
- **供应链协同设计**：不同工艺节点 die 的良率模型整合

---

## 参考链接

- Futurum Group 分析：https://futurumgroup.com/insights/eda-vendors-race-to-align-with-tsmcs-angstrom-era-roadmap-at-technology-symposium/
- 关联 wiki：concepts/chiplet.md | concepts/advanced-packaging.md | entities/synopsys.md | entities/cadence.md | entities/tsmc.md
