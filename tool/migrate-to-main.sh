#!/usr/bin/env bash
# 仓库结构重构脚本：按 llm-wiki 模式重新组织到 main 分支
set -e

cd /root/.openclaw/workspace/wiki

echo "🗂️  创建新目录结构..."
mkdir -p raw/sessions
mkdir -p site
mkdir -p tool
mkdir -p wiki/sources
mkdir -p wiki/entities
mkdir -p wiki/concepts
mkdir -p wiki/syntheses
mkdir -p wiki/comparisons
mkdir -p wiki/questions
mkdir -p wiki/digest
mkdir -p wiki/weekly-digest
mkdir -p wiki/appendix
mkdir -p wiki/agent-engineering
mkdir -p wiki/hardware
mkdir -p wiki/open-source
mkdir -p wiki/people
mkdir -p wiki/vendors
mkdir -p wiki/knowledge-compiler

echo "📦 迁移外层知识目录 → wiki/..."
mv sources/* wiki/sources/ 2>/dev/null || true
mv entities/* wiki/entities/ 2>/dev/null || true
mv concepts/* wiki/concepts/ 2>/dev/null || true
mv syntheses/* wiki/syntheses/ 2>/dev/null || true
mv comparisons/* wiki/comparisons/ 2>/dev/null || true
mv questions/* wiki/questions/ 2>/dev/null || true
mv knowledge-compiler/* wiki/knowledge-compiler/ 2>/dev/null || true

echo "📦 迁移 src/ 内容 → wiki/..."
for dir in agent-engineering appendix digest hardware open-source people vendors; do
    if [ -d "src/$dir" ] && [ ! -L "src/$dir" ]; then
        cp -r "src/$dir"/* "wiki/$dir/" 2>/dev/null || true
    fi
done
# 复制文件（保留一份在master分支）
cp src/README.md wiki/README.md 2>/dev/null || true
cp src/SUMMARY.md wiki/SUMMARY.md 2>/dev/null || true

echo "📦 迁移 weekly-digest → wiki/..."
mv weekly-digest/* wiki/weekly-digest/ 2>/dev/null || true

echo "📦 迁移构建产物 → site/..."
rm -rf site/*
mv book/* site/ 2>/dev/null || true

echo "📦 迁移脚本 → tool/..."
mv scripts/* tool/ 2>/dev/null || true

echo "🧹 清理旧目录..."
rm -rf sources entities concepts syntheses comparisons questions \
       weekly-digest knowledge-compiler scripts book src

echo "✅ 目录重构完成"
find . -maxdepth 2 -type d | sort | grep -v '.git'
