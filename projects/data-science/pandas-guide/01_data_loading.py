"""
Pandas 数据加载示例
演示如何从不同数据源加载数据
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================================
# 示例 1: 从 CSV 文件加载数据
# ============================================================================

def load_csv_example():
    """从 CSV 文件加载数据的示例"""
    print("=" * 60)
    print("示例 1: 从 CSV 加载数据")
    print("=" * 60)

    # 创建示例 CSV 数据
    sample_data = {
        'name': ['张三', '李四', '王五', '赵六', '钱七'],
        'age': [25, 30, 35, 28, 32],
        'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'salary': [8000, 12000, 15000, 10000, 11000]
    }

    # 保存为 CSV
    df_sample = pd.DataFrame(sample_data)
    csv_path = "data/employees.csv"
    df_sample.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"✓ 已创建示例 CSV 文件: {csv_path}")

    # 加载 CSV 数据
    df = pd.read_csv(csv_path)
    print("\n加载的数据:")
    print(df)
    print(f"\n数据形状: {df.shape}")
    print(f"列名: {list(df.columns)}")

    # 指定数据类型和编码
    df_utf8 = pd.read_csv(csv_path, encoding='utf-8')
    print("\n使用 UTF-8 编码加载:")


# ============================================================================
# 示例 2: 从 Excel 文件加载数据
# ============================================================================

def load_excel_example():
    """从 Excel 文件加载数据的示例"""
    print("\n" + "=" * 60)
    print("示例 2: 从 Excel 加载数据")
    print("=" * 60)

    # 创建示例数据
    data = {
        'product': ['A', 'B', 'C', 'D', 'E'],
        'sales_q1': [100, 150, 120, 180, 200],
        'sales_q2': [110, 160, 130, 190, 210],
        'sales_q3': [105, 155, 125, 185, 205],
        'sales_q4': [115, 165, 135, 195, 215]
    }

    df = pd.DataFrame(data)
    excel_path = "data/sales_data.xlsx"
    df.to_excel(excel_path, index=False)
    print(f"✓ 已创建示例 Excel 文件: {excel_path}")

    # 加载 Excel 数据
    df_loaded = pd.read_excel(excel_path, sheet_name=0)
    print("\n加载的 Excel 数据:")
    print(df_loaded)

    # 加载指定工作表
    # df_sheet = pd.read_excel(excel_path, sheet_name='Sheet1')


# ============================================================================
# 示例 3: 从 JSON 文件加载数据
# ============================================================================

def load_json_example():
    """从 JSON 文件加载数据的示例"""
    print("\n" + "=" * 60)
    print("示例 3: 从 JSON 加载数据")
    print("=" * 60)

    # 创建嵌套 JSON 数据
    json_data = [
        {"name": "张三", "scores": {"math": 90, "english": 85, "physics": 88}},
        {"name": "李四", "scores": {"math": 75, "english": 92, "physics": 80}},
        {"name": "王五", "scores": {"math": 85, "english": 78, "physics": 92}}
    ]

    # 保存 JSON
    import json
    json_path = "data/students.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"✓ 已创建示例 JSON 文件: {json_path}")

    # 加载 JSON 数据
    df_json = pd.read_json(json_path, encoding='utf-8')
    print("\n加载的 JSON 数据:")
    print(df_json)

    # 处理嵌套 JSON
    print("\n处理嵌套 JSON (展开 scores 列):")
    df_normalized = pd.json_normalize(json_data)
    print(df_normalized)


# ============================================================================
# 示例 4: 从字典创建 DataFrame
# ============================================================================

def create_dataframe_from_dict():
    """从字典创建 DataFrame"""
    print("\n" + "=" * 60)
    print("示例 4: 从字典创建 DataFrame")
    print("=" * 60)

    # 方法 1: 使用字典列表
    data_list = [
        {'name': 'A', 'value': 1, 'category': 'X'},
        {'name': 'B', 'value': 2, 'category': 'Y'},
        {'name': 'C', 'value': 3, 'category': 'Z'}
    ]
    df1 = pd.DataFrame(data_list)
    print("方法 1 - 字典列表:")
    print(df1)

    # 方法 2: 使用列字典
    data_dict = {
        'name': ['A', 'B', 'C'],
        'value': [1, 2, 3],
        'category': ['X', 'Y', 'Z']
    }
    df2 = pd.DataFrame(data_dict)
    print("\n方法 2 - 列字典:")
    print(df2)

    # 方法 3: 从二维数组
    data_array = [
        ['A', 1, 'X'],
        ['B', 2, 'Y'],
        ['C', 3, 'Z']
    ]
    df3 = pd.DataFrame(data_array, columns=['name', 'value', 'category'])
    print("\n方法 3 - 二维数组:")
    print(df3)


# ============================================================================
# 示例 5: 数据保存
# ============================================================================

def save_data_examples():
    """数据保存示例"""
    print("\n" + "=" * 60)
    print("示例 5: 数据保存")
    print("=" * 60)

    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    })

    # 保存为 CSV
    df.to_csv('output/data_export.csv', index=False, encoding='utf-8')
    print("✓ 已保存为 CSV: output/data_export.csv")

    # 保存为 Excel
    df.to_excel('output/data_export.xlsx', index=False)
    print("✓ 已保存为 Excel: output/data_export.xlsx")

    # 保存为 JSON
    df.to_json('output/data_export.json', orient='records', force_ascii=False, indent=2)
    print("✓ 已保存为 JSON: output/data_export.json")

    # 保存为 Parquet（高效格式）
    df.to_parquet('output/data_export.parquet')
    print("✓ 已保存为 Parquet: output/data_export.parquet")


# ============================================================================
# 示例 6: 数据类型处理
# ============================================================================

def data_types_example():
    """数据类型处理示例"""
    print("\n" + "=" * 60)
    print("示例 6: 数据类型处理")
    print("=" * 60)

    # 创建混合类型数据
    df = pd.DataFrame({
        'int_col': [1, 2, 3],
        'float_col': [1.1, 2.2, 3.3],
        'str_col': ['a', 'b', 'c'],
        'bool_col': [True, False, True],
        'date_col': ['2024-01-01', '2024-01-02', '2024-01-03']
    })

    print("原始数据类型:")
    print(df.dtypes)

    # 转换数据类型
    df['int_col'] = df['int_col'].astype('int64')
    df['float_col'] = df['float_col'].astype('float32')
    df['str_col'] = df['str_col'].astype('string')
    df['bool_col'] = df['bool_col'].astype('bool')
    df['date_col'] = pd.to_datetime(df['date_col'])

    print("\n转换后数据类型:")
    print(df.dtypes)

    # 检查内存使用
    print("\n内存使用情况:")
    print(df.memory_usage(deep=True))


if __name__ == "__main__":
    print("\n📊 Pandas 数据加载示例\n")

    # 确保目录存在
    Path("data").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

    load_csv_example()
    load_excel_example()
    load_json_example()
    create_dataframe_from_dict()
    save_data_examples()
    data_types_example()

    print("\n" + "=" * 60)
    print("✅ 所有数据加载示例完成！")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 运行 02_data_cleaning.py 了解数据清洗")
    print("2. 运行 03_data_analysis.py 学习数据分析")
    print("3. 查看 output/ 目录中的输出文件")
    print("=" * 60 + "\n")
