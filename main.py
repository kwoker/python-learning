#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test1 - Python 学习项目主程序

这是一个学习项目的主入口文件，展示了各种 Python 特性和用法。
"""

from examples.basics.hello_world import main as hello_world
from examples.basics.variables import main as variables_demo
from examples.basics.control_flow import main as control_flow_demo
from examples.oop.basic_class import main as oop_demo
from examples.modules.file_operations import main as file_ops_demo


def main():
    """主函数：运行所有示例"""
    print("=" * 50)
    print("欢迎来到 Python 学习项目 - Test1")
    print("=" * 50)
    print()

    # 运行各个示例
    print("1. Hello World 示例")
    print("-" * 30)
    hello_world()
    print()

    print("2. 变量和数据类型示例")
    print("-" * 30)
    variables_demo()
    print()

    print("3. 控制流示例")
    print("-" * 30)
    control_flow_demo()
    print()

    print("4. 面向对象编程示例")
    print("-" * 30)
    oop_demo()
    print()

    print("5. 文件操作示例")
    print("-" * 30)
    file_ops_demo()
    print()

    print("=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
