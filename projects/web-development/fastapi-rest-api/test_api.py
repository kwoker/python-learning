"""
FastAPI API 测试示例
使用 requests 测试 API 端点
"""

import requests
import json
from typing import Dict, Any

# API 基础 URL
BASE_URL = "http://localhost:8000/api/v1"


def test_root():
    """测试根路径"""
    print("=" * 60)
    print("测试 1: 根路径")
    print("=" * 60)

    response = requests.get(f"{BASE_URL}/")
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_health():
    """测试健康检查"""
    print("\n" + "=" * 60)
    print("测试 2: 健康检查")
    print("=" * 60)

    response = requests.get(f"{BASE_URL}/health")
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_create_task():
    """测试创建任务"""
    print("\n" + "=" * 60)
    print("测试 3: 创建任务")
    print("=" * 60)

    task_data = {
        "title": "完成项目报告",
        "description": "撰写第三季度项目总结报告",
        "status": "pending",
        "priority": "high",
        "due_date": "2024-12-31T23:59:59"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=task_data)
    print(f"状态码: {response.status_code}")

    if response.status_code == 201:
        task = response.json()
        print(f"创建的任务 ID: {task['id']}")
        print(f"任务标题: {task['title']}")
        return task['id']
    else:
        print(f"错误: {response.text}")
        return None


def test_get_tasks():
    """测试获取任务列表"""
    print("\n" + "=" * 60)
    print("测试 4: 获取任务列表")
    print("=" * 60)

    response = requests.get(f"{BASE_URL}/tasks")
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"总任务数: {data['total']}")
        print(f"当前页: {data['page']}")
        print(f"每页数量: {data['page_size']}")
        print("\n任务列表:")
        for task in data['items']:
            print(f"  - ID: {task['id']}, 标题: {task['title']}, 状态: {task['status']}")


def test_get_task(task_id: int):
    """测试获取单个任务"""
    print("\n" + "=" * 60)
    print(f"测试 5: 获取任务 {task_id}")
    print("=" * 60)

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        task = response.json()
        print(f"任务信息:")
        print(f"  ID: {task['id']}")
        print(f"  标题: {task['title']}")
        print(f"  描述: {task['description']}")
        print(f"  状态: {task['status']}")
        print(f"  优先级: {task['priority']}")
        print(f"  创建时间: {task['created_at']}")


def test_update_task(task_id: int):
    """测试更新任务"""
    print("\n" + "=" * 60)
    print(f"测试 6: 更新任务 {task_id}")
    print("=" * 60)

    update_data = {
        "status": "in_progress",
        "description": "更新：正在撰写报告，已完成50%"
    }

    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        task = response.json()
        print(f"更新成功!")
        print(f"  新状态: {task['status']}")
        print(f"  新描述: {task['description']}")


def test_complete_task(task_id: int):
    """测试完成任务"""
    print("\n" + "=" * 60)
    print(f"测试 7: 完成任务 {task_id}")
    print("=" * 60)

    response = requests.post(f"{BASE_URL}/tasks/{task_id}/complete")
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        task = response.json()
        print(f"任务已完成! 状态: {task['status']}")


def test_get_stats():
    """测试获取统计信息"""
    print("\n" + "=" * 60)
    print("测试 8: 获取任务统计")
    print("=" * 60)

    response = requests.get(f"{BASE_URL}/tasks/stats")
    print(f"状态码: {response.status_code}")

    if response.status_code == 200:
        stats = response.json()
        print("任务统计:")
        print(f"  总任务数: {stats['total']}")
        print(f"  待处理: {stats['pending']}")
        print(f"  进行中: {stats['in_progress']}")
        print(f"  已完成: {stats['completed']}")
        print(f"  已取消: {stats['cancelled']}")
        print(f"  逾期任务: {stats['overdue']}")


def test_delete_task(task_id: int):
    """测试删除任务"""
    print("\n" + "=" * 60)
    print(f"测试 9: 删除任务 {task_id}")
    print("=" * 60)

    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    print(f"状态码: {response.status_code}")

    if response.status_code == 204:
        print("任务删除成功!")


def test_filter_tasks():
    """测试任务筛选"""
    print("\n" + "=" * 60)
    print("测试 10: 任务筛选")
    print("=" * 60)

    # 按状态筛选
    response = requests.get(f"{BASE_URL}/tasks?status=pending")
    print(f"\n待处理任务 (状态=pending):")
    if response.status_code == 200:
        data = response.json()
        print(f"  数量: {data['total']}")

    # 按优先级筛选
    response = requests.get(f"{BASE_URL}/tasks?priority=high")
    print(f"\n高优先级任务 (priority=high):")
    if response.status_code == 200:
        data = response.json()
        print(f"  数量: {data['total']}")

    # 分页
    response = requests.get(f"{BASE_URL}/tasks?page=1&page_size=5")
    print(f"\n分页测试 (page=1, page_size=5):")
    if response.status_code == 200:
        data = response.json()
        print(f"  当前页: {data['page']}")
        print(f"  每页数量: {data['page_size']}")
        print(f"  总页数: {data['pages']}")


def main():
    """主测试函数"""
    print("\n🚀 FastAPI REST API 测试\n")

    # 启动服务器提示
    print("⚠️  请确保 API 服务器已启动:")
    print("   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    print()

    try:
        # 基础测试
        test_root()
        test_health()

        # 任务 CRUD 测试
        task_id = test_create_task()
        if task_id:
            test_get_tasks()
            test_get_task(task_id)
            test_update_task(task_id)
            test_complete_task(task_id)

        # 高级功能测试
        test_get_stats()
        test_filter_tasks()

        # 清理测试数据
        if task_id:
            test_delete_task(task_id)

        print("\n" + "=" * 60)
        print("✅ 所有测试完成!")
        print("=" * 60)

    except requests.exceptions.ConnectionError:
        print("\n❌ 无法连接到 API 服务器")
        print("请先启动服务器:")
        print("python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {str(e)}")


if __name__ == "__main__":
    main()
