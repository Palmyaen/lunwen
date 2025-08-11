# 混合Transformer-LSTM工业故障诊断系统项目文档

## 项目概述

### 项目标题
基于混合Transformer-LSTM架构的工业设备故障诊断系统

### 项目背景
在工业4.0快速发展的背景下，智能制造系统广泛应用，工业设备故障诊断已成为现代预测性维护策略的核心。本项目旨在开发一个创新的混合深度学习架构，结合Transformer和LSTM网络的互补优势，解决传统故障诊断方法的局限性。

### 核心问题
传统故障诊断方法面临的主要挑战：
1. **长期时间依赖关系**：工业故障通过长时间演化的细微变化表现出来
2. **类别不平衡**：正常运行数据远多于故障数据
3. **多尺度时间模式**：从高频振动到低频操作循环的复杂行为
4. **不同操作条件下的泛化**：在不同负载和环境因素下保持性能

## 技术架构

### 混合神经网络架构
```
输入数据 → Transformer组件 → 特征融合 → LSTM组件 → 输出分类
                ↓                ↓               ↓
        全局注意力机制    自适应融合策略    序列记忆能力
```

#### Transformer组件
- **功能**：采用自注意力机制捕获全局依赖关系
- **优势**：并行处理能力，从多维传感器数据中高效提取特征
- **实现**：多头注意力、位置编码、前馈神经网络

#### LSTM组件
- **功能**：利用循环连接建模序列依赖关系
- **优势**：维护历史模式记忆，分析故障演化过程
- **实现**：双向LSTM、门控机制、梯度裁剪

#### 融合策略
- **自适应权重分配**：动态调整Transformer和LSTM输出的权重
- **特征级融合**：在特征层面结合两种架构的表示
- **决策级融合**：在最终预测阶段整合结果

### 关键技术创新

#### 1. 长期依赖建模
- **问题**：传统LSTM在处理长序列时的梯度消失，标准Transformer在时间故障演化序列性方面的局限
- **解决方案**：
  - 利用Transformer注意力机制识别长序列中的相关时间点
  - 运用LSTM记忆能力维护时间故障演化的连续性
  - 实现自适应注意力权重，聚焦故障相关时间区域

#### 2. 类别不平衡缓解
- **高级数据增强技术**：专为时间序列故障数据设计
- **焦点损失实现**：强调稀有故障类别的学习
- **集成学习策略**：提高少数类检测能力

#### 3. 多尺度时间分析
- **多分辨率输入处理**：捕获不同时间尺度的模式
- **分层特征提取**：从细粒度到粗粒度的时间表示
- **跨尺度注意力机制**：识别不同时间层次间的相关性

## 数据集信息

### 主要数据集
```
Dataset_1/
├── ALL_processed.csv          # 所有类型故障的综合数据
├── BACKLASH_X_processed.csv   # X轴反冲故障数据
├── BACKLASH_Y_processed.csv   # Y轴反冲故障数据
├── BS_X_processed.csv         # X轴基线偏移故障
├── BS_XY_processed.csv        # XY轴基线偏移故障
├── BS_Y_processed.csv         # Y轴基线偏移故障
├── JERK_A_processed.csv       # A轴抖动故障
├── JERK_ALL_processed.csv     # 所有轴抖动故障
├── JERK_B_processed.csv       # B轴抖动故障
├── JERK_X_processed.csv       # X轴抖动故障
├── JERK_Y_processed.csv       # Y轴抖动故障
└── good_1.csv, good_2.csv, good_3.csv  # 正常运行数据
```

### 故障类型
1. **反冲故障 (BACKLASH)**：机械间隙导致的位置偏差
2. **基线偏移故障 (BS - Baseline Shift)**：传感器基线漂移
3. **抖动故障 (JERK)**：运动控制中的突然加速度变化

## 模型性能

### 当前成果
- **准确度**：82-85%（根据目录名称推断）
- **模型保存**：多个训练阶段的快照和最佳模型
- **评估指标**：包含详细的性能指标JSON文件

### 训练框架
```
model/
├── best_model.pth              # 最佳性能模型
├── final_model.pth             # 最终训练模型
├── transformer_lstm/           # 基础Transformer-LSTM模型
├── transformer_lstm_optimized/ # 优化版本模型
└── backup_**/                  # 版本控制备份
```

## 代码结构

### 核心文件
1. **main_merged_good_final.py**：主要训练和评估脚本
2. **models.py**：神经网络架构定义
3. **data_utils_merged_good.py**：数据处理和预处理
4. **train_utils_merged_good.py**：训练工具和函数
5. **visualization.py**：结果可视化

### 辅助工具
- **evaluate_model.py**：模型评估
- **generate_report.py**：性能报告生成
- **backup_model.py**：模型备份管理
- **run_tuning.py**：超参数调优

## 实验设置

### 数据预处理流程
1. **噪声减少**：滤波和平滑处理
2. **归一化**：标准化传感器数据
3. **特征选择**：相关性分析和降维
4. **时间窗口分割**：序列数据分段

### 训练策略
1. **优化器**：Adam优化器，自适应学习率调度
2. **正则化**：Dropout、权重衰减
3. **早停机制**：防止过拟合
4. **检查点保存**：定期保存训练状态

### 评估指标
- **准确率 (Accuracy)**
- **精确率 (Precision)**
- **召回率 (Recall)**
- **F1分数**
- **ROC-AUC**
- **混淆矩阵**

## 可视化和报告

### 生成的图表
```
imgs/
├── 归一化混淆矩阵.png
├── 混淆矩阵图.png
├── class_distribution_merged.png
├── class_distribution.png
├── confusion_matrix.png
├── learning_curve.png
├── normalized_confusion_matrix.png
└── ROC_PR_Curves.png
```

### 报告内容
- **性能对比分析**
- **学习曲线**
- **类别分布统计**
- **ROC和PR曲线**

## 部署考虑

### 计算效率
- **模型压缩**：减少参数数量
- **推理优化**：加速预测过程
- **内存管理**：高效资源利用

### 实时处理能力
- **流式数据处理**
- **低延迟预测**
- **在线学习适应**

## 项目配置

### 环境要求
- Python 3.x
- PyTorch
- NumPy, Pandas
- Scikit-learn
- Matplotlib, Seaborn

### 配置文件
- **config.json**：模型超参数
- **performance_metrics.json**：性能指标记录

## 研究贡献

### 理论贡献
1. **新颖的混合架构**：首次将Transformer和LSTM有效结合用于工业故障诊断
2. **自适应融合机制**：动态权重分配策略
3. **多尺度时间建模**：跨时间尺度的特征学习

### 实践价值
1. **工业应用**：可直接部署到实际生产环境
2. **性能提升**：相比传统方法显著改善
3. **可扩展性**：适用于不同类型的工业设备

## 未来工作方向

### 短期目标
1. **进一步优化融合策略**
2. **扩展到更多故障类型**
3. **实时系统部署测试**

### 长期目标
1. **无监督学习集成**
2. **联邦学习应用**
3. **边缘计算优化**

## 使用说明

### 快速开始
```bash
# 训练模型
python main_merged_good_final.py

# 评估模型
python evaluate_model.py

# 生成报告
python generate_report.py

# 可视化结果
python visualization.py
```

### 自定义配置
1. 修改数据路径在 `data_utils_merged_good.py`
2. 调整模型参数在 `models.py`
3. 更改训练设置在主脚本中

## 关键文献引用

1. **Vaswani et al. (2017)**: "Attention is All You Need" - Transformer架构基础
2. **Hochreiter & Schmidhuber (1997)**: "Long Short-Term Memory" - LSTM网络原理
3. **Chen et al. (2017)**: Industry 4.0技术综述
4. **Zhang et al. (2019)**: 深度学习在旋转机械故障诊断中的应用
5. **Zhao et al. (2019)**: 深度学习在机器健康监测中的应用

## 联系信息

- **项目类型**：硕士学位论文研究
- **研究领域**：工业人工智能、故障诊断、深度学习
- **技术栈**：PyTorch, Python, 机器学习

---

**注意**：本文档提供了项目的全面概述，包含所有关键技术细节和实现要点。任何AI系统都可以基于此文档快速理解项目的核心内容、技术架构和研究贡献。
