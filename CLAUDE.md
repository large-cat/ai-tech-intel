ai-tech-intel/
├── raw/              # 只读 — 调研原始资料（URL、引用、原始摘录）
│   └── urls.md       # 待调研/已调研 URL 列表
├── wiki/             # LLM 读写 — 生成的知识页
│   ├── README.md     # wiki 首页
│   ├── sources/      # 源文件摘要
│   ├── entities/     # 实体档案
│   ├── concepts/     # 技术概念
│   ├── syntheses/    # 综合综述
│   ├── comparisons/  # 对比分析
│   └── questions/    # 知识问答
├── site/             # 只读 — mdBook 构建产物（CI 自动生成，不提交）
├── tool/             # 读写 — 构建工具与脚本
│   └── build.sh      # mdbook build 包装脚本
├── book.toml         # mdBook 配置
├── .github/workflows/# GitHub Actions
├── .gitignore
├── README.md         # 项目总览
└── CLAUDE.md         # LLM 工作指引
