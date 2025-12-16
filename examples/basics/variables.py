#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
变量和数据类型示例
演示 Python 中的各种数据类型
"""


def main():
    """演示各种数据类型"""
    # 数字类型
    print("=== 数字类型 ===")
    integer_num = 42522
    float_num = 3.14159
    complex_num = 3 + 4j

    print(f"整数: {integer_num} (类型: {type(integer_num).__name__})")
    print(f"浮点数: {float_num} (类型: {type(float_num).__name__})")
    print(f"复数: {complex_num} (类型: {type(complex_num).__name__})")
    print()

    # 字符串类型
    print("=== 字符串类型 ===")
    single_quote = '单引号字符串'
    double_quote = "双引号字符串"
    multiline_string = """
    这是一个
    多行字符串
    """

    print(f"单引号: {single_quote}")
    print(f"双引号: {double_quote}")
    print(f"多行字符串: {multiline_string}")
    print()

    # 字符串操作
    text = "Python"
    print(f"字符串长度: {len(text)}")
    print(f"大写: {text.upper()}")
    print(f"小写: {text.lower()}")
    print(f"切片 [1:4]: {text[1:4]}")
    print()

    # 布尔类型
    print("=== 布尔类型 ===")
    is_student = True
    has_license = False

    print(f"是学生: {is_student}")
    print(f"有驾照: {has_license}")
    print(f"逻辑与: {is_student and has_license}")
    print(f"逻辑或: {is_student or has_license}")
    print()

    # 列表类型
    print("=== 列表类型 ===")
    numbers = [1, 2, 3, 4, 5]
    mixed_list = ["苹果", 3, True, 3.14]

    print(f"数字列表: {numbers}")
    print(f"混合列表: {mixed_list}")
    print(f"第一个元素: {numbers[0]}")
    print(f"最后一个元素: {numbers[-1]}")
    print(f"列表长度: {len(numbers)}")
    print()

    # 列表操作
    numbers.append(6)
    print(f"添加元素后: {numbers}")
    numbers.remove(3)
    print(f"删除元素后: {numbers}")
    print()

    # 元组类型
    print("=== 元组类型 ===")
    coordinates = (10, 20)
    person = ("张三", 25, "北京")

    print(f"坐标: {coordinates}")
    print(f"人员信息: {person}")
    print(f"X坐标: {coordinates[0]}")
    print()

    # 字典类型
    print("=== 字典类型 ===")
    student = {
        "姓名": "李四",
        "年龄": 22,
        "专业": "计算机科学",
        "成绩": [85, 90, 78]
    }

    print(f"学生信息: {student}")
    print(f"姓名: {student['姓名']}")
    print(f"年龄: {student['年龄']}")
    print()

    # 字典操作
    student["城市"] = "上海"
    print(f"添加城市后: {student}")
    print()

    # 集合类型
    print("=== 集合类型 ===")
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    print(f"交集: {set1 & set2}")
    print(f"并集: {set1 | set2}")
    print(f"差集: {set1 - set2}")
    print()


if __name__ == "__main__":
    main()
