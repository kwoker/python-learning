# FastAPI REST API 项目

> 🚀 基于 FastAPI 的任务管理系统 REST API

## 🎯 项目简介

这是一个完整的 FastAPI REST API 项目，实现了任务管理系统。包含用户管理、任务 CRUD 操作、统计功能等，提供完整的 Web API 服务。

## ✨ 特性

- 📦 **完整的 REST API** - 遵循 REST 原则
- 🔄 **CRUD 操作** - 创建、读取、更新、删除任务
- 📊 **数据统计** - 任务统计和分析
- 🔍 **筛选分页** - 支持状态、优先级筛选和分页
- 📚 **自动文档** - 自动生成 API 文档
- ✅ **输入验证** - 使用 Pydantic 进行数据验证
- 🛡️ **异常处理** - 全局异常处理
- 🌐 **CORS 支持** - 跨域资源共享

## 📁 项目结构

```
fastapi-rest-api/
├── app/                          # 主应用目录
│   ├── __init__.py
│   ├── main.py                   # FastAPI 应用入口
│   ├── core/                     # 核心配置
│   │   ├── __init__.py
│   │   └── config.py             # 配置管理
│   ├── api/                      # API 路由
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py            # 路由汇总
│   │       └── endpoints/        # API 端点
│   │           ├── __init__.py
│   │           └── tasks.py      # 任务端点
│   ├── models/                   # 数据模型
│   │   ├── __init__.py
│   │   └── task.py               # 任务模型
│   ├── schemas/                  # Pydantic 模式
│   │   └── __init__.py
│   └── services/                 # 业务逻辑
│       ├── __init__.py
│       └── task_service.py       # 任务服务
├── test_api.py                   # API 测试脚本
├── requirements.txt              # 项目依赖
└── README.md                     # 项目文档
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动服务器

```bash
# 开发模式
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 或直接运行
python app/main.py
```

### 3. 访问 API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

### 4. 运行测试

```bash
# 确保服务器启动后，运行测试
python test_api.py
```

## 📖 API 文档

### 根路径

#### GET /
- **描述**: 获取 API 信息
- **响应**: API 基本信息

#### GET /health
- **描述**: 健康检查
- **响应**: 服务状态

### 任务管理

#### POST /api/v1/tasks
- **描述**: 创建新任务
- **请求体**:
  ```json
  {
    "title": "任务标题",
    "description": "任务描述",
    "status": "pending",
    "priority": "medium",
    "due_date": "2024-12-31T23:59:59"
  }
  ```
- **响应**: 创建的任务对象

#### GET /api/v1/tasks
- **描述**: 获取任务列表
- **查询参数**:
  - `page`: 页码 (默认: 1)
  - `page_size`: 每页数量 (默认: 10, 最大: 100)
  - `status`: 状态筛选 (pending, in_progress, completed, cancelled)
  - `priority`: 优先级筛选 (low, medium, high, urgent)
- **响应**: 分页的任务列表

#### GET /api/v1/tasks/{task_id}
- **描述**: 获取单个任务
- **路径参数**:
  - `task_id`: 任务 ID
- **响应**: 任务详情

#### PUT /api/v1/tasks/{task_id}
- **描述**: 更新任务
- **路径参数**:
  - `task_id`: 任务 ID
- **请求体**: 部分任务字段
- **响应**: 更新后的任务

#### DELETE /api/v1/tasks/{task_id}
- **描述**: 删除任务
- **路径参数**:
  - `task_id`: 任务 ID
- **响应**: 成功消息

#### POST /api/v1/tasks/{task_id}/complete
- **描述**: 完成任务
- **路径参数**:
  - `task_id`: 任务 ID
- **响应**: 更新后的任务

#### POST /api/v1/tasks/{task_id}/start
- **描述**: 开始任务
- **路径参数**:
  - `task_id`: 任务 ID
- **响应**: 更新后的任务

### 任务统计

#### GET /api/v1/tasks/stats
- **描述**: 获取任务统计信息
- **响应**:
  ```json
  {
    "total": 10,
    "pending": 2,
    "in_progress": 3,
    "completed": 4,
    "cancelled": 1,
    "overdue": 1
  }
  ```

## 💻 使用示例

### Python requests

```python
import requests

BASE_URL = "http://localhost:8000/api/v1"

# 创建任务
task_data = {
    "title": "完成项目文档",
    "description": "撰写项目技术文档",
    "priority": "high"
}

response = requests.post(f"{BASE_URL}/tasks", json=task_data)
task = response.json()
print(f"创建任务 ID: {task['id']}")

# 获取任务列表
response = requests.get(f"{BASE_URL}/tasks?status=pending")
tasks = response.json()
print(f"待处理任务数: {tasks['total']}")

# 完成任务
response = requests.post(f"{BASE_URL}/tasks/{task['id']}/complete")
completed_task = response.json()
print(f"任务状态: {completed_task['status']}")
```

### curl

```bash
# 创建任务
curl -X POST "http://localhost:8000/api/v1/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "新任务",
    "description": "任务描述",
    "priority": "medium"
  }'

# 获取任务列表
curl "http://localhost:8000/api/v1/tasks?status=pending&page=1&page_size=10"

# 更新任务
curl -X PUT "http://localhost:8000/api/v1/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'

# 获取统计信息
curl "http://localhost:8000/api/v1/tasks/stats"
```

### JavaScript fetch

```javascript
const BASE_URL = 'http://localhost:8000/api/v1';

// 创建任务
const taskData = {
    title: '新任务',
    description: '任务描述',
    priority: 'high'
};

fetch(`${BASE_URL}/tasks`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(taskData)
})
.then(response => response.json())
.then(task => {
    console.log('创建任务:', task);
});

// 获取任务列表
fetch(`${BASE_URL}/tasks?status=pending&page=1&page_size=10`)
.then(response => response.json())
.then(data => {
    console.log('任务列表:', data.items);
    console.log('总数:', data.total);
});
```

## 🛠️ 技术栈

- **FastAPI** - 现代化 Web 框架
- **Pydantic** - 数据验证
- **Uvicorn** - ASGI 服务器
- **Python 3.8+** - 编程语言

## 🔧 配置

### 环境变量

创建 `.env` 文件：

```bash
# 应用配置
SECRET_KEY=your-secret-key-change-in-production
ALLOWED_HOSTS=["*"]

# 数据库配置（可选）
DATABASE_URL=postgresql://user:password@localhost/dbname

# 服务器配置
HOST=0.0.0.0
PORT=8000
```

### 配置项说明

- `SECRET_KEY`: 应用密钥
- `ALLOWED_HOSTS`: 允许的 CORS 主机
- `DATABASE_URL`: 数据库连接 URL
- `HOST`: 服务器绑定地址
- `PORT`: 服务器端口

## 🧪 测试

### 单元测试（可选）

```bash
pip install pytest httpx

# 运行测试
pytest tests/
```

### API 测试

运行提供的测试脚本：

```bash
python test_api.py
```

测试包括：
- 根路径测试
- 健康检查
- 任务 CRUD 操作
- 筛选和分页
- 统计功能

## 📊 数据模型

### 任务 (Task)

| 字段 | 类型 | 描述 | 必需 |
|------|------|------|------|
| id | int | 任务 ID | 自动生成 |
| title | str | 任务标题 | 是 |
| description | str | 任务描述 | 否 |
| status | enum | 任务状态 | 否 (默认: pending) |
| priority | enum | 任务优先级 | 否 (默认: medium) |
| due_date | datetime | 截止日期 | 否 |
| created_at | datetime | 创建时间 | 自动生成 |
| updated_at | datetime | 更新时间 | 自动生成 |

### 任务状态
- `pending`: 待处理
- `in_progress`: 进行中
- `completed`: 已完成
- `cancelled`: 已取消

### 任务优先级
- `low`: 低
- `medium`: 中
- `high`: 高
- `urgent`: 紧急

## 🔄 扩展功能

### 添加数据库支持

1. 安装数据库驱动：
```bash
pip install sqlalchemy asyncpg  # PostgreSQL
# 或
pip install sqlalchemy aiomysql  # MySQL
```

2. 创建数据库模型：
```python
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000))
    status = Column(Enum('pending', 'in_progress', 'completed', 'cancelled'))
    priority = Column(Enum('low', 'medium', 'high', 'urgent'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
```

### 添加认证

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

def get_current_user(token: str = Depends(security)):
    # 验证 token
    # 返回用户信息
    pass

@router.get("/tasks")
async def get_tasks(current_user: dict = Depends(get_current_user)):
    # 需要认证的端点
    pass
```

### 添加日志

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/tasks")
async def create_task(task: TaskCreate):
    logger.info(f"创建任务: {task.title}")
    # ...
```

## 🐛 常见问题

### Q: 如何处理跨域请求？
A: 应用已配置 CORS 中间件，如需修改，在 `app/main.py` 中调整 `ALLOWED_HOSTS`。

### Q: 如何添加更多 API 端点？
A: 在 `app/api/v1/endpoints/` 下创建新的端点文件，并在 `api.py` 中注册。

### Q: 如何连接数据库？
A: 目前使用内存存储，生产环境建议集成 SQLAlchemy 或其他 ORM。

### Q: 如何部署到生产环境？
A: 使用 Gunicorn + Uvicorn workers：
```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📚 学习资源

### 官方文档
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Pydantic 文档](https://docs.pydantic.dev/)
- [Uvicorn 文档](https://www.uvicorn.org/)

### 教程
- [FastAPI 教程](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI 进阶](https://fastapi.tiangolo.com/advanced/)

### 社区
- [GitHub 讨论](https://github.com/tiangolo/fastapi/discussions)
- [Discord 社区](https://discord.com/invite/VQjSZaeJ2W)

## 🤝 贡献

欢迎贡献代码！

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 创建 Pull Request

## 📄 许可证

MIT License

## 👨‍💻 作者

Claude - Anthropic

---

**开始构建你的 Web API！** 🚀
