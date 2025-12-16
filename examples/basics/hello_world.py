#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World 示例
这是每个编程语言学习的经典第一个程序
"""


def main():
    """主函数：输出 Hello World"""
    # 最简单的输出
    print("Hello, World!")
    print()

    # 使用变量
    message = "Hello, Python!"
    print(message)
    print()

    # 使用函数
    greet("Python 学习者")
    print()

    # 使用格式化字符串
    name = "小明"
    age = 20
    print(f"你好，我叫{name}，今年{age}岁")


def greet(name):
    """问候函数"""
    print(f"你好，{name}！欢迎学习Python！")


if __name__ == "__main__":
    main()
