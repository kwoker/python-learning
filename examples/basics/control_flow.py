#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
控制流示例
演示 if、for、while 等控制流语句
"""


def main():
    """演示各种控制流语句"""
    # 条件语句
    print("=== 条件语句 ===")
    check_number(10)
    check_number(-5)
    check_number(0)
    print()

    # 循环
    print("=== for 循环 ===")
    print("打印 1-5:")
    for i in range(1, 6):
        print(f"  {i}")
    print()

    print("遍历列表:")
    fruits = ["苹果", "香蕉", "橙子"]
    for fruit in fruits:
        print(f"  我喜欢 {fruit}")
    print()

    # enumerate 示例
    print("使用 enumerate:")
    for index, fruit in enumerate(fruits, 1):
        print(f"  {index}. {fruit}")
    print()

    # while 循环
    print("=== while 循环 ===")
    count = 1
    while count <= 3:
        print(f"  计数: {count}")
        count += 1
    print()

    # 循环控制
    print("=== 循环控制（break 和 continue）===")
    print("使用 break（找到第一个偶数就停止）:")
    for i in range(1, 10):
        if i % 2 == 0:
            print(f"  找到偶数: {i}")
            break
        print(f"  检查: {i}")
    print()

    print("使用 continue（跳过奇数）:")
    for i in range(1, 6):
        if i % 2 == 1:
            continue
        print(f"  偶数: {i}")
    print()

    # 嵌套循环
    print("=== 嵌套循环 ===")
    print("打印乘法表（1-3）:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"  {i} x {j} = {i * j}")
    print()

    # 列表推导式
    print("=== 列表推导式 ===")
    numbers = [1, 2, 3, 4, 5]
    squares = [x ** 2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]

    print(f"原列表: {numbers}")
    print(f"平方: {squares}")
    print(f"偶数: {evens}")
    print()

    # 字典推导式
    print("=== 字典推导式 ===")
    square_dict = {x: x ** 2 for x in range(1, 6)}
    print(f"平方字典: {square_dict}")
    print()

    # try-except
    print("=== 异常处理 ===")
    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide("10", "2")
    print()


def check_number(num):
    """检查数字的正负性"""
    if num > 0:
        print(f"  {num} 是正数")
    elif num < 0:
        print(f"  {num} 是负数")
    else:
        print(f"  {num} 是零")


def safe_divide(a, b):
    """安全的除法运算"""
    try:
        result = a / b
        print(f"  {a} / {b} = {result}")
    except TypeError:
        print(f"  类型错误：无法计算 {a} / {b}")
    except ZeroDivisionError:
        print(f"  错误：除数不能为零")
    except Exception as e:
        print(f"  未知错误：{e}")


if __name__ == "__main__":
    main()
