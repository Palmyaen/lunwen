#!/bin/bash

# LaTeX论文编译脚本 - 支持反向搜索
# 使用方法: ./compile_thesis.sh [clean|synctex]

if [ "$1" == "clean" ]; then
    echo "🧹 清理所有临时文件..."
    rm -f *.aux *.log *.bbl *.blg *.toc *.out *.lot *.lof *.idx *.ind *.ilg *.synctex.gz chapters/*.aux
    echo "✅ 清理完成！"
    exit 0
fi

echo "🚀 开始编译LaTeX论文..."

# 启用SyncTeX反向搜索
SYNCTEX_FLAG="-synctex=1"

echo "📝 第一次编译 (xelatex + SyncTeX)..."
xelatex $SYNCTEX_FLAG -interaction=nonstopmode thesis.tex

echo "📚 处理参考文献 (bibtex)..."
bibtex thesis

echo "📝 第二次编译 (xelatex)..."
xelatex $SYNCTEX_FLAG -interaction=nonstopmode thesis.tex

echo "📝 第三次编译 (xelatex)..."
xelatex $SYNCTEX_FLAG -interaction=nonstopmode thesis.tex

echo "✅ 编译完成！论文PDF已生成：thesis.pdf"

# 验证SyncTeX文件生成
if [ -f "thesis.synctex.gz" ]; then
    echo "🎯 SyncTeX反向搜索已启用！"
    echo "📍 文件大小：$(ls -lh thesis.synctex.gz | awk '{print $5}')"
    echo "🔍 现在可以在PDF中Cmd+点击跳转到源码！"
else
    echo "⚠️  SyncTeX文件未生成，请检查编译设置"
fi

echo "🎉 全部完成！"