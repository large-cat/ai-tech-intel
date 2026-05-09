// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded affix "><a href="index.html">封面与导言</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">卷一：今日速递</li><li class="chapter-item expanded "><a href="part1/2026-05-09.html"><strong aria-hidden="true">1.</strong> 2026年5月9日：Harness成为核心范式、NVIDIA双架构、存算一体走向产品</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">卷二：AI Agent 工程</li><li class="chapter-item expanded "><a href="part2/01-harness.html"><strong aria-hidden="true">2.</strong> Harness 方法论：Agent = Model + Harness</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="part2/02-anthropic-harness.html"><strong aria-hidden="true">2.1.</strong> Anthropic：三Agent架构与Managed Agents</a></li><li class="chapter-item "><a href="part2/03-openai-harness.html"><strong aria-hidden="true">2.2.</strong> OpenAI：100万行零手写代码</a></li><li class="chapter-item "><a href="part2/04-stripe.html"><strong aria-hidden="true">2.3.</strong> Stripe Minions：确定性×智能体混合</a></li><li class="chapter-item "><a href="part2/05-langchain.html"><strong aria-hidden="true">2.4.</strong> LangChain：模型不变，Harness变，结果剧变</a></li><li class="chapter-item "><a href="part2/06-moonshot.html"><strong aria-hidden="true">2.5.</strong> 月之暗面：Agent Swarm 100子Agent</a></li></ol></li><li class="chapter-item expanded "><a href="part2/07-agent-skills.html"><strong aria-hidden="true">3.</strong> Agent Skills</a></li><li class="chapter-item expanded "><a href="part2/08-rlhf.html"><strong aria-hidden="true">4.</strong> RLHF：人类反馈强化学习</a></li><li class="chapter-item expanded "><a href="part2/09-test-time-compute.html"><strong aria-hidden="true">5.</strong> 测试时计算扩展</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">卷三：AI 硬件与芯片</li><li class="chapter-item expanded "><a href="part3/01-nvidia.html"><strong aria-hidden="true">6.</strong> NVIDIA：Rubin + Feynman 双架构</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="part3/01a-feynman.html"><strong aria-hidden="true">6.1.</strong> Feynman：1.6nm + 硅光子 + Groq LPU</a></li><li class="chapter-item "><a href="part3/01b-rubin.html"><strong aria-hidden="true">6.2.</strong> Rubin：HBM4 576GB，2026H2上市</a></li></ol></li><li class="chapter-item expanded "><a href="part3/02-amd.html"><strong aria-hidden="true">7.</strong> AMD MI450：2nm工艺首次反超</a></li><li class="chapter-item expanded "><a href="part3/03-memory.html"><strong aria-hidden="true">8.</strong> 内存技术：HBM与存算一体</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="part3/03a-hbm.html"><strong aria-hidden="true">8.1.</strong> HBM：高带宽内存演进</a></li><li class="chapter-item "><a href="part3/03b-pim.html"><strong aria-hidden="true">8.2.</strong> 存算一体：突破冯·诺依曼瓶颈</a></li><li class="chapter-item "><a href="part3/03c-nmc.html"><strong aria-hidden="true">8.3.</strong> 近存运算：最接近产品化</a></li></ol></li><li class="chapter-item expanded "><a href="part3/04-chiplet.html"><strong aria-hidden="true">9.</strong> Chiplet：芯粒架构</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">卷四：大模型厂商</li><li class="chapter-item expanded "><a href="part4/01-anthropic.html"><strong aria-hidden="true">10.</strong> Anthropic：Claude与Harness领导者</a></li><li class="chapter-item expanded "><a href="part4/02-openai.html"><strong aria-hidden="true">11.</strong> OpenAI：GPT、o系列与开源</a></li><li class="chapter-item expanded "><a href="part4/03-google.html"><strong aria-hidden="true">12.</strong> Google DeepMind：Gemini与TPU</a></li><li class="chapter-item expanded "><a href="part4/04-moonshot.html"><strong aria-hidden="true">13.</strong> 月之暗面：Kimi与Agent Swarm</a></li><li class="chapter-item expanded "><a href="part4/05-deepseek.html"><strong aria-hidden="true">14.</strong> DeepSeek：推理效率与低价策略</a></li><li class="chapter-item expanded "><a href="part4/06-meta.html"><strong aria-hidden="true">15.</strong> Meta：Llama与基础设施</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">卷五：开源与人物</li><li class="chapter-item expanded "><a href="part5/01-ds4.html"><strong aria-hidden="true">16.</strong> ds4：DeepSeek V4 Flash本地推理引擎</a></li><li class="chapter-item expanded "><a href="part5/02-people.html"><strong aria-hidden="true">17.</strong> 值得关注的人物</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded affix "><li class="part-title">附录</li><li class="chapter-item expanded "><a href="appendix/01-llm-wiki-pattern.html"><strong aria-hidden="true">18.</strong> LLM Wiki 知识库模式</a></li><li class="chapter-item expanded "><a href="appendix/02-methodology.html"><strong aria-hidden="true">19.</strong> 本项目信息源与方法论</a></li><li class="chapter-item expanded "><a href="appendix/03-entities-index.html"><strong aria-hidden="true">20.</strong> 完整实体索引</a></li><li class="chapter-item expanded "><a href="appendix/04-concepts-index.html"><strong aria-hidden="true">21.</strong> 完整概念索引</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
