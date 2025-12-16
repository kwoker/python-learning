#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作示例
演示如何读写文件和目录操作
"""

import os
import json
import csv
from pathlib import Path


def main():
    """演示文件操作"""
    # 文件路径
    test_file = "data/test.txt"
    json_file = "data/data.json"
    csv_file = "data/data.csv"

    # 创建 data 目录（如果不存在）
    os.makedirs("data", exist_ok=True)

    # 写入文本文件
    print("=== 写入文本文件 ===")
    write_text_file(test_file, "这是第一行\n这是第二行\n这是第三行")
    print(f"已写入文件: {test_file}")

    # 读取文本文件
    print("\n=== 读取文本文件 ===")
    content = read_text_file(test_file)
    print(f"文件内容:\n{content}")

    # 逐行读取
    print("\n=== 逐行读取 ===")
    lines = read_lines(test_file)
    for i, line in enumerate(lines, 1):
        print(f"第 {i} 行: {line.strip()}")

    # 写入 JSON 文件
    print("\n=== 写入 JSON 文件 ===")
    data = {
        "name": "张三",
        "age": 25,
        "skills": ["Python", "JavaScript", "Java"],
        "is_student": False
    }
    write_json_file(json_file, data)
    print(f"已写入 JSON 文件: {json_file}")

    # 读取 JSON 文件
    print("\n=== 读取 JSON 文件 ===")
    loaded_data = read_json_file(json_file)
    print(f"加载的数据: {loaded_data}")

    # 写入 CSV 文件
    print("\n=== 写入 CSV 文件 ===")
    csv_data = [
        ["姓名", "年龄", "城市"],
        ["张三", "25", "北京"],
        ["李四", "30", "上海"],
        ["王五", "28", "广州"]
    ]
    write_csv_file(csv_file, csv_data)
    print(f"已写入 CSV 文件: {csv_file}")

    # 读取 CSV 文件
    print("\n=== 读取 CSV 文件 ===")
    loaded_csv = read_csv_file(csv_file)
    print("CSV 数据:")
    for row in loaded_csv:
        print(f"  {row}")

    # 获取文件信息
    print("\n=== 文件信息 ===")
    file_info(test_file)

    # 列出目录内容
    print("\n=== 目录内容 ===")
    list_directory("data")

    # 清理测试文件
    print("\n=== 清理测试文件 ===")
    cleanup_files([test_file, json_file, csv_file])
    print("测试文件已清理")


def write_text_file(filename, content):
    """写入文本文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def read_text_file(filename):
    """读取文本文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def read_lines(filename):
    """逐行读取文件"""
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
    return lines


def write_json_file(filename, data):
    """写入 JSON 文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_json_file(filename):
    """读取 JSON 文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_csv_file(filename, data):
    """写入 CSV 文件"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def read_csv_file(filename):
    """读取 CSV 文件"""
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def file_info(filename):
    """获取文件信息"""
    if os.path.exists(filename):
        stat = os.stat(filename)
        print(f"文件: {filename}")
        print(f"  大小: {stat.st_size} 字节")
        print(f"  修改时间: {stat.st_mtime}")
        print(f"  是否文件: {os.path.isfile(filename)}")
        print(f"  是否目录: {os.path.isdir(filename)}")


def list_directory(dirname):
    """列出目录内容"""
    if os.path.exists(dirname):
        print(f"目录: {dirname}")
        for item in os.listdir(dirname):
            path = os.path.join(dirname, item)
            if os.path.isfile(path):
                print(f"  [文件] {item}")
            elif os.path.isdir(path):
                print(f"  [目录] {item}/")
    else:
        print(f"目录 {dirname} 不存在")


def cleanup_files(filenames):
    """清理测试文件"""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"已删除: {filename}")


if __name__ == "__main__":
    main()
