#!/usr/bin/env python3
"""
AI Tech Intel 知识编译器 v2 (Knowledge Compiler)
基于 llm-wiki 模式，智能识别内容引用关系
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

WIKI_ROOT = Path("/root/.openclaw/workspace/wiki")
OUTPUT_DIR = WIKI_ROOT / "knowledge-compiler"

# 实体别名映射
ENTITY_ALIASES = {
    "andrej-karpathy": ["karpathy", "andrej karpathy", "karpathy's"],
    "anthropic": ["anthropic", "claude", "claude 3", "claude 4"],
    "openai": ["openai", "gpt", "gpt-4", "gpt-5", "chatgpt", "o3", "o4"],
    "google-deepmind": ["google", "deepmind", "gemini", "alphabet"],
    "nvidia": ["nvidia", "geforce", "cuda", "hopper", "blackwell", "feynman", "rubin"],
    "amd": ["amd", "mi300", "mi400", "mi450", "ryzen"],
    "samsung": ["samsung", "三星"],
    "sk-hynix": ["sk hynix", "sk海力士", "sk-hynix"],
    "intel": ["intel", "英特尔", "gaudi"],
    "micron": ["micron", "美光"],
    "tsmc": ["tsmc", "台积电"],
    "stripe": ["stripe", "minions"],
    "moonshot": ["moonshot", "月之暗面", "kimi"],
    "deepseek": ["deepseek", "deep seek"],
    "meta": ["meta", "llama", "facebook"],
    "langchain": ["langchain", "lang graph"],
    "addy-osmani": ["addy osmani", "osmani"],
    "antirez": ["antirez", "salvatore sanfilippo", "redis"],
    "pratiyush": ["pratiyush", "llm-wiki"],
}

# 概念别名映射
CONCEPT_ALIASES = {
    "harness-methodology": ["harness", "agent harness", "harness engineering", "agentic engineering"],
    "agent-skills": ["agent skills", "agent skill", "skills"],
    "rlhf": ["rlhf", "dpo", "ppo", "grpo", "ipo", "kto", "human feedback"],
    "test-time-compute": ["test-time compute", "test time compute", "ttc", "reasoning time"],
    "processing-in-memory": ["processing in memory", "pim", "存算一体"],
    "near-memory-computing": ["near memory computing", "near-memory", "近存运算", "近存计算"],
    "hbm": ["hbm", "high bandwidth memory", "高带宽内存"],
    "chiplet": ["chiplet", "芯粒", "芯粒架构"],
    "advanced-packaging": ["advanced packaging", "先进封装", "cowos", "emib", "foveros"],
    "ds4": ["ds4", "deepseek v4 flash"],
    "llm-wiki-pattern": ["llm wiki", "karpathy pattern", "知识库模式"],
}

def extract_title(content):
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"

def extract_summary(content, max_len=200):
    clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    paragraphs = [p.strip() for p in clean.split('\n\n') if p.strip() and not p.startswith('#')]
    if paragraphs:
        s = paragraphs[0][:max_len]
        return s + "..." if len(paragraphs[0]) > max_len else s
    return ""

def find_references(content, aliases_dict):
    """在内容中查找别名匹配，返回匹配到的 key 列表"""
    found = set()
    content_lower = content.lower()
    for key, aliases in aliases_dict.items():
        for alias in aliases:
            # 用单词边界匹配，避免 partial match
            pattern = r'\b' + re.escape(alias.lower()) + r'\b'
            if re.search(pattern, content_lower):
                found.add(key)
                break
    return list(found)

def build_enhanced_graph():
    graph = {
        "entities": {},
        "concepts": {},
        "sources": {},
        "cross_refs": []
    }
    
    # 加载实体
    entities_path = WIKI_ROOT / "entities"
    if entities_path.exists():
        for f in entities_path.glob("*.md"):
            content = f.read_text(encoding='utf-8')
            name = f.stem
            graph["entities"][name] = {
                "title": extract_title(content),
                "path": str(f.relative_to(WIKI_ROOT)),
                "sources": [],
                "concepts": []
            }
    
    # 加载概念
    concepts_path = WIKI_ROOT / "concepts"
    if concepts_path.exists():
        for f in concepts_path.glob("*.md"):
            content = f.read_text(encoding='utf-8')
            name = f.stem
            graph["concepts"][name] = {
                "title": extract_title(content),
                "path": str(f.relative_to(WIKI_ROOT)),
                "sources": []
            }
    
    # 扫描来源，智能识别引用
    sources_path = WIKI_ROOT / "sources"
    if sources_path.exists():
        for f in sources_path.glob("*.md"):
            content = f.read_text(encoding='utf-8')
            name = f.stem
            title = extract_title(content)
            summary = extract_summary(content)
            
            # 显式 wikilinks
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
            
            # 智能识别实体引用
            entity_refs = find_references(content, ENTITY_ALIASES)
            # 智能识别概念引用
            concept_refs = find_references(content, CONCEPT_ALIASES)
            
            graph["sources"][name] = {
                "title": title,
                "path": str(f.relative_to(WIKI_ROOT)),
                "summary": summary,
                "wikilinks": wikilinks,
                "entities": entity_refs,
                "concepts": concept_refs
            }
            
            # 建立反向引用
            for entity in entity_refs:
                if entity in graph["entities"]:
                    if name not in graph["entities"][entity]["sources"]:
                        graph["entities"][entity]["sources"].append(name)
                    graph["cross_refs"].append({
                        "from": f"sources/{name}",
                        "to": f"entities/{entity}",
                        "type": "mentions"
                    })
            
            for concept in concept_refs:
                if concept in graph["concepts"]:
                    if name not in graph["concepts"][concept]["sources"]:
                        graph["concepts"][concept]["sources"].append(name)
                    graph["cross_refs"].append({
                        "from": f"sources/{name}",
                        "to": f"concepts/{concept}",
                        "type": "mentions"
                    })
    
    return graph

def generate_knowledge_index(graph):
    lines = [
        "# 知识编译索引 (Knowledge Compiler Index)",
        "",
        f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 版本 v2.0",
        "> 基于 llm-wiki 模式：sources → entities → concepts → syntheses → comparisons → questions",
        "",
        "## 📚 目录结构（知识树骨架）",
        "",
        "```",
        "wiki/",
        "├── sources/          # 原始资料来源",
        "├── entities/         # 实体档案",
        "├── concepts/         # 技术概念",
        "├── syntheses/        # 综合综述",
        "├── comparisons/      # 对比分析",
        "├── questions/        # 知识问答（中文Q&A）",
        "├── digest/           # 每日速递",
        "├── weekly-digest/    # 每周摘要",
        "├── knowledge-compiler/  # 知识编译输出",
        "│   ├── index.md      # 本索引",
        "│   ├── graph.jsonld  # 机器可读图谱",
        "│   └── stats.json    # 统计数据",
        "└── src/              # mdBook 阅读层",
        "```",
        "",
        "## 🔗 交叉引用映射（目录 → 内容页码）",
        "",
        "### 实体档案被引用来源",
        "",
    ]
    
    for entity_name, info in sorted(graph["entities"].items()):
        sources = info.get("sources", [])
        lines.append(f"#### {info['title']} (`{info['path']}`)")
        lines.append("")
        if sources:
            lines.append(f"**被 {len(sources)} 篇来源引用：**")
            for src in sources:
                src_info = graph["sources"].get(src, {})
                src_title = src_info.get("title", src)
                lines.append(f"- [{src_title}]({src_info.get('path', f'sources/{src}.md')})")
        else:
            lines.append("*暂无来源引用 — 待完善*")
        lines.append("")
    
    lines.append("---")
    lines.append("### 技术概念被引用来源")
    lines.append("")
    
    for concept_name, info in sorted(graph["concepts"].items()):
        sources = info.get("sources", [])
        lines.append(f"#### {info['title']} (`{info['path']}`)")
        lines.append("")
        if sources:
            lines.append(f"**被 {len(sources)} 篇来源引用：**")
            for src in sources:
                src_info = graph["sources"].get(src, {})
                src_title = src_info.get("title", src)
                lines.append(f"- [{src_title}]({src_info.get('path', f'sources/{src}.md')})")
        else:
            lines.append("*暂无来源引用 — 待完善*")
        lines.append("")
    
    lines.append("---")
    lines.append("## 📊 统计概览")
    lines.append("")
    total_entity_refs = sum(len(e.get("sources",[])) for e in graph["entities"].values())
    total_concept_refs = sum(len(c.get("sources",[])) for c in graph["concepts"].values())
    lines.append(f"| 类别 | 数量 | 被引用次数 |")
    lines.append(f"|------|------|------------|")
    lines.append(f"| 实体 (entities) | {len(graph['entities'])} | {total_entity_refs} |")
    lines.append(f"| 概念 (concepts) | {len(graph['concepts'])} | {total_concept_refs} |")
    lines.append(f"| 来源 (sources) | {len(graph['sources'])} | — |")
    lines.append(f"| 交叉引用 | — | {len(graph['cross_refs'])} |")
    lines.append("")
    lines.append("---")
    lines.append("## 🧭 如何使用本索引")
    lines.append("")
    lines.append("1. **查找实体/概念**：上方按字母排序的实体和概念列表")
    lines.append("2. **追溯来源**：每个实体/概念下方列出引用它的 sources/ 文件")
    lines.append("3. **发现空白**：标记为「暂无来源引用」的条目 = 知识缺口，可通过提问触发补充")
    lines.append("4. **机器查询**：读取 `graph.jsonld` 获取结构化数据")
    lines.append("")
    lines.append("---")
    lines.append("*本索引随知识库增长自动更新。运行 `python3 scripts/knowledge_compiler.py` 重新编译。*")
    
    return "\n".join(lines)

def generate_jsonld(graph):
    nodes = []
    edges = []
    
    for name, info in graph["entities"].items():
        nodes.append({
            "@id": f"entity:{name}",
            "@type": "Organization" if name in ["anthropic","openai","google-deepmind","nvidia","amd","samsung","sk-hynix","intel","micron","tsmc","stripe","moonshot","deepseek","meta","langchain"] else "Person",
            "name": info["title"],
            "path": info["path"],
            "source_count": len(info.get("sources", []))
        })
    
    for name, info in graph["concepts"].items():
        nodes.append({
            "@id": f"concept:{name}",
            "@type": "TechConcept",
            "name": info["title"],
            "path": info["path"],
            "source_count": len(info.get("sources", []))
        })
    
    for name, info in graph["sources"].items():
        nodes.append({
            "@id": f"source:{name}",
            "@type": "TechArticle",
            "name": info["title"],
            "path": info["path"],
            "summary": info.get("summary", "")
        })
    
    for ref in graph["cross_refs"]:
        edges.append({
            "from": ref["from"].replace("/", ":"),
            "to": ref["to"].replace("/", ":"),
            "type": ref.get("type", "references")
        })
    
    return {
        "@context": {
            "schema": "https://schema.org",
            "aiti": "https://large-cat.github.io/ai-tech-intel/"
        },
        "@graph": {
            "project": "ai-tech-intel",
            "version": "2.0.0",
            "generated": datetime.now().isoformat(),
            "nodes": nodes,
            "edges": edges
        }
    }

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("🔍 扫描知识库文件...")
    print("🧠 智能识别内容引用关系...")
    graph = build_enhanced_graph()
    
    print("📑 生成知识编译索引...")
    index_md = generate_knowledge_index(graph)
    (OUTPUT_DIR / "index.md").write_text(index_md, encoding='utf-8')
    
    print("🌐 生成机器可读图谱...")
    jsonld = generate_jsonld(graph)
    (OUTPUT_DIR / "graph.jsonld").write_text(
        json.dumps(jsonld, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    
    stats = {
        "generated_at": datetime.now().isoformat(),
        "version": "2.0.0",
        "entities": len(graph["entities"]),
        "concepts": len(graph["concepts"]),
        "sources": len(graph["sources"]),
        "cross_references": len(graph["cross_refs"]),
        "entity_refs": sum(len(e.get("sources",[])) for e in graph["entities"].values()),
        "concept_refs": sum(len(c.get("sources",[])) for c in graph["concepts"].values())
    }
    (OUTPUT_DIR / "stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    
    print(f"✅ 知识编译完成！")
    print(f"   📄 {OUTPUT_DIR}/index.md — 人类可读索引")
    print(f"   🌐 {OUTPUT_DIR}/graph.jsonld — 机器可读图谱")
    print(f"   📊 {OUTPUT_DIR}/stats.json — 统计摘要")
    print(f"   🔗 交叉引用: {len(graph['cross_refs'])} 条")
    print(f"   📊 实体被引用: {stats['entity_refs']} 次")
    print(f"   📊 概念被引用: {stats['concept_refs']} 次")

if __name__ == "__main__":
    main()
