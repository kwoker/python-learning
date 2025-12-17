"""
Pandas 数据分析示例
演示基本的数据分析操作
"""

import pandas as pd
import numpy as np

# ============================================================================
# 示例 1: 描述性统计
# ============================================================================

def descriptive_statistics():
    """描述性统计示例"""
    print("=" * 60)
    print("示例 1: 描述性统计")
    print("=" * 60)

    # 创建示例销售数据
    np.random.seed(42)
    data = {
        'product': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'region': np.random.choice(['北京', '上海', '广州', '深圳'], 100),
        'sales': np.random.normal(10000, 3000, 100),
        'quantity': np.random.randint(10, 100, 100),
        'price': np.random.uniform(50, 200, 100)
    }

    df = pd.DataFrame(data)
    print("数据预览:")
    print(df.head())
    print(f"\n数据形状: {df.shape}")

    # 数值列的描述性统计
    print("\n数值列统计:")
    print(df.describe())

    # 单列统计
    print(f"\n销售额统计:")
    print(f"  平均值: {df['sales'].mean():.2f}")
    print(f"  中位数: {df['sales'].median():.2f}")
    print(f"  标准差: {df['sales'].std():.2f}")
    print(f"  最小值: {df['sales'].min():.2f}")
    print(f"  最大值: {df['sales'].max():.2f}")

    # 分类列统计
    print(f"\n产品分布:")
    print(df['product'].value_counts())

    print(f"\n地区分布:")
    print(df['region'].value_counts())


# ============================================================================
# 示例 2: 分组分析
# ============================================================================

def group_analysis():
    """分组分析示例"""
    print("\n" + "=" * 60)
    print("示例 2: 分组分析")
    print("=" * 60)

    # 使用上面的数据
    np.random.seed(42)
    data = {
        'product': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'region': np.random.choice(['北京', '上海', '广州', '深圳'], 100),
        'sales': np.random.normal(10000, 3000, 100),
        'quantity': np.random.randint(10, 100, 100),
    }

    df = pd.DataFrame(data)

    # 按产品分组
    print("按产品分组统计:")
    product_stats = df.groupby('product').agg({
        'sales': ['mean', 'sum', 'count'],
        'quantity': ['mean', 'sum']
    }).round(2)

    print(product_stats)

    # 按地区和产品双重分组
    print("\n按地区和产品分组统计:")
    region_product_stats = df.groupby(['region', 'product'])['sales'].mean().round(2)
    print(region_product_stats)

    # 透视表
    print("\n销售额透视表:")
    pivot_table = df.pivot_table(
        values='sales',
        index='region',
        columns='product',
        aggfunc='mean'
    ).round(2)
    print(pivot_table)


# ============================================================================
# 示例 3: 数据筛选
# ============================================================================

def data_filtering():
    """数据筛选示例"""
    print("\n" + "=" * 60)
    print("示例 3: 数据筛选")
    print("=" * 60)

    # 创建示例数据
    df = pd.DataFrame({
        'name': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
        'age': [25, 30, 35, 28, 32, 26],
        'salary': [8000, 12000, 15000, 10000, 11000, 9000],
        'department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT'],
        'city': ['北京', '上海', '广州', '深圳', '杭州', '北京']
    })

    print("原始数据:")
    print(df)

    # 单一条件筛选
    print("\n筛选年龄 > 28 的员工:")
    age_filter = df[df['age'] > 28]
    print(age_filter)

    # 多条件筛选（AND）
    print("\n筛选 IT 部门且薪资 > 10000 的员工:")
    it_high_salary = df[(df['department'] == 'IT') & (df['salary'] > 10000)]
    print(it_high_salary)

    # 多条件筛选（OR）
    print("\n筛选北京或上海地区的员工:")
    beijing_shanghai = df[(df['city'] == '北京') | (df['city'] == '上海')]
    print(beijing_shanghai)

    # 使用 isin()
    print("\n筛选张三、李四、王五:")
    specific_names = df[df['name'].isin(['张三', '李四', '王五'])]
    print(specific_names)

    # 使用 str.contains()
    print("\n筛选姓名包含 '三' 或 '四' 的员工:")
    name_contains = df[df['name'].str.contains('三|四')]
    print(name_contains)

    # 排序
    print("\n按薪资降序排序:")
    sorted_by_salary = df.sort_values('salary', ascending=False)
    print(sorted_by_salary)


# ============================================================================
# 示例 4: 数据聚合
# ============================================================================

def data_aggregation():
    """数据聚合示例"""
    print("\n" + "=" * 60)
    print("示例 4: 数据聚合")
    print("=" * 60)

    # 创建销售数据
    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30),
        'product': np.random.choice(['A', 'B', 'C'], 30),
        'sales': np.random.randint(1000, 5000, 30),
        'region': np.random.choice(['北京', '上海', '广州'], 30)
    })

    print("销售数据示例:")
    print(df.head(10))

    # 时间聚合
    print("\n按月聚合:")
    df['month'] = df['date'].dt.to_period('M')
    monthly_sales = df.groupby('month')['sales'].sum()
    print(monthly_sales)

    # 多级聚合
    print("\n按产品和地区聚合:")
    multi_agg = df.groupby(['product', 'region']).agg({
        'sales': ['sum', 'mean', 'count']
    }).round(2)
    print(multi_agg)

    # 使用 agg() 自定义聚合
    print("\n自定义聚合函数:")
    custom_agg = df.groupby('product')['sales'].agg([
        'sum',
        'mean',
        'min',
        'max',
        'std'
    ]).round(2)
    print(custom_agg)


# ============================================================================
# 示例 5: 数据合并
# ============================================================================

def data_merging():
    """数据合并示例"""
    print("\n" + "=" * 60)
    print("示例 5: 数据合并")
    print("=" * 60)

    # 创建两个表
    employees = pd.DataFrame({
        'emp_id': [1, 2, 3, 4, 5],
        'name': ['张三', '李四', '王五', '赵六', '钱七'],
        'dept_id': [101, 102, 101, 103, 102]
    })

    departments = pd.DataFrame({
        'dept_id': [101, 102, 103],
        'dept_name': ['IT部', '人事部', '销售部'],
        'manager': ['张经理', '李经理', '王经理']
    })

    print("员工表:")
    print(employees)
    print("\n部门表:")
    print(departments)

    # 内连接 (INNER JOIN)
    print("\n内连接:")
    inner_join = pd.merge(employees, departments, on='dept_id', how='inner')
    print(inner_join)

    # 左连接 (LEFT JOIN)
    print("\n左连接:")
    left_join = pd.merge(employees, departments, on='dept_id', how='left')
    print(left_join)

    # 外连接 (OUTER JOIN)
    print("\n外连接:")
    outer_join = pd.merge(employees, departments, on='dept_id', how='outer')
    print(outer_join)

    # 追加数据 (APPEND)
    new_employees = pd.DataFrame({
        'emp_id': [6, 7],
        'name': ['孙八', '周九'],
        'dept_id': [101, 104]
    })

    print("\n追加新员工:")
    all_employees = pd.concat([employees, new_employees], ignore_index=True)
    print(all_employees)


# ============================================================================
# 示例 6: 时间序列分析
# ============================================================================

def time_series_analysis():
    """时间序列分析示例"""
    print("\n" + "=" * 60)
    print("示例 6: 时间序列分析")
    print("=" * 60)

    # 创建时间序列数据
    dates = pd.date_range('2024-01-01', periods=365, freq='D')
    np.random.seed(42)
    sales = 1000 + np.cumsum(np.random.randn(365) * 10)

    df = pd.DataFrame({
        'date': dates,
        'sales': sales
    })

    print("时间序列数据示例:")
    print(df.head(10))

    # 设置日期为索引
    df.set_index('date', inplace=True)

    # 重采样 - 按月汇总
    print("\n按月汇总销售额:")
    monthly_sales = df.resample('M').sum()
    print(monthly_sales.head())

    # 移动平均
    print("\n7天移动平均:")
    df['ma_7'] = df['sales'].rolling(window=7).mean()
    print(df[['sales', 'ma_7']].head(10))

    # 同比环比
    print("\n月度销售额:")
    monthly = df.resample('M').sum()
    monthly['prev_month'] = monthly['sales'].shift(1)
    monthly['mom_change'] = ((monthly['sales'] - monthly['prev_month']) / monthly['prev_month'] * 100).round(2)
    print(monthly.head())


if __name__ == "__main__":
    print("\n📊 Pandas 数据分析示例\n")

    descriptive_statistics()
    group_analysis()
    data_filtering()
    data_aggregation()
    data_merging()
    time_series_analysis()

    print("\n" + "=" * 60)
    print("✅ 所有数据分析示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 运行 04_data_visualization.py 学习数据可视化")
    print("2. 使用自己的数据集进行分析练习")
    print("3. 结合实际业务场景进行数据分析")
    print("=" * 60 + "\n")
