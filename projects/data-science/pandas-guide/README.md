# Pandas 数据科学完整指南

> 📊 从零开始学习 Pandas 进行数据分析与可视化

## 🎯 项目简介

这是一个系统化的 Pandas 学习项目，涵盖了数据科学工作流程的各个环节，从数据加载到清洗、分析和可视化。

## 📚 学习内容

### 核心模块

1. **数据加载** (`01_data_loading.py`)
   - CSV、Excel、JSON 文件读取
   - DataFrame 创建方法
   - 数据类型处理
   - 数据保存格式

2. **数据清洗** (`02_data_cleaning.py`)
   - 缺失值处理
   - 重复数据处理
   - 数据类型转换
   - 字符串操作
   - 异常值检测
   - 数据重塑

3. **数据分析** (`03_data_analysis.py`)
   - 描述性统计
   - 分组分析
   - 数据筛选
   - 数据聚合
   - 数据合并
   - 时间序列分析

4. **数据可视化** (`04_data_visualization.py`)
   - Matplotlib 基础图表
   - Seaborn 高级图表
   - 多子图布局
   - 交互式图表
   - 实际案例分析

## 🚀 快速开始

### 安装依赖

```bash
# 安装数据科学相关依赖
pip install -r requirements.txt
```

### 运行示例

```bash
# 1. 学习数据加载
python 01_data_loading.py

# 2. 学习数据清洗
python 02_data_cleaning.py

# 3. 学习数据分析
python 03_data_analysis.py

# 4. 学习数据可视化
python 04_data_visualization.py
```

## 📖 学习路径

### 第一步：基础概念
1. 运行 `01_data_loading.py` 了解 DataFrame 结构
2. 学习不同数据源的加载方法
3. 掌握数据类型和转换

### 第二步：数据清洗
1. 运行 `02_data_cleaning.py`
2. 学习处理真实数据中的问题
3. 掌握数据质量检查方法

### 第三步：数据分析
1. 运行 `03_data_analysis.py`
2. 学习统计分析方法
3. 掌握数据聚合和分组

### 第四步：数据可视化
1. 运行 `04_data_visualization.py`
2. 学习图表类型和选择
3. 掌握可视化最佳实践

## 📊 示例数据

项目会自动生成示例数据：
- `data/employees.csv` - 员工数据
- `data/sales_data.xlsx` - 销售数据
- `data/students.json` - 学生成绩

## 📈 输出文件

运行后会生成：
- `output/data_*.csv` - 数据导出文件
- `output/charts/*.png` - 图表文件
- `output/*.parquet` - 高效存储格式

## 🛠️ 技术栈

- **pandas** - 数据处理和分析
- **numpy** - 数值计算
- **matplotlib** - 基础绘图
- **seaborn** - 统计数据可视化
- **scipy** - 科学计算（统计分析）

## 📝 核心概念

### DataFrame 基础
```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'age': [25, 30, 35],
    'city': ['北京', '上海', '广州']
})

# 查看数据
print(df.head())
print(df.info())
print(df.describe())
```

### 数据筛选
```python
# 条件筛选
filtered = df[df['age'] > 28]

# 多条件筛选
filtered = df[(df['age'] > 25) & (df['city'] == '北京')]

# 分组统计
grouped = df.groupby('city')['age'].mean()
```

### 数据可视化
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 柱状图
plt.figure(figsize=(10, 6))
df['city'].value_counts().plot(kind='bar')
plt.show()

# 散点图
sns.scatterplot(data=df, x='age', y='name', hue='city')
plt.show()
```

## 💡 实战练习

### 练习 1: 销售数据分析
```python
# 加载销售数据
sales_df = pd.read_csv('data/sales.csv')

# 1. 计算各地区总销售额
region_sales = sales_df.groupby('region')['sales'].sum()

# 2. 找出销售额最高的月份
monthly_sales = sales_df.groupby('month')['sales'].sum()
best_month = monthly_sales.idxmax()

# 3. 可视化趋势
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o')
plt.show()
```

### 练习 2: 客户细分分析
```python
# 基于 RFM 模型分析客户
customer_df = pd.read_csv('data/customers.csv')

# 计算 RFM 指标
rfm = customer_df.groupby('customer_id').agg({
    'recency': 'min',      # 最近购买时间
    'frequency': 'sum',    # 购买频次
    'monetary': 'sum'      # 购买金额
})

# 客户细分
rfm['R_score'] = pd.qcut(rfm['recency'], 5, labels=[5,4,3,2,1])
rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_score'] = pd.qcut(rfm['monetary'], 5, labels=[1,2,3,4,5])

# 客户分组
rfm['RFM_Segment'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)
rfm['RFM_Score'] = rfm[['R_score', 'F_score', 'M_score']].sum(axis=1)
```

## 🔍 常见问题

### Q1: 如何处理大数据集？
```python
# 使用分块读取
chunk_list = []
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    chunk_list.append(chunk)
df = pd.concat(chunk_list, ignore_index=True)

# 使用下采样
df_sample = df.sample(n=10000, random_state=42)
```

### Q2: 如何提高性能？
```python
# 指定数据类型
df = pd.read_csv('data.csv', dtype={'id': 'int32', 'value': 'float32'})

# 使用分类数据类型
df['category'] = df['category'].astype('category')

# 使用向量化操作
df['new_col'] = df['col1'] * df['col2']  # 比循环快

# 避免链式索引
df = df.loc[df['condition']]  # 而不是 df[df['condition']]['col']
```

### Q3: 如何处理日期时间？
```python
# 转换为日期类型
df['date'] = pd.to_datetime(df['date'])

# 提取日期特征
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday

# 日期范围
date_range = pd.date_range('2024-01-01', '2024-12-31', freq='D')
```

## 📚 学习资源

### 官方文档
- [Pandas 官方文档](https://pandas.pydata.org/docs/)
- [Matplotlib 教程](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn 教程](https://seaborn.pydata.org/tutorial.html)

### 推荐书籍
- 《利用 Python 进行数据分析》
- 《Python 数据科学手册》
- 《数据科学实战》

### 在线资源
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Pandas 练习题](https://github.com/guipsamora/pandas_exercises)

## 🏆 下一步学习

完成本项目后，建议学习：

1. **高级数据处理**
   - 大数据处理（Dask、Modin）
   - 数据库操作（SQLAlchemy）
   - 数据管道（Apache Airflow）

2. **机器学习**
   - Scikit-learn 基础
   - 特征工程
   - 模型评估

3. **深度学习**
   - TensorFlow/Keras
   - PyTorch
   - 计算机视觉

4. **专业工具**
   - Jupyter Notebook
   - Apache Spark
   - 数据库（PostgreSQL、MongoDB）

## 🤝 贡献

欢迎贡献更多示例和练习！

### 如何贡献
1. Fork 本项目
2. 添加新的示例或练习
3. 完善文档
4. 提交 Pull Request

## 📄 许可证

MIT License

## 👨‍💻 作者

Claude - Anthropic

---

**开始你的数据分析之旅！** 🚀

有问题？查看 [Pandas 官方文档](https://pandas.pydata.org/docs/) 或提交 Issue。
