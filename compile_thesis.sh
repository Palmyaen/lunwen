#!/bin/bash

# LaTeX论文编译脚本
# 使用方法: ./compile_thesis.sh [clean]

if [ "$1" == "clean" ]; then
    echo "🧹 清理所有临时文件..."
    rm -f *.aux *.log *.bbl *.blg *.toc *.out *.lot *.lof *.idx *.ind *.ilg *.synctex.gz chapters/*.aux
    echo "✅ 清理完成！"
    exit 0
fi

echo "🚀 开始编译LaTeX论文..."

echo "📝 第一次编译 (pdflatex)..."
pdflatex thesis.tex

echo "📚 处理参考文献 (bibtex)..."
bibtex thesis

echo "📝 第二次编译 (pdflatex)..."
pdflatex thesis.tex

echo "📝 第三次编译 (pdflatex)..."
pdflatex thesis.tex

echo "✅ 编译完成！论文PDF已生成：thesis.pdf"

# 清理临时文件（可选）
echo "🧹 清理临时文件..."
rm -f *.aux *.log *.bbl *.blg *.toc *.out *.lot *.lof chapters/*.aux

echo "🎉 全部完成！"