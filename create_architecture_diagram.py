#!/usr/bin/env python3
"""
脚本用于生成TransformerLSTMModel架构图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_architecture_diagram():
    """创建TransformerLSTMModel架构图"""
    
    # 创建图形和轴
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # 定义颜色方案
    colors = {
        'input': '#E8F4FD',
        'preprocessing': '#D1ECF1', 
        'transformer': '#FFE6CC',
        'lstm': '#D4EDDA',
        'attention': '#F8D7DA',
        'fusion': '#FCF8E3',
        'output': '#F0E6FF'
    }
    
    # 定义组件位置和大小
    components = [
        # (x, y, width, height, text, color_key)
        (4, 1, 2, 0.8, 'Input Data\n[B, L, D]\n[B, 64, 14]', 'input'),
        (3.5, 2.5, 3, 0.8, 'Input Projection & Normalization\nLinear + LayerNorm', 'preprocessing'),
        (3.5, 3.8, 3, 0.8, 'Positional Encoding\nPE(L)', 'preprocessing'),
        (3.5, 5.1, 3, 1.2, 'Transformer Encoder\n3 Layers, 2 Heads\nSelf-Attention', 'transformer'),
        (3.5, 6.8, 3, 1.2, 'Bidirectional LSTM\n2 Layers, 336 Hidden Units', 'lstm'),
        (3.5, 8.5, 3, 1, 'Multi-Head Attention\n2 Heads', 'attention'),
        (1, 9.8, 2.5, 1, 'Original Features\n(Last timestep)', 'preprocessing'),
        (6.5, 9.8, 2.5, 1, 'LSTM Features\n(Last timestep)', 'lstm'),
        (3.5, 10.5, 3, 0.8, 'Feature Fusion\nGating Mechanism', 'fusion'),
        (3.5, 11.5, 3, 0.8, 'Classification\nFC Layers → 12 Classes', 'output')
    ]
    
    # 绘制组件
    boxes = []
    for x, y, w, h, text, color_key in components:
        # 创建圆角矩形
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.1",
            facecolor=colors[color_key],
            edgecolor='black',
            linewidth=1.5
        )
        ax.add_patch(box)
        
        # 添加文本
        ax.text(x + w/2, y + h/2, text, 
               ha='center', va='center', 
               fontsize=10, weight='bold',
               wrap=True)
        
        boxes.append((x + w/2, y, x + w/2, y + h))  # 存储连接点
    
    # 绘制数据流箭头
    arrows = [
        (0, 1),  # Input → Input Projection
        (1, 2),  # Input Projection → Positional Encoding
        (2, 3),  # Positional Encoding → Transformer
        (3, 4),  # Transformer → LSTM
        (4, 5),  # LSTM → Attention
        (5, 7),  # Attention → LSTM Features
        (1, 6),  # Input Projection → Original Features (残差连接)
        (6, 8),  # Original Features → Fusion
        (7, 8),  # LSTM Features → Fusion
        (8, 9),  # Fusion → Classification
    ]
    
    for start_idx, end_idx in arrows:
        if start_idx < len(boxes) and end_idx < len(boxes):
            start_x, start_y_bottom, _, start_y_top = boxes[start_idx]
            end_x, end_y_bottom, _, end_y_top = boxes[end_idx]
            
            # 特殊处理残差连接
            if start_idx == 1 and end_idx == 6:  # 残差连接
                # 绘制弯曲的箭头
                ax.annotate('', xy=(end_x, end_y_bottom), xytext=(start_x - 1.5, start_y_top),
                           arrowprops=dict(arrowstyle='->', lw=2, color='red',
                                         connectionstyle="arc3,rad=0.3"))
                # 添加标签
                ax.text(start_x - 2, (start_y_top + end_y_bottom)/2, 'Residual\nConnection', 
                       ha='center', va='center', fontsize=8, color='red', weight='bold')
            elif start_idx == 6 and end_idx == 8:  # Original Features → Fusion
                ax.annotate('', xy=(end_x - 1, end_y_top), xytext=(start_x, end_y_bottom),
                           arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
            elif start_idx == 7 and end_idx == 8:  # LSTM Features → Fusion
                ax.annotate('', xy=(end_x + 1, end_y_top), xytext=(start_x, end_y_bottom),
                           arrowprops=dict(arrowstyle='->', lw=2, color='green'))
            else:
                # 普通的垂直箭头
                ax.annotate('', xy=(end_x, end_y_bottom), xytext=(start_x, start_y_top),
                           arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # 添加标题
    ax.text(5, 0.3, 'TransformerLSTMModel Architecture for Fault Diagnosis', 
           ha='center', va='center', fontsize=16, weight='bold')
    
    # 添加图例
    legend_elements = [
        patches.Patch(color=colors['input'], label='Input Layer'),
        patches.Patch(color=colors['preprocessing'], label='Preprocessing'),
        patches.Patch(color=colors['transformer'], label='Transformer'),
        patches.Patch(color=colors['lstm'], label='LSTM'),
        patches.Patch(color=colors['attention'], label='Attention'),
        patches.Patch(color=colors['fusion'], label='Feature Fusion'),
        patches.Patch(color=colors['output'], label='Output')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    # 保存图形
    plt.tight_layout()
    plt.savefig('/Users/palmt/Downloads/毕设85精准度/写论文/Thesis/logos/hybrid_architecture.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('/Users/palmt/Downloads/毕设85精准度/写论文/Thesis/logos/hybrid_architecture.pdf', 
                bbox_inches='tight', facecolor='white')
    
    print("架构图已保存为:")
    print("- hybrid_architecture.png")
    print("- hybrid_architecture.pdf")
    
    plt.show()

if __name__ == "__main__":
    create_architecture_diagram()
