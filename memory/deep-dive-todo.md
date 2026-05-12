# 深度调研计划 — wiki知识拓展

## 状态：执行中

## 评估结果

当前wiki知识深度（1=最浅，5=最深）：
| 主题 | 深度 | 优先深挖理由 |
|------|------|-------------|
| Processing-in-Memory | ⭐ | 最浅，分类概述，缺具体技术实现 |
| Chiplet | ⭐⭐ | 有框架缺UCIe协议细节、制造工艺 |
| HBM | ⭐⭐⭐ | 有代际演进缺TSV/HCB制造工艺细节 |
| Advanced Packaging | ⭐⭐⭐ | 有平台对比缺工艺参数 |
| Near-Memory Computing | ⭐⭐ | cHBM/AiMX缺架构细节 |
| Agent Skills | ⭐⭐ | 概念介绍缺SKILL.md格式规范 |
| Harness方法论 | ⭐⭐⭐⭐ | 已较深，但MCP/ACP/A2A协议细节可补 |
| Test-Time Compute | ⭐⭐⭐ | 方法分类缺算法实现细节 |
| RLHF | ⭐⭐⭐ | 变体概述缺GRPO/DPO数学原理 |

## 批次安排

### 第一批：半导体底层技术深挖
- [ ] Processing-in-Memory深度调研（PuM/SRAM-CIM/ReRAM-CIM具体实现）
- [ ] UCIe协议技术细节（电气层、物理层、信号完整性）
- [ ] HBM制造工艺深度（TSV/HCB原子级原理、中介层设计）
- [ ] CoWoS/EMIB/Foveros制造工艺对比

### 第二批：AI Agent工程细节
- [ ] MCP协议技术规范（JSON-RPC、资源/工具/提示三大原语）
- [ ] ACP/A2A协议对比
- [ ] Agent Skills SKILL.md具体格式
- [ ] Harness Evals体系（52%缺口的具体方案）

### 第三批：AI训练/推理算法细节
- [ ] Test-Time Compute算法深度（CoT token经济学、ToT实现、PRM训练）
- [ ] RLHF变体数学原理（GRPO、DPO简化推导、Constitutional AI）
- [ ] DeepSeek-R1纯RL技术路径

## 执行记录

#### 2026-05-12 — 第一批完成3/4
- [x] Processing-in-Memory深度版完成（电路级：DRAM电荷共享MAC、8T SRAM IMC、ReRAM Crossbar欧姆定律MVM、PiDRAM真实芯片验证、128Kb瓶颈分析）
- [x] UCIe协议深度扩展完成（三层协议栈、Lane/Module/Link结构、Bump-out规格、2.0 3D封装支持、与AIB/Lipincon/BoW对比）
- [x] HBM深度版完成（TSV DRIE Bosch全流程、Cu电镀底部向上填充、CMP与背面暴露、Base Die逻辑工艺、HCB混合铜键合原子级键合、JEDEC电气接口、TSV热应力Keep-out Zone）
- [ ] CoWoS/EMIB/Foveros制造工艺对比（待执行）
