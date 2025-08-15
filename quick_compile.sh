#!/bin/bash


# 快速编译脚本 - 支持SVG和参考文献
# 使用方法: ./quick_compile.sh

echo "🚀 开始编译含有SVG和参考文献的LaTeX论文..."

cd "/Users/palmt/Downloads/毕设85精准度/写论文/Thesis"

# 运行pdflatex, bibtex, 再运行两次pdflatex以确保所有引用都正确
# --shell-escape 选项是处理SVG所必需的
echo "📝 第一次编译 (pdflatex)..."
pdflatex -shell-escape -interaction=nonstopmode -file-line-error thesis.tex

echo "📚 处理参考文献 (bibtex)..."
bibtex thesis

echo "📝 第二次编译 (pdflatex)..."
pdflatex -shell-escape -interaction=nonstopmode -file-line-error thesis.tex

echo "📝 最终编译 (pdflatex)..."
pdflatex -shell-escape -interaction=nonstopmode -file-line-error thesis.tex

if [ $? -eq 0 ]; then
    echo "✅ 编译成功！论文PDF已更新：thesis.pdf"
    echo "📊 PDF文件信息："
    ls -lh thesis.pdf
    echo "📚 参考文献数量："
    grep "bibitem" thesis.bbl | wc -l
else
    echo "❌ 编译失败"
    echo "📋 检查最后几行日志："
    tail -n 30 thesis.log
fi
