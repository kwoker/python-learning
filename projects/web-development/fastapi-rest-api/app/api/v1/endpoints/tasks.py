"""
任务 API 端点
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Depends
from app.models.task import Task, TaskCreate, TaskUpdate, TaskList, TaskStats, TaskStatus
from app.services.task_service import task_service

router = APIRouter()


@router.post("/tasks", response_model=Task, status_code=201, tags=["任务管理"])
async def create_task(task: TaskCreate):
    """创建新任务"""
    try:
        created_task = task_service.create_task(task)
        return created_task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建任务失败: {str(e)}")


@router.get("/tasks", response_model=TaskList, tags=["任务管理"])
async def get_tasks(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    status: Optional[TaskStatus] = Query(None, description="任务状态筛选"),
    priority: Optional[str] = Query(None, description="优先级筛选")
):
    """获取任务列表"""
    try:
        skip = (page - 1) * page_size
        tasks = task_service.get_tasks(
            skip=skip,
            limit=page_size,
            status=status,
            priority=priority
        )
        total = len(task_service.get_tasks())

        return TaskList(
            items=tasks,
            total=total,
            page=page,
            page_size=page_size,
            pages=(total + page_size - 1) // page_size
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取任务列表失败: {str(e)}")


@router.get("/tasks/{task_id}", response_model=Task, tags=["任务管理"])
async def get_task(task_id: int):
    """获取单个任务"""
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task


@router.put("/tasks/{task_id}", response_model=Task, tags=["任务管理"])
async def update_task(task_id: int, task_update: TaskUpdate):
    """更新任务"""
    task = task_service.update_task(task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task


@router.delete("/tasks/{task_id}", status_code=204, tags=["任务管理"])
async def delete_task(task_id: int):
    """删除任务"""
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="任务不存在")
    return {"message": "任务删除成功"}


@router.get("/tasks/stats", response_model=TaskStats, tags=["任务统计"])
async def get_task_stats():
    """获取任务统计"""
    try:
        stats = task_service.get_task_stats()
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取统计信息失败: {str(e)}")


@router.post("/tasks/{task_id}/complete", response_model=Task, tags=["任务管理"])
async def complete_task(task_id: int):
    """完成任务"""
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="任务不存在")

    update_data = TaskUpdate(status=TaskStatus.COMPLETED)
    updated_task = task_service.update_task(task_id, update_data)
    return updated_task


@router.post("/tasks/{task_id}/start", response_model=Task, tags=["任务管理"])
async def start_task(task_id: int):
    """开始任务"""
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="任务不存在")

    update_data = TaskUpdate(status=TaskStatus.IN_PROGRESS)
    updated_task = task_service.update_task(task_id, update_data)
    return updated_task
