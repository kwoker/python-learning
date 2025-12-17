# 文档问答系统

基于 LangChain 和 RAGFlow 的智能文档问答系统，支持多文档格式、智能检索和多轮对话。

## 功能特性

- 📄 **多格式支持**: PDF、TXT、DOCX 文档
- 🔍 **智能检索**: 基于向量相似度的语义搜索
- 💬 **多轮对话**: 支持上下文记忆
- 📚 **答案溯源**: 显示答案来源文档
- ⚙️ **灵活配置**: 可调整分块策略和检索参数
- 🌐 **易于扩展**: 模块化设计，易于添加新功能

## 项目结构

```
document-qa-system/
├── main.py                 # 主程序入口
├── README.md              # 项目说明
├── data/                  # 数据目录
│   ├── knowledge/         # 知识库文档
│   └── vectorstore/       # 向量存储（自动生成）
├── requirements.txt       # 依赖列表
└── .env.example          # 环境变量示例
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

创建 `.env` 文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，设置你的 API 密钥：

```env
OPENAI_API_KEY=your-api-key-here
```

### 3. 准备知识库

在 `data/knowledge/` 目录下放置你的文档：

```bash
# 创建目录
mkdir -p data/knowledge

# 复制示例文档或添加自己的文档
cp /path/to/your/document.txt data/knowledge/
```

支持的格式：
- `.txt` - 纯文本文件
- `.pdf` - PDF 文档
- `.docx` - Word 文档

### 4. 运行系统

```bash
python main.py
```

## 使用说明

### 交互式问答

运行程序后，你可以直接输入问题：

```
🤔 问题: Python 的主要特点是什么？

💡 回答: Python是一种高级编程语言，具有以下主要特点：
1. 简洁易读：语法简单，接近自然语言
2. 开源免费：可以自由地使用和分发
3. 跨平台：可以在多种操作系统上运行
4. 丰富的库：标准库功能强大，第三方库丰富
5. 可扩展：可以与C/C++等语言混合编程

📚 来源: python-guide.txt
```

### 程序化调用

```python
from main import DocumentQASystem, Config

# 初始化系统
qa_system = DocumentQASystem(Config())

# 添加知识库
qa_system.add_knowledge_base(["data/knowledge/my-doc.txt"])

# 问答查询
result = qa_system.query("什么是机器学习？")
print(result["answer"])
print("来源:", result["sources"])
```

## 配置选项

### 在 `Config` 类中可以调整的参数：

```python
class Config:
    # LLM 配置
    MODEL_NAME = "gpt-3.5-turbo"      # 模型名称
    TEMPERATURE = 0.1                 # 生成随机性 (0-1)

    # 文档处理配置
    CHUNK_SIZE = 500                  # 文档块大小（字符数）
    CHUNK_OVERLAP = 50                # 块重叠大小
    MAX_CHUNKS_PER_QUERY = 5          # 每次查询的最大文档块数

    # 存储配置
    VECTOR_STORE_PATH = "./data/vectorstore"  # 向量存储路径
    KNOWLEDGE_BASE_PATH = "./data/knowledge"  # 知识库路径
```

### 参数调优建议：

- **CHUNK_SIZE**:
  - 小文档（< 1MB）: 200-500
  - 大文档（> 1MB）: 500-1000
  - 过小：失去上下文；过大：检索不精确

- **CHUNK_OVERLAP**:
  - 通常为 CHUNK_SIZE 的 10-20%
  - 作用：保持文档块之间的连续性

- **MAX_CHUNKS_PER_QUERY**:
  - 简单问题：3-5
  - 复杂问题：5-10
  - 过多：可能引入噪音；过少：可能遗漏信息

## 高级功能

### 1. 自定义文档加载器

```python
from langchain_community.document_loaders import WebLoader

# 加载网页
loader = WebLoader("https://example.com")
documents = loader.load()

# 自定义处理
processor = DocumentProcessor()
splits = processor.split_text(documents)
```

### 2. 不同的检索策略

```python
# 相似度搜索（默认）
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# 最大边际相关性搜索（MMR）
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "lambda_mult": 0.5}
)
```

### 3. 自定义提示词模板

```python
custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
你是一个专业的技术文档助手。请基于提供的上下文回答问题。

上下文：
{context}

问题：{question}

要求：
1. 回答准确、专业
2. 如果上下文没有相关信息，明确说明
3. 使用简洁明了的语言
"""
)
```

## 性能优化

### 1. 缓存向量存储

向量存储会持久化到本地，重复使用时无需重建：

```python
# 系统会自动加载现有的向量存储
qa_system = DocumentQASystem(config)

# 首次运行需要构建向量存储，后续运行直接使用
```

### 2. 批量添加文档

```python
# 一次性添加多个文档
doc_paths = [
    "data/knowledge/doc1.txt",
    "data/knowledge/doc2.txt",
    "data/knowledge/doc3.txt"
]
qa_system.add_knowledge_base(doc_paths)
```

### 3. 异步处理（可选）

对于大量文档，可以使用异步处理：

```python
import asyncio

async def async_add_documents(qa_system, doc_paths):
    tasks = []
    for doc_path in doc_paths:
        task = asyncio.create_task(
            asyncio.to_thread(qa_system.add_knowledge_base, [doc_path])
        )
        tasks.append(task)

    await asyncio.gather(*tasks)

# 使用
asyncio.run(async_add_documents(qa_system, doc_paths))
```

## 故障排除

### 常见问题

**1. 文档加载失败**
```
错误: FileNotFoundError
解决: 检查文件路径是否正确，文件是否存在
```

**2. API 调用失败**
```
错误: API 错误或配额超限
解决: 检查 API 密钥是否正确，账户是否有余额
```

**3. 向量存储错误**
```
错误: ChromaDB 相关错误
解决: 删除 vectorstore 目录重新构建
rm -rf data/vectorstore
```

**4. 检索质量差**
```
问题: 答案不准确或找不到相关信息
解决: 调整 CHUNK_SIZE 和 CHUNK_OVERLAP 参数
```

## 扩展开发

### 添加新的文档格式

```python
from langchain_community.document_loaders import BaseLoader

class CustomLoader(BaseLoader):
    def load(self):
        # 实现自定义加载逻辑
        pass

# 在 DocumentProcessor 中添加支持
if file_path.suffix.lower() == ".custom":
    loader = CustomLoader(str(file_path))
```

### 添加新的检索方式

```python
class CustomRetriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def search(self, query, k=5):
        # 实现自定义检索逻辑
        pass
```

## 最佳实践

1. **文档准备**
   - 清理无关内容（页眉、页脚、目录）
   - 保持文本的语义完整性
   - 使用 UTF-8 编码保存文本文件

2. **参数调优**
   - 根据文档类型调整分块策略
   - 测试不同的检索参数
   - 监控答案质量

3. **性能优化**
   - 定期清理向量存储
   - 合理设置缓存策略
   - 监控 API 使用量

4. **安全考虑**
   - 不上传敏感文档到第三方 API
   - 使用本地部署的 RAGFlow
   - 定期备份向量数据库

## 参考资料

- [LangChain 官方文档](https://python.langchain.com/)
- [RAGFlow 官方文档](https://ragflow.io/)
- [向量数据库比较](https://docs.trychroma.com/)
- [提示词工程指南](https://www.promptingguide.ai/)

## 许可证

MIT License
