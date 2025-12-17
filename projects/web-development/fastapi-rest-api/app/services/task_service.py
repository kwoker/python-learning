"""
任务服务层
处理业务逻辑
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from app.models.task import Task, TaskCreate, TaskUpdate, TaskStatus, TaskStats


class TaskService:
    """任务服务类"""

    def __init__(self):
        # 内存存储（生产环境应使用数据库）
        self._tasks: Dict[int, Task] = {}
        self._counter = 0

    def create_task(self, task_data: TaskCreate) -> Task:
        """创建任务"""
        self._counter += 1
        now = datetime.now()

        task = Task(
            id=self._counter,
            created_at=now,
            updated_at=now,
            **task_data.dict()
        )

        self._tasks[self._counter] = task
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """获取单个任务"""
        return self._tasks.get(task_id)

    def get_tasks(
        self,
        skip: int = 0,
        limit: int = 10,
        status: Optional[TaskStatus] = None,
        priority: Optional[str] = None
    ) -> List[Task]:
        """获取任务列表"""
        tasks = list(self._tasks.values())

        # 状态筛选
        if status:
            tasks = [t for t in tasks if t.status == status]

        # 优先级筛选
        if priority:
            tasks = [t for t in tasks if t.priority == priority]

        # 排序（按创建时间倒序）
        tasks.sort(key=lambda x: x.created_at, reverse=True)

        # 分页
        return tasks[skip:skip + limit]

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
        """更新任务"""
        task = self._tasks.get(task_id)
        if not task:
            return None

        update_data = task_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)

        task.updated_at = datetime.now()
        self._tasks[task_id] = task
        return task

    def delete_task(self, task_id: int) -> bool:
        """删除任务"""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def get_task_stats(self) -> TaskStats:
        """获取任务统计"""
        tasks = list(self._tasks.values())
        now = datetime.now()

        stats = {
            "total": len(tasks),
            "pending": 0,
            "in_progress": 0,
            "completed": 0,
            "cancelled": 0,
            "overdue": 0
        }

        for task in tasks:
            # 按状态统计
            stats[task.status.value] += 1

            # 逾期统计
            if task.due_date and task.due_date < now and task.status != TaskStatus.COMPLETED:
                stats["overdue"] += 1

        return TaskStats(**stats)


# 创建全局服务实例
task_service = TaskService()
