# 📚 学习资源导航

> 🎯 快速定位所有学习资源，按学习阶段分类

---

## 🚀 快速开始

**第一步：了解项目**
👉 [README.md](README.md) - 项目介绍和基本信息

**第二步：选择学习路径**
👉 [COMPLETE_LEARNING_GUIDE.md](COMPLETE_LEARNING_GUIDE.md) - 完整学习路径指南（推荐⭐⭐⭐）

---

## 📖 按阶段学习

### 🌱 第一阶段：Python 基础（2-3周）

#### 核心文档
- 📝 [QUICKSTART.md](QUICKSTART.md) - 快速开始指南
- 📝 [notes/python_basics.md](notes/python_basics.md) - 基础学习笔记

#### 示例代码
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/basics/hello_world.py` | 第一个程序 | 程序运行方式 |
| `examples/basics/variables.py` | 变量和数据类型 | int, float, str, bool, list, dict |
| `examples/basics/control_flow.py` | 条件语句和循环 | if, for, while, 函数 |

#### 练习
- 💻 [exercises/exercise1.py](exercises/exercise1.py) - 基础练习题

**学习顺序**: QUICKSTART → 基础示例 → 练习题 → 学习笔记

---

### 🌿 第二阶段：Python 进阶（2-3周）

#### 面向对象
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/oop/basic_class.py` | 类和对象、继承 | 类定义、self、继承、封装 |

#### 模块系统
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/modules/file_operations.py` | 模块导入、文件操作 | import、from...import、文件I/O |

#### 高级特性
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/advanced/decorators.py` | 装饰器、生成器 | @装饰器、yield、迭代器 |

**学习顺序**: OOP → 模块 → 高级特性

---

### 🌳 第三阶段：LLM 应用开发（3-4周）

#### 快速上手
- 📝 [RAGFLOW_LANGCHAIN_QUICKSTART.md](RAGFLOW_LANGCHAIN_QUICKSTART.md) - LLM开发快速开始

#### LangChain 学习
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/llm/langchain-basics.py` | LangChain 基础 | LLM调用、Prompt、Chain、Memory |

#### RAG 应用
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/llm/langchain-rag-examples.py` | RAG 应用开发 | 向量数据库、文档分块、检索QA |

#### RAGFlow 企业级
| 文件 | 内容 | 重点 |
|------|------|------|
| `examples/llm/ragflow-integration.py` | RAGFlow 集成 | API客户端、知识库管理、多轮对话 |

#### 深度指南
- 📝 [`.agentdocs/learning/ragflow-langchain-guide.md`](.agentdocs/learning/ragflow-langchain-guide.md) - 核心概念和学习路径
- 📝 [`.agentdocs/learning/comprehensive-guide.md`](.agentdocs/learning/comprehensive-guide.md) - 完整学习指南（含最佳实践）

**学习顺序**: 快速上手 → LangChain基础 → RAG应用 → RAGFlow → 深度指南

---

### 🎯 第四阶段：实战项目（2-3周）

#### 文档问答系统
📁 `projects/document-qa-system/`

| 文件 | 描述 |
|------|------|
| `README.md` | 项目详细文档 |
| `main.py` | 主程序入口 |
| `requirements.txt` | 依赖列表 |
| `data/knowledge/` | 示例知识库文档 |

**运行方式**:
```bash
cd projects/document-qa-system
python main.py
```

---

## 📋 学习资源总览

### 文档类型

| 类型 | 文件 | 描述 |
|------|------|------|
| 📖 主指南 | `COMPLETE_LEARNING_GUIDE.md` | 完整学习路径 |
| 🚀 快速开始 | `QUICKSTART.md` | 项目入门 |
| 🚀 LLM快速开始 | `RAGFLOW_LANGCHAIN_QUICKSTART.md` | LLM开发入门 |
| 📝 项目说明 | `README.md` | 项目基本信息 |
| 📚 导航 | `LEARNING_INDEX.md` | 本文件，学习资源导航 |

### 代码示例

| 目录 | 内容 |
|------|------|
| `examples/basics/` | Python 基础语法示例 |
| `examples/oop/` | 面向对象编程示例 |
| `examples/modules/` | 模块和文件操作示例 |
| `examples/advanced/` | 高级特性示例（装饰器等） |
| `examples/llm/` | LangChain 和 RAGFlow 示例 |
| `exercises/` | 练习题 |
| `projects/document-qa-system/` | 实战项目 |

### 学习笔记

| 文件 | 内容 |
|------|------|
| `notes/python_basics.md` | Python 基础学习笔记 |
| `.agentdocs/learning/` | LLM 应用开发学习指南 |

---

## 🎓 学习路径推荐

### 零基础学习者
```
1. 阅读 COMPLETE_LEARNING_GUIDE.md 了解全貌
2. 按阶段学习：基础 → 进阶 → LLM → 实战
3. 每完成一个示例，立即动手实践
4. 完成所有练习题
5. 最后完成实战项目
```

### 有 Python 基础的学习者
```
1. 直接从第二阶段进阶内容开始
2. 快速浏览基础示例，查漏补缺
3. 重点学习第三阶段 LLM 应用开发
4. 完成实战项目
```

### 有 LLM 应用开发经验的学习者
```
1. 查看 examples/llm/ 了解项目代码风格
2. 直接运行并研究 document-qa-system 项目
3. 参考 comprehensive-guide.md 进行深度优化
4. 扩展项目功能
```

---

## ⚡ 常用命令

### 运行示例
```bash
# 基础示例
python examples/basics/hello_world.py
python examples/basics/variables.py
python examples/basics/control_flow.py

# 进阶示例
python examples/oop/basic_class.py
python examples/modules/file_operations.py
python examples/advanced/decorators.py

# LLM 示例
python examples/llm/langchain-basics.py
python examples/llm/langchain-rag-examples.py

# 实战项目
cd projects/document-qa-system
python main.py
```

### 环境配置
```bash
# 安装依赖
pip install -r requirements.txt

# 设置 API 密钥
export OPENAI_API_KEY="your-api-key"
```

---

## ✅ 学习检查清单

### 基础阶段
- [ ] 运行所有基础示例
- [ ] 完成练习题
- [ ] 理解变量、数据类型、控制流
- [ ] 能够编写简单函数

### 进阶阶段
- [ ] 理解类和对象
- [ ] 掌握继承和封装
- [ ] 理解装饰器原理
- [ ] 熟练使用模块

### LLM 应用开发阶段
- [ ] 完成所有 LangChain 示例
- [ ] 理解 RAG 原理
- [ ] 能够调用 OpenAI API
- [ ] 构建简单的问答系统

### 实战阶段
- [ ] 成功运行文档问答系统
- [ ] 添加自己的文档
- [ ] 理解系统架构
- [ ] 能够扩展功能

---

## 🆘 获取帮助

### 文档资源
- [Python 官方文档](https://docs.python.org/3/)
- [LangChain 文档](https://python.langchain.com/)
- [RAGFlow 文档](https://ragflow.io/)

### 项目文档
- 📖 [COMPLETE_LEARNING_GUIDE.md](COMPLETE_LEARNING_GUIDE.md) - 完整学习指南
- 📚 [`.agentdocs/learning/comprehensive-guide.md`](.agentdocs/learning/comprehensive-guide.md) - 深度指南
- 📝 [项目 README](README.md) - 项目信息

---

## 📞 快速定位

**想知道整体学习路径？**
👉 [COMPLETE_LEARNING_GUIDE.md](COMPLETE_LEARNING_GUIDE.md)

**想快速开始？**
👉 [QUICKSTART.md](QUICKSTART.md) 或 [RAGFLOW_LANGCHAIN_QUICKSTART.md](RAGFLOW_LANGCHAIN_QUICKSTART.md)

**想学习 Python 基础？**
👉 `examples/basics/` 目录

**想学习面向对象？**
👉 `examples/oop/basic_class.py`

**想学习 LangChain？**
👉 `examples/llm/langchain-basics.py`

**想学习 RAG？**
👉 `examples/llm/langchain-rag-examples.py`

**想学习 RAGFlow？**
👉 `examples/llm/ragflow-integration.py`

**想完成实战项目？**
👉 `projects/document-qa-system/`

---

*祝学习愉快！* 🎉
