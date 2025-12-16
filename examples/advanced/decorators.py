#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器示例
演示 Python 中的装饰器用法
"""

import time
from functools import wraps


def timer_decorator(func):
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {execution_time:.4f} 秒")
        return result
    return wrapper


def logging_decorator(func):
    """日志装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper


def repeat_decorator(times):
    """重复执行装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


class CountCalls:
    """计数装饰器类"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)


@timer_decorator
@logging_decorator
def slow_function():
    """一个慢函数"""
    time.sleep(1)
    return "函数执行完成"


@repeat_decorator(3)
def greet(name):
    """问候函数"""
    return f"你好, {name}!"


@CountCalls
def simple_function():
    """简单函数"""
    return "执行"


def main():
    """演示各种装饰器"""
    print("=== 装饰器示例 ===\n")

    # 组合装饰器
    print("1. 组合装饰器（计时 + 日志）")
    result = slow_function()
    print(f"结果: {result}\n")

    # 参数化装饰器
    print("2. 参数化装饰器（重复执行）")
    results = greet("Python")
    print(f"结果: {results}\n")

    # 类装饰器
    print("3. 类装饰器（计数）")
    simple_function()
    simple_function()
    simple_function()
    print()

    # 手动应用装饰器
    print("4. 手动应用装饰器")
    def plain_function(x, y):
        return x + y

    decorated = logging_decorator(plain_function)
    result = decorated(5, 3)
    print(f"结果: {result}\n")


if __name__ == "__main__":
    main()
