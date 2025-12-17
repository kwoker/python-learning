"""
Pandas 数据清洗示例
演示常见的数据清洗操作
"""

import pandas as pd
import numpy as np

# ============================================================================
# 示例 1: 处理缺失值
# ============================================================================

def handle_missing_values():
    """处理缺失值的示例"""
    print("=" * 60)
    print("示例 1: 处理缺失值")
    print("=" * 60)

    # 创建包含缺失值的数据
    data = {
        'name': ['张三', '李四', None, '王五', '赵六'],
        'age': [25, None, 35, 28, 32],
        'city': ['北京', '上海', None, '深圳', '杭州'],
        'salary': [8000, 12000, None, 10000, 11000]
    }

    df = pd.DataFrame(data)
    print("原始数据（含缺失值）:")
    print(df)
    print(f"\n缺失值统计:")
    print(df.isnull().sum())

    # 1. 删除包含缺失值的行
    df_dropped = df.dropna()
    print("\n删除缺失值后的数据:")
    print(df_dropped)

    # 2. 用指定值填充缺失值
    df_filled = df.copy()
    df_filled['age'].fillna(df_filled['age'].mean(), inplace=True)
    df_filled['salary'].fillna(0, inplace=True)
    df_filled['name'].fillna('未知', inplace=True)
    df_filled['city'].fillna('未知城市', inplace=True)

    print("\n填充缺失值后的数据:")
    print(df_filled)

    # 3. 前向填充和后向填充
    df_forward = df.fillna(method='ffill')
    print("\n前向填充:")
    print(df_forward)


# ============================================================================
# 示例 2: 处理重复数据
# ============================================================================

def handle_duplicates():
    """处理重复数据的示例"""
    print("\n" + "=" * 60)
    print("示例 2: 处理重复数据")
    print("=" * 60)

    # 创建包含重复数据的数据
    data = {
        'name': ['张三', '李四', '王五', '张三', '李四'],
        'age': [25, 30, 35, 25, 30],
        'city': ['北京', '上海', '广州', '北京', '上海']
    }

    df = pd.DataFrame(data)
    print("原始数据（含重复行）:")
    print(df)

    # 查找重复行
    duplicated = df.duplicated()
    print(f"\n重复行标记:")
    print(duplicated)

    # 删除重复行（保留第一个）
    df_unique = df.drop_duplicates()
    print("\n删除重复行后:")
    print(df_unique)

    # 基于特定列删除重复行
    df_unique_name = df.drop_duplicates(subset=['name'])
    print("\n基于 name 列删除重复:")
    print(df_unique_name)


# ============================================================================
# 示例 3: 数据类型转换
# ============================================================================

def data_type_conversion():
    """数据类型转换示例"""
    print("\n" + "=" * 60)
    print("示例 3: 数据类型转换")
    print("=" * 60)

    # 创建混合类型数据
    data = {
        'int_str': ['1', '2', '3', '4', '5'],
        'float_str': ['1.1', '2.2', '3.3', '4.4', '5.5'],
        'date_str': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'bool_str': ['True', 'False', 'True', 'False', 'True']
    }

    df = pd.DataFrame(data)
    print("原始数据类型:")
    print(df.dtypes)
    print("\n原始数据:")
    print(df)

    # 字符串转整数
    df['int_num'] = df['int_str'].astype('int')
    print("\n转换为整数后:")
    print(df[['int_str', 'int_num']])

    # 字符串转浮点数
    df['float_num'] = df['float_str'].astype('float')
    print("\n转换为浮点数后:")
    print(df[['float_str', 'float_num']])

    # 字符串转日期
    df['date'] = pd.to_datetime(df['date_str'])
    print("\n转换为日期后:")
    print(df[['date_str', 'date']])

    # 字符串转布尔值
    df['bool'] = df['bool_str'].map({'True': True, 'False': False})
    print("\n转换为布尔值后:")
    print(df[['bool_str', 'bool']])


# ============================================================================
# 示例 4: 字符串处理
# ============================================================================

def string_operations():
    """字符串操作示例"""
    print("\n" + "=" * 60)
    print("示例 4: 字符串处理")
    print("=" * 60)

    # 创建包含字符串的数据
    data = {
        'name': ['  张三  ', '李四', 'WANGWU', 'zhaoliu'],
        'email': ['zhang@email.com', 'li@EMAIL.COM', 'wang@email.com', 'zhao@Email.Com'],
        'phone': ['138-0000-0001', '13900000002', '137-0000-0003', '13600000004']
    }

    df = pd.DataFrame(data)
    print("原始数据:")
    print(df)

    # 去除空格
    df['name_clean'] = df['name'].str.strip()
    print("\n去除空格后:")
    print(df[['name', 'name_clean']])

    # 转换大小写
    df['name_upper'] = df['name_clean'].str.upper()
    df['name_lower'] = df['name_clean'].str.lower()
    print("\n大小写转换:")
    print(df[['name_clean', 'name_upper', 'name_lower']])

    # 邮箱标准化（小写）
    df['email_clean'] = df['email'].str.lower()
    print("\n邮箱标准化:")
    print(df[['email', 'email_clean']])

    # 字符串替换
    df['phone_clean'] = df['phone'].str.replace('-', '')
    print("\n去除连字符:")
    print(df[['phone', 'phone_clean']])

    # 字符串分割
    df['phone_prefix'] = df['phone_clean'].str[:3]
    df['phone_suffix'] = df['phone_clean'].str[-4:]
    print("\n字符串分割:")
    print(df[['phone', 'phone_prefix', 'phone_suffix']])


# ============================================================================
# 示例 5: 异常值检测与处理
# ============================================================================

def handle_outliers():
    """异常值检测与处理示例"""
    print("\n" + "=" * 60)
    print("示例 5: 异常值检测与处理")
    print("=" * 60)

    # 创建包含异常值的数据
    np.random.seed(42)
    data = {
        'score': np.concatenate([
            np.random.normal(70, 10, 100),  # 正常分数
            [150, 160, 170, -20, -30]      # 异常值
        ])
    }

    df = pd.DataFrame(data)
    print("分数数据统计:")
    print(df['score'].describe())

    # 使用 IQR 方法检测异常值
    Q1 = df['score'].quantile(0.25)
    Q3 = df['score'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"\nIQR 范围: [{lower_bound:.2f}, {upper_bound:.2f}]")

    # 标记异常值
    df['is_outlier'] = (df['score'] < lower_bound) | (df['score'] > upper_bound)
    outliers = df[df['is_outlier']]
    print(f"\n检测到 {len(outliers)} 个异常值:")
    print(outliers)

    # 删除异常值
    df_clean = df[~df['is_outlier']]
    print(f"\n删除异常值后剩余 {len(df_clean)} 条记录")

    # 使用 Z-score 方法
    from scipy import stats
    df['z_score'] = np.abs(stats.zscore(df['score']))
    df['is_outlier_z'] = df['z_score'] > 3
    outliers_z = df[df['is_outlier_z']]
    print(f"\nZ-score 方法检测到 {len(outliers_z)} 个异常值")


# ============================================================================
# 示例 6: 数据重塑
# ============================================================================

def reshape_data():
    """数据重塑示例"""
    print("\n" + "=" * 60)
    print("示例 6: 数据重塑")
    print("=" * 60)

    # 创建宽格式数据
    data = {
        'name': ['张三', '李四', '王五'],
        'math': [90, 85, 92],
        'english': [88, 90, 87],
        'physics': [85, 88, 90]
    }

    df_wide = pd.DataFrame(data)
    print("宽格式数据:")
    print(df_wide)

    # 宽格式转长格式 (melt)
    df_long = pd.melt(
        df_wide,
        id_vars=['name'],
        value_vars=['math', 'english', 'physics'],
        var_name='subject',
        value_name='score'
    )
    print("\n长格式数据:")
    print(df_long)

    # 长格式转宽格式 (pivot)
    df_wide_again = df_long.pivot(
        index='name',
        columns='subject',
        values='score'
    ).reset_index()
    df_wide_again.columns.name = None  # 移除列名索引
    print("\n重新转换为宽格式:")
    print(df_wide_again)


if __name__ == "__main__":
    print("\n🧹 Pandas 数据清洗示例\n")

    handle_missing_values()
    handle_duplicates()
    data_type_conversion()
    string_operations()
    handle_outliers()
    reshape_data()

    print("\n" + "=" * 60)
    print("✅ 所有数据清洗示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 运行 03_data_analysis.py 学习数据分析")
    print("2. 结合实际数据集进行清洗练习")
    print("=" * 60 + "\n")
