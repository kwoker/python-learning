"""
Pandas 数据可视化示例
使用 Matplotlib 和 Seaborn 进行数据可视化
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ============================================================================
# 示例 1: 基础图表
# ============================================================================

def basic_plots():
    """基础图表示例"""
    print("=" * 60)
    print("示例 1: 基础图表")
    print("=" * 60)

    # 创建示例数据
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })

    # 创建图表目录
    Path("output/charts").mkdir(parents=True, exist_ok=True)

    # 折线图
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'])
    plt.title('折线图示例', fontsize=16, pad=20)
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    plt.grid(True, alpha=0.3)
    plt.savefig('output/charts/line_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 折线图已保存: output/charts/line_plot.png")

    # 散点图
    plt.figure(figsize=(10, 6))
    colors = {'A': 'red', 'B': 'blue', 'C': 'green'}
    for category in data['category'].unique():
        subset = data[data['category'] == category]
        plt.scatter(subset['x'], subset['y'], c=colors[category], label=category, alpha=0.6)

    plt.title('散点图示例', fontsize=16, pad=20)
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('output/charts/scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 散点图已保存: output/charts/scatter_plot.png")

    # 柱状图
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    plt.title('柱状图示例', fontsize=16, pad=20)
    plt.xlabel('类别')
    plt.ylabel('数值')

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{int(height)}', ha='center', va='bottom')

    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig('output/charts/bar_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 柱状图已保存: output/charts/bar_plot.png")

    # 直方图
    plt.figure(figsize=(10, 6))
    plt.hist(data['x'], bins=20, color='skyblue', alpha=0.7, edgecolor='black')
    plt.title('直方图示例', fontsize=16, pad=20)
    plt.xlabel('数值')
    plt.ylabel('频次')
    plt.grid(True, alpha=0.3)
    plt.savefig('output/charts/histogram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 直方图已保存: output/charts/histogram.png")

    # 饼图
    plt.figure(figsize=(8, 8))
    sizes = [30, 25, 20, 15, 10]
    labels = ['A', 'B', 'C', 'D', 'E']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    explode = (0.05, 0, 0, 0, 0)  # 突出显示第一块

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('饼图示例', fontsize=16, pad=20)
    plt.axis('equal')
    plt.savefig('output/charts/pie_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 饼图已保存: output/charts/pie_chart.png")


# ============================================================================
# 示例 2: Seaborn 高级图表
# ============================================================================

def seaborn_plots():
    """Seaborn 高级图表示例"""
    print("\n" + "=" * 60)
    print("示例 2: Seaborn 高级图表")
    print("=" * 60)

    # 创建示例数据
    np.random.seed(42)
    df = pd.DataFrame({
        'x': np.random.randn(200),
        'y': np.random.randn(200),
        'category': np.random.choice(['A', 'B', 'C'], 200),
        'size': np.random.randint(10, 100, 200)
    })

    # 箱线图
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='category', y='y')
    plt.title('箱线图示例', fontsize=16, pad=20)
    plt.xlabel('类别')
    plt.ylabel('数值')
    plt.savefig('output/charts/boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 箱线图已保存: output/charts/boxplot.png")

    # 小提琴图
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='category', y='y')
    plt.title('小提琴图示例', fontsize=16, pad=20)
    plt.xlabel('类别')
    plt.ylabel('数值')
    plt.savefig('output/charts/violinplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 小提琴图已保存: output/charts/violinplot.png")

    # 热力图
    plt.figure(figsize=(10, 8))
    # 创建相关性矩阵
    corr_data = np.random.randn(5, 5)
    corr_df = pd.DataFrame(corr_data, columns=['A', 'B', 'C', 'D', 'E'],
                          index=['A', 'B', 'C', 'D', 'E'])

    sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": .8})
    plt.title('热力图示例', fontsize=16, pad=20)
    plt.savefig('output/charts/heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 热力图已保存: output/charts/heatmap.png")

    # 成对关系图
    plt.figure(figsize=(10, 8))
    # 创建数值型数据
    pair_data = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100),
        'category': np.random.choice(['X', 'Y'], 100)
    })

    sns.pairplot(pair_data, hue='category', diag_kind='hist')
    plt.suptitle('成对关系图示例', fontsize=16, y=1.02)
    plt.savefig('output/charts/pairplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 成对关系图已保存: output/charts/pairplot.png")


# ============================================================================
# 示例 3: 多子图布局
# ============================================================================

def subplots_layout():
    """多子图布局示例"""
    print("\n" + "=" * 60)
    print("示例 3: 多子图布局")
    print("=" * 60)

    # 创建示例数据
    np.random.seed(42)
    data = pd.DataFrame({
        'month': range(1, 13),
        'sales': np.random.randint(1000, 5000, 12),
        'profit': np.random.randint(100, 1000, 12),
        'region': np.random.choice(['北京', '上海', '广州'], 12)
    })

    # 2x2 布局
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('多子图布局示例', fontsize=18, y=0.98)

    # 子图1: 折线图
    axes[0, 0].plot(data['month'], data['sales'], marker='o', color='#FF6B6B')
    axes[0, 0].set_title('月度销售额')
    axes[0, 0].set_xlabel('月份')
    axes[0, 0].set_ylabel('销售额')
    axes[0, 0].grid(True, alpha=0.3)

    # 子图2: 柱状图
    axes[0, 1].bar(data['month'], data['profit'], color='#4ECDC4')
    axes[0, 1].set_title('月度利润')
    axes[0, 1].set_xlabel('月份')
    axes[0, 1].set_ylabel('利润')
    axes[0, 1].grid(True, alpha=0.3, axis='y')

    # 子图3: 散点图
    x = np.random.randn(100)
    y = np.random.randn(100)
    axes[1, 0].scatter(x, y, alpha=0.6, color='#45B7D1')
    axes[1, 0].set_title('散点图')
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')
    axes[1, 0].grid(True, alpha=0.3)

    # 子图4: 直方图
    axes[1, 1].hist(x, bins=20, color='#96CEB4', alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('直方图')
    axes[1, 1].set_xlabel('数值')
    axes[1, 1].set_ylabel('频次')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('output/charts/subplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 多子图布局已保存: output/charts/subplots.png")

    # 复杂布局示例
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    # 主图
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(data['month'], data['sales'], marker='o', linewidth=2, markersize=8)
    ax1.set_title('月度销售额趋势', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # 侧边图
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.pie([30, 25, 20, 25], labels=['Q1', 'Q2', 'Q3', 'Q4'], autopct='%1.1f%%')
    ax2.set_title('季度占比')

    ax3 = fig.add_subplot(gs[1, 1])
    region_counts = data['region'].value_counts()
    ax3.bar(region_counts.index, region_counts.values)
    ax3.set_title('地区分布')
    ax3.tick_params(axis='x', rotation=45)

    ax4 = fig.add_subplot(gs[1, 2])
    ax4.hist(np.random.randn(100), bins=20, color='skyblue', alpha=0.7)
    ax4.set_title('分布图')

    # 底部图
    ax5 = fig.add_subplot(gs[2, :])
    ax5.plot(data['month'], data['sales'], label='销售额', marker='o')
    ax5.plot(data['month'], data['profit'], label='利润', marker='s')
    ax5.set_title('销售额与利润对比')
    ax5.set_xlabel('月份')
    ax5.set_ylabel('数值')
    ax5.legend()
    ax5.grid(True, alpha=0.3)

    plt.suptitle('复杂布局示例', fontsize=18, y=0.98)
    plt.savefig('output/charts/complex_layout.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 复杂布局已保存: output/charts/complex_layout.png")


# ============================================================================
# 示例 4: 交互式图表（基础）
# ============================================================================

def interactive_basics():
    """基础交互式图表示例"""
    print("\n" + "=" * 60)
    print("示例 4: 交互式图表")
    print("=" * 60)

    # 创建时间序列数据
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    values = np.cumsum(np.random.randn(100)) + 100

    df = pd.DataFrame({
        'date': dates,
        'value': values
    })

    # Pandas 基础交互图
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['value'], color='#FF6B6B', linewidth=2)
    plt.fill_between(df['date'], df['value'], alpha=0.3, color='#FF6B6B')
    plt.title('带填充的时间序列图', fontsize=16, pad=20)
    plt.xlabel('日期')
    plt.ylabel('数值')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/charts/time_series.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 时间序列图已保存: output/charts/time_series.png")

    # 双轴图
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 第一个轴
    ax1.plot(dates, values, color='#FF6B6B', label='销售额', linewidth=2)
    ax1.set_xlabel('日期')
    ax1.set_ylabel('销售额', color='#FF6B6B')
    ax1.tick_params(axis='y', labelcolor='#FF6B6B')
    ax1.grid(True, alpha=0.3)

    # 第二个轴
    ax2 = ax1.twinx()
    profit_values = np.cumsum(np.random.randn(100)) + 50
    ax2.plot(dates, profit_values, color='#4ECDC4', label='利润', linewidth=2)
    ax2.set_ylabel('利润', color='#4ECDC4')
    ax2.tick_params(axis='y', labelcolor='#4ECDC4')

    plt.title('双轴图表示例', fontsize=16, pad=20)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/charts/dual_axis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 双轴图已保存: output/charts/dual_axis.png")


# ============================================================================
# 示例 5: 实际案例 - 销售数据分析
# ============================================================================

def sales_analysis_case():
    """销售数据分析案例"""
    print("\n" + "=" * 60)
    print("示例 5: 销售数据分析案例")
    print("=" * 60)

    # 创建综合销售数据
    np.random.seed(42)
    regions = ['北京', '上海', '广州', '深圳', '杭州']
    products = ['产品A', '产品B', '产品C', '产品D']
    months = range(1, 13)

    data = []
    for region in regions:
        for product in products:
            for month in months:
                sales = np.random.normal(10000, 3000)
                quantity = np.random.randint(50, 200)
                price = np.random.uniform(100, 500)

                data.append({
                    'region': region,
                    'product': product,
                    'month': month,
                    'sales': sales,
                    'quantity': quantity,
                    'price': price
                })

    df = pd.DataFrame(data)

    # 分析1: 各地区销售额对比
    plt.figure(figsize=(12, 6))
    region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
    bars = plt.bar(region_sales.index, region_sales.values,
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    plt.title('各地区销售额对比', fontsize=16, pad=20)
    plt.xlabel('地区')
    plt.ylabel('销售额')
    plt.xticks(rotation=45)

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1000,
                f'{int(height/1000)}K', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('output/charts/region_sales.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 地区销售额对比图已保存")

    # 分析2: 产品销售额趋势
    plt.figure(figsize=(12, 6))
    for product in products:
        product_monthly = df[df['product'] == product].groupby('month')['sales'].mean()
        plt.plot(product_monthly.index, product_monthly.values,
                marker='o', linewidth=2, label=product)

    plt.title('各产品月度销售额趋势', fontsize=16, pad=20)
    plt.xlabel('月份')
    plt.ylabel('平均销售额')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/charts/product_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 产品趋势图已保存")

    # 分析3: 销售额分布热力图
    plt.figure(figsize=(10, 8))
    pivot_data = df.pivot_table(values='sales', index='region', columns='product', aggfunc='mean')
    sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd',
                linewidths=0.5, cbar_kws={"shrink": .8})
    plt.title('各地区产品销售额热力图', fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig('output/charts/sales_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 销售额热力图已保存")

    print("\n📊 销售数据分析结果:")
    print(f"  总销售额: {df['sales'].sum():,.2f}")
    print(f"  平均销售额: {df['sales'].mean():,.2f}")
    print(f"  最高销售额地区: {region_sales.index[0]}")
    print(f"  销售额最高产品: {df.groupby('product')['sales'].sum().idxmax()}")


if __name__ == "__main__":
    print("\n📈 Pandas 数据可视化示例\n")

    basic_plots()
    seaborn_plots()
    subplots_layout()
    interactive_basics()
    sales_analysis_case()

    print("\n" + "=" * 60)
    print("✅ 所有数据可视化示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 查看 output/charts/ 目录中的图表文件")
    print("2. 修改示例代码，生成自己的图表")
    print("3. 学习 Plotly 或 Bokeh 创建交互式图表")
    print("=" * 60 + "\n")
