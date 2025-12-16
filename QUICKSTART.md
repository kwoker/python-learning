# 快速开始指南

欢迎来到 Test1 Python 学习项目！这个项目包含了丰富的示例代码和练习，帮助你快速掌握 Python。

## 🚀 快速开始

### 1. 进入项目目录
```bash
cd test1
```

### 2. 运行主程序
```bash
python main.py
```

这将运行所有的基础示例，包括：
- Hello World
- 变量和数据类型
- 控制流（if、for、while）
- 面向对象编程
- 文件操作

### 3. 学习路径

#### 路径 1：按示例学习
1. 先运行 `python main.py` 了解整体结构
2. 进入 `examples/basics/` 目录，从 `hello_world.py` 开始
3. 逐步学习 `variables.py` 和 `control_flow.py`
4. 进阶到 `oop/` 和 `modules/` 目录
5. 挑战 `advanced/` 目录的装饰器等高级特性

#### 路径 2：实践练习
1. 直接打开 `exercises/exercise1.py`
2. 实现 TODO 部分的函数
3. 运行文件查看结果
4. 对照示例代码理解正确实现

## 📁 项目结构说明

```
test1/
├── main.py              # 主程序入口
├── README.md            # 详细项目说明
├── QUICKSTART.md        # 快速开始（本文件）
├── requirements.txt     # Python 依赖包
├── .gitignore          # Git 忽略文件配置
│
├── examples/           # 示例代码目录
│   ├── basics/         # 基础语法示例
│   │   ├── hello_world.py
│   │   ├── variables.py
│   │   └── control_flow.py
│   │
│   ├── oop/            # 面向对象编程
│   │   └── basic_class.py
│   │
│   ├── modules/        # 模块使用
│   │   └── file_operations.py
│   │
│   └── advanced/       # 高级特性
│       └── decorators.py
│
├── exercises/          # 练习题
│   └── exercise1.py
│
├── data/               # 示例数据
│   └── .gitkeep
│
└── notes/              # 学习笔记
    └── python_basics.md
```

## 🎯 学习建议

### 初学者
1. **先运行 `python main.py`**，看看所有功能的效果
2. **阅读 `hello_world.py`**，理解 Python 程序的基本结构
3. **学习 `variables.py`**，掌握各种数据类型
4. **练习 `control_flow.py`**，熟悉条件语句和循环
5. **完成 `exercise1.py`** 中的练习题

### 有基础的开发者
1. **直接跳到高级示例**，如 `decorators.py`
2. **尝试修改示例代码**，加入自己的创意
3. **扩展练习题**，添加更多挑战
4. **创建自己的模块**，放在 `examples/` 目录下

## 💡 使用技巧

### 1. 虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行单个示例
```bash
# 只运行 Hello World 示例
python examples/basics/hello_world.py

# 只运行面向对象示例
python examples/oop/basic_class.py
```

### 3. 使用 Jupyter Notebook（可选）
如果安装了 Jupyter，可以创建 Notebook 来实验：
```bash
pip install jupyter
jupyter notebook
```

## 📚 扩展学习

### 添加新的示例
1. 在相应目录创建新的 `.py` 文件
2. 编写示例代码
3. 在 `main.py` 中添加调用
4. 运行测试

### 添加练习题
1. 在 `exercises/` 目录创建新文件
2. 编写题目描述和 TODO
3. 提供测试用例
4. 运行验证

## 🆘 遇到问题？

1. **查看错误信息**：Python 会显示详细的错误和行号
2. **阅读注释**：每个示例都有详细的注释
3. **查阅笔记**：`notes/python_basics.md` 包含语法要点
4. **在线资源**：
   - [Python 官方教程](https://docs.python.org/3/tutorial/)
   - [Python 练习题](https://www.w3resource.com/python-exercises/)

## ✅ 学习检查清单

- [ ] 运行了 `python main.py`
- [ ] 阅读了 `hello_world.py`
- [ ] 理解了 `variables.py` 中的数据类型
- [ ] 练习了 `control_flow.py` 中的控制流
- [ ] 完成了 `exercise1.py` 中的至少一个练习
- [ ] 查看了 `notes/python_basics.md`

---

祝你学习愉快！ 🎉

如果这个项目对你有帮助，欢迎给项目点星或分享给其他学习者！
