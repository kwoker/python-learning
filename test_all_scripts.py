#!/usr/bin/env python3
"""
项目综合测试脚本
验证所有学习模块的核心功能
"""

import os
import sys
import subprocess
from pathlib import Path

def run_script(script_path, description):
    """运行脚本并返回结果"""
    print(f"\n{'='*60}")
    print(f"测试: {description}")
    print(f"脚本: {script_path}")
    print('='*60)

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=Path(script_path).parent,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print("✅ 执行成功")
            # 显示最后几行输出
            output_lines = result.stdout.strip().split('\n')
            if output_lines:
                print("\n最后输出:")
                for line in output_lines[-5:]:
                    print(f"  {line}")
            return True
        else:
            print("❌ 执行失败")
            print(f"错误: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("⏱️  执行超时")
        return False
    except Exception as e:
        print(f"❌ 异常: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 开始项目综合测试")
    print("="*60)

    # 测试脚本列表
    test_cases = [
        # Pandas 数据科学模块
        ("projects/data-science/pandas-guide/01_data_loading.py", "Pandas 数据加载"),
        ("projects/data-science/pandas-guide/02_data_cleaning.py", "Pandas 数据清洗"),
        ("projects/data-science/pandas-guide/03_data_analysis.py", "Pandas 数据分析"),
        ("projects/data-science/pandas-guide/04_data_visualization.py", "Pandas 数据可视化"),

        # 基础示例
        ("examples/basics/hello_world.py", "基础示例 - Hello World"),
        ("examples/basics/variables.py", "基础示例 - 变量"),
        ("examples/basics/control_flow.py", "基础示例 - 控制流"),

        # 练习题
        ("exercises/exercise1.py", "练习题 - 基础语法"),

        # 自动化模块
        ("projects/automation/web-scraping/01_basic_scraper.py", "网络爬虫 - 基础"),
        ("projects/automation/web-scraping/02_advanced_scraper.py", "网络爬虫 - 高级"),
    ]

    # 执行测试
    results = []
    for script_path, description in test_cases:
        full_path = Path("/Users/kwok/project/python/test1") / script_path
        if full_path.exists():
            success = run_script(full_path, description)
            results.append((description, success))
        else:
            print(f"\n⚠️  脚本不存在: {script_path}")
            results.append((description, False))

    # 汇总结果
    print("\n" + "="*60)
    print("📊 测试结果汇总")
    print("="*60)

    passed = sum(1 for _, success in results if success)
    total = len(results)

    for description, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"{status:8s} - {description}")

    print(f"\n总计: {passed}/{total} 通过")

    if passed == total:
        print("\n🎉 所有测试通过！项目功能完整！")
        return 0
    else:
        print(f"\n⚠️  有 {total - passed} 个测试失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
