# SyncTeX反向搜索使用指南

## 🎯 功能说明
现在您可以通过点击PDF文档中的内容，直接跳转到对应的LaTeX源文件位置！

## 📱 使用方法

### macOS系统
1. **使用Skim.app**（推荐）
   - 下载安装 [Skim](https://skim-app.sourceforge.io/)
   - 打开 `thesis.pdf`
   - `Cmd+Shift+点击` PDF中的任意位置 → 自动跳转到对应TeX源文件

2. **使用VS Code内置PDF查看器**
   - 在VS Code中打开任意 `.tex` 文件
   - 点击右上角的"打开预览"或使用 `Cmd+Shift+P` → "LaTeX Workshop: View PDF"
   - `Cmd+点击` PDF中的内容 → 跳转到源码

### Windows系统
1. **使用SumatraPDF**（推荐）
   - 下载安装 [SumatraPDF](https://www.sumatrapdfreader.org/)
   - 打开 `thesis.pdf`
   - 双击PDF中的任意位置 → 跳转到对应TeX源文件

2. **使用TeXstudio**
   - 打开 `thesis.pdf`
   - `Ctrl+点击` PDF中的内容 → 跳转到源码

## 🔧 技术细节

### 已配置的文件
- ✅ `thesis.synctex.gz` - SyncTeX同步文件（454KB）
- ✅ `compile_thesis.sh` - 自动启用SyncTeX的编译脚本

### 支持的跳转
- ✅ 章节标题 → 跳转到对应章节的 `.tex` 文件
- ✅ 图表 → 跳转到图表定义位置
- ✅ 公式 → 跳转到公式定义位置
- ✅ 参考文献 → 跳转到 `.bib` 文件中的条目

## 🚀 快速开始
1. 运行 `./compile_thesis.sh synctex` 编译文档
2. 使用支持的PDF查看器打开 `thesis.pdf`\3. 按住对应快捷键点击内容即可跳转！

## 💡 提示
- 如果跳转不准确，重新运行编译脚本
- 保持 `.synctex.gz` 文件与PDF在同一目录
- 使用VS Code的LaTeX Workshop插件可获得最佳体验