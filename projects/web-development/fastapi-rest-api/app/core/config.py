"""
配置管理
"""

import os
from typing import List, Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """应用配置"""
    # API 配置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "任务管理 API"

    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # CORS 配置
    ALLOWED_HOSTS: List[str] = ["*"]

    # 数据库配置（可选）
    DATABASE_URL: Optional[str] = None

    # 密钥配置
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")

    # 分页配置
    DEFAULT_PAGE_SIZE: int = 10
    MAX_PAGE_SIZE: int = 100

    class Config:
        env_file = ".env"


# 创建配置实例
settings = Settings()
