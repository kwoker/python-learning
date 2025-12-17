"""
API 路由汇总
"""

from fastapi import APIRouter
from app.api.v1.endpoints import tasks

api_router = APIRouter()

# 注册所有端点
api_router.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["任务管理"]
)
