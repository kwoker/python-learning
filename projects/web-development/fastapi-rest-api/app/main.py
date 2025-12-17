"""
FastAPI REST API 主应用
任务管理系统 API
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from app.api.v1.api import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时执行
    print("🚀 任务管理 API 启动中...")
    yield
    # 关闭时执行
    print("👋 任务管理 API 关闭")


# 创建 FastAPI 应用
app = FastAPI(
    title="任务管理 API",
    description="基于 FastAPI 的任务管理系统，提供完整的 REST API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 根路径
@app.get("/", tags=["根路径"])
async def root():
    """根路径，返回 API 信息"""
    return {
        "message": "欢迎使用任务管理 API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# 健康检查
@app.get("/health", tags=["健康检查"])
async def health_check():
    """健康检查接口"""
    return {
        "status": "healthy",
        "message": "API 运行正常"
    }


# 注册 API 路由
app.include_router(api_router, prefix=settings.API_V1_STR)


# 全局异常处理
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """HTTP 异常处理器"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
                "type": "HTTPException"
            }
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """通用异常处理器"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "code": 500,
                "message": "服务器内部错误",
                "type": "InternalServerError"
            }
        }
    )


if __name__ == "__main__":
    uvicorn.run(
app",
        host        "main:="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
