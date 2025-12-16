#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习题 1：基础语法
"""

def exercise_1_1():
    """练习 1.1：计算器
    编写一个函数，接受两个数字和一个运算符（+、-、*、/），
    返回计算结果。
    """
    def calculator(a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b != 0:
                return a / b
            else:
                return "错误：除数不能为零"
        else:
            return "错误：无效的运算符"

    # 测试用例
    print("=== 练习 1.1：计算器 ===")
    print(calculator(10, 5, '+'))  # 应该输出 15
    print(calculator(10, 5, '-'))  # 应该输出 5
    print(calculator(10, 5, '*'))  # 应该输出 50
    print(calculator(10, 5, '/'))  # 应该输出 2.0
    print()


def exercise_1_2():
    """练习 1.2：列表操作
    编写函数处理列表：
    1. 返回列表中的最大值和最小值
    2. 计算列表的平均值
    3. 返回列表中所有偶数
    """
    def list_operations(numbers):
        if not numbers:
            return {"max": None, "min": None, "average": None, "evens": []}

        return {
            "max": max(numbers),
            "min": min(numbers),
            "average": sum(numbers) / len(numbers),
            "evens": [x for x in numbers if x % 2 == 0]
        }

    # 测试用例
    print("=== 练习 1.2：列表操作 ===")
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list_operations(test_list)
    print(f"原列表: {test_list}")
    print(f"最大值: {result['max']}")
    print(f"最小值: {result['min']}")
    print(f"平均值: {result['average']}")
    print(f"偶数: {result['evens']}")
    print()


def exercise_1_3():
    """练习 1.3：字符串处理
    编写函数统计字符串中的：
    1. 字符总数
    2. 单词总数（以空格分隔）
    3. 每个字符出现的次数
    """
    def string_stats(text):
        # 字符总数
        char_count = len(text)

        # 单词总数（以空格分隔）
        words = text.split()
        word_count = len(words)

        # 字符频率统计
        char_frequency = {}
        for char in text:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        return {
            "char_count": char_count,
            "word_count": word_count,
            "char_frequency": char_frequency
        }

    # 测试用例
    print("=== 练习 1.3：字符串处理 ===")
    test_string = "Hello World! Python is awesome."
    stats = string_stats(test_string)
    print(f"字符串: {test_string}")
    print(f"字符总数: {stats['char_count']}")
    print(f"单词总数: {stats['word_count']}")
    print("字符频率:")
    for char, count in stats['char_frequency'].items():
        print(f"  '{char}': {count}")
    print()


def exercise_1_4():
    """练习 1.4：回文检查
    编写函数检查一个字符串是否是回文（正读和反读都一样）
    """
    def is_palindrome(text):
        # 移除空格并转为小写进行比较
        cleaned = ''.join(text.lower().split())
        # 检查是否与反转后的字符串相等
        return cleaned == cleaned[::-1]

    # 测试用例
    print("=== 练习 1.4：回文检查 ===")
    test_cases = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "12321"
    ]

    for text in test_cases:
        result = is_palindrome(text)
        print(f"'{text}' 是回文吗？{result}")
    print()


def exercise_1_5():
    """练习 1.5：斐波那契数列
    编写函数返回斐波那契数列的前 n 项
    """
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        # 初始化前两项
        fib = [0, 1]
        # 生成后续的项
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    # 测试用例
    print("=== 练习 1.5：斐波那契数列 ===")
    for i in [5, 10, 15]:
        sequence = fibonacci(i)
        print(f"前 {i} 项: {sequence}")
    print()


def main():
    """运行所有练习"""
    print("=" * 50)
    print("Python 基础语法练习题")
    print("=" * 50)
    print()

    # 运行每个练习
    exercise_1_1()
    exercise_1_2()
    exercise_1_3()
    exercise_1_4()
    exercise_1_5()

    print("=" * 50)
    print("所有练习题完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
