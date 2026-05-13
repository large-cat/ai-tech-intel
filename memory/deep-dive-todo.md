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
- [x] Processing-in-Memory深度调研（PuM/SRAM-CIM/ReRAM-CIM具体实现）
- [x] UCIe协议技术细节（电气层、物理层、信号完整性）
- [x] HBM制造工艺深度（TSV/HCB原子级原理、中介层设计）
- [x] CoWoS/EMIB/Foveros制造工艺对比

### 第二批：AI Agent工程细节
- [x] MCP协议技术规范（JSON-RPC 2.0、三大原语、Transport层、四阶段生命周期）
- [x] ACP/A2A协议对比（Agent Card、Task生命周期、三协议定位表）
- [x] Agent Skills SKILL.md具体格式 + OpenClaw运行时 + MCP SDK API
- [x] Harness方法论深度版（PEV循环数学化、Verifier独立性论证、MCP集成架构、Minions Blueprint实现细节）

### 第三批：AI训练/推理算法细节
- [x] Test-Time Compute算法深度（CoT数学分解、Self-Consistency投票、Best-of-N+ORM数学、PRM步骤级奖励公式、ToT Beam Search复杂度）
- [x] RLHF变体数学原理（PPO-CLIP损失+KL约束、DPO隐式奖励推导+与PPO对比表、GRPO组内相对优势公式+DeepSeek-R1纯RL路径）
- [x] DeepSeek-R1纯RL技术路径（GRPO跳过SFT、R1-Zero→R1演进）

### 第四批：半导体封装与近存计算
- [x] CoWoS/EMIB/Foveros制造工艺深度（CoWoS中介层Bosch DRIE全流程、光罩拼接技术、EMIB-T TSV改进、Foveros有源堆叠、Hybrid Bonding Cu-Cu原子级键合六步工艺、玻璃基板TGV）
- [x] Near-Memory Computing深度（UPMEM DPU架构64MB+24线程、AiMX 4芯片加速器、CXL 3.0 CMM-Ax协议栈、Google 3D-DRAM混合键合专利、数据搬运能耗100-1000×量化公式）

## 执行记录

#### 2026-05-12 — 第一批完成4/4
- [x] Processing-in-Memory深度版完成（电路级：DRAM电荷共享MAC、8T SRAM IMC、ReRAM Crossbar欧姆定律MVM、PiDRAM真实芯片验证、128Kb瓶颈分析）
- [x] UCIe协议深度扩展完成（三层协议栈、Lane/Module/Link结构、Bump-out规格、2.0 3D封装支持、与AIB/Lipincon/BoW对比）
- [x] HBM深度版完成（TSV DRIE Bosch全流程、Cu电镀底部向上填充、CMP与背面暴露、Base Die逻辑工艺、HCB混合铜键合原子级键合、JEDEC电气接口、TSV热应力Keep-out Zone）
- [x] CoWoS/EMIB/Foveros制造工艺对比完成（CoWoS中介层8步制造、光罩拼接、EMIB-T TSV+MIM、Hybrid Bonding六步工艺流程、玻璃基板CTE/TGV）

#### 2026-05-12 — 第二批完成4/4
- [x] Agent Skills深度版完成（MCP JSON-RPC 2.0消息格式、错误码表、Tool/Resource/Prompt三大原语、四阶段生命周期、Transport层stdio/SSE/HTTP、ACP/A2A协议对比、Stripe Minions 400+ MCP Tool实现）
- [x] Harness方法论深度版完成（PEV循环数学化公式、Verifier独立性论证、MCP集成架构图、Minions Blueprint 90分钟无人值守实现细节）

#### 2026-05-12 — 第三批完成3/3
- [x] Test-Time Compute深度版完成（CoT联合分布分解公式、Self-Consistency投票数学、Best-of-N+ORM交叉熵损失、PRM步骤级奖励公式+训练目标、ToT Beam Search O(b·k·d)复杂度、验证器类型对比表）
- [x] RLHF深度版完成（PPO-CLIP损失+KL散度约束+超参数表、DPO隐式奖励推导+与PPO四维对比表、GRPO组内相对优势公式+显存节省50%、Constitutional AI/RLAIF）

#### 2026-05-12 — 第四批完成2/2
- [x] Advanced Packaging深度版完成（CoWoS中介层8步制造工艺、光罩拼接亚微米对准、EMIB-T TSV+MIM电容+Cu接地网格、Foveros有源堆叠、Hybrid Bonding六步工艺流程、玻璃基板CTE/TGV）
- [x] Near-Memory Computing深度版完成（UPMEM DPU 64MB+24线程+编程模型、AiMX 4芯片加速器、CXL 3.0协议栈、Google 3D-DRAM混合键合专利、数据搬运能耗100-1000×公式）

## 下一步（明天继续更深入）
- [ ] **Agent Skills**：MCP Server实现示例（TypeScript/Python SDK代码）、Agent Card JSON Schema完整定义、MCP Sampling Loop（AI主动请求人类输入）
- [ ] **Harness**：Verifier Model训练方法（如何训练一个"严格"的LLM）、多Agent协作的分布式Harness架构、失败模式分类与自动恢复策略
- [ ] **Test-Time Compute**：PRM训练数据构建（如何标注步骤级标签）、PRM+RLHF联合训练、测试时计算的自适应预算分配（Adaptive Compute Budgeting）
- [ ] **RLHF**：在线DPO（Online DPO）vs离线DPO、IPO（Identity Preference Optimization）、KTO（Kahneman-Tversky Optimization）等2025-2026新变体
- [ ] **Processing-in-Memory**：存内计算的商业化障碍（良率、可靠性、编程模型）、工业界路线图（Samsung PIM-DRAM、SK hynix AiM、UPMEM量产进展）
- [ ] **HBM**：HBM4/5路线图（16Hi堆叠、2048-bit接口、3D DRAM）、HBM的热管理（TSV热应力模拟、微通道液冷）、HBM的测试挑战（KGD、老化测试）
- [ ] **Chiplet**：UCIe 2.0的3D封装电气规范、Chiplet的EDA工具链（芯原/芯来/新思）、Chiplet安全架构（UCIe Security层）
- [ ] **Advanced Packaging**：台积电CoWoS Gen6的12层中介层、Intel玻璃基板量产路线图、混合键合的可靠性（热循环、跌落测试）
- [ ] **Karpathy动态追踪**：microGPT更新（2026-02）、Claude coding工作流转变分析（2026-01推文）、2025 LLM Year in Review、新YouTube系列（RL+AI Agents）、Eureka Labs种子轮融资
- [ ] **12-Factor Agents深度调研**：humanlayer/12-factor-agents工程原则逐条解析、与Karpathy 4条原则的对比定位、生产级Agent架构实践
- [ ] **GitHub AI仓库排名追踪**：yuxiaopeng/Github-Ranking-AI（AI分类Top100）、EvanLi/Github-Ranking（全语言总榜Top100）、ossinsight.io/trending/ai（实时增长率Top50）

## 深度完成度追踪

| 主题 | 5月12日深度 | 目标深度 | 状态 |
|------|-----------|---------|------|
| Processing-in-Memory | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 待补商业化/可靠性 |
| Chiplet | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 待补UCIe 2.0 3D/EDA/安全 |
| HBM | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入热管理/测试） |
| Advanced Packaging | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入可靠性） |
| Near-Memory Computing | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 待补CXL内存池化 |
| Agent Skills | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入Sampling Loop） |
| Harness方法论 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入Verifier训练） |
| Test-Time Compute | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入自适应预算） |
| RLHF | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 已完成（可再深入Online DPO/KTO） |