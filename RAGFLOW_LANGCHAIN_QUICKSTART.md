# RAGFlow 和 LangChain 快速开始指南

## 🚀 快速上手

### 第一步：安装依赖

```bash
# 基础依赖
pip install langchain langchain-openai langchain-community

# 向量数据库
pip install chromadb

# 文档处理
pip install pypdf python-docx beautifulsoup4
```

### 第二步：设置 API 密钥

```bash
# Linux/macOS
export OPENAI_API_KEY="your-api-key-here"

# Windows
set OPENAI_API_KEY=your-api-key-here

# 或者在 .env 文件中
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### 第三步：运行示例

```bash
# LangChain 基础示例
python examples/llm/langchain-basics.py

# RAG 示例
python examples/llm/langchain-rag-examples.py

# RAGFlow 集成示例
python examples/llm/ragflow-integration.py

# 实战项目
cd projects/document-qa-system
python main.py
```

## 📁 项目结构

```
test1/
├── examples/llm/                    # 学习示例
│   ├── langchain-basics.py         # LangChain 基础
│   ├── langchain-rag-examples.py   # RAG 应用
│   └── ragflow-integration.py      # RAGFlow 集成
├── projects/document-qa-system/     # 实战项目
│   ├── main.py                     # 主程序
│   ├── README.md                   # 项目文档
│   ├── requirements.txt            # 依赖列表
│   └── data/knowledge/             # 示例文档
└── .agentdocs/learning/            # 学习文档
    ├── ragflow-langchain-guide.md  # 基础指南
    └── comprehensive-guide.md      # 完整指南
```

## 💡 学习路径

### 1️⃣ 入门阶段（1-2周）
**目标**：理解基本概念

**内容**：
- 阅读 `.agentdocs/learning/ragflow-langchain-guide.md`
- 运行 `langchain-basics.py`
- 理解 LLM、Prompt、Chain 的概念

**实践**：
```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 基础调用
llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke("解释机器学习")
print(response.content)

# 使用链
template = PromptTemplate(
    input_variables=["topic"],
    template="请解释{topic}"
)
chain = LLMChain(llm=llm, prompt=template)
result = chain.run(topic="Python")
```

### 2️⃣ 进阶阶段（2-3周）
**目标**：掌握 RAG 应用

**内容**：
- 阅读 `langchain-rag-examples.py`
- 学习向量数据库和文档分块
- 构建简单的问答系统

**实践**：
```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# 创建向量存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

# 检索
docs = vectorstore.similarity_search("Python 特点", k=3)
```

### 3️⃣ 实战阶段（1-2周）
**目标**：完成完整项目

**内容**：
- 部署 `document-qa-system` 项目
- 添加自己的文档
- 优化检索效果

**实践**：
```bash
cd projects/document-qa-system
# 添加文档到 data/knowledge/
python main.py
```

### 4️⃣ 高级阶段（持续）
**目标**：企业级应用

**内容**：
- 学习 RAGFlow 部署
- 性能优化和成本控制
- 多模态扩展

**实践**：
- 部署 RAGFlow 服务器
- 构建生产级应用

## 📚 推荐学习资源

### 官方文档
- [LangChain 文档](https://python.langchain.com/)
- [RAGFlow 文档](https://ragflow.io/)

### 视频教程
- LangChain 官方教程
- YouTube RAGFlow 教程

### 实践项目
- 智能客服机器人
- 文档助手
- 代码问答系统

## ⚠️ 注意事项

### API 成本控制
```python
# 使用缓存
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
set_llm_cache(InMemoryCache())

# 控制输出长度
llm = ChatOpenAI(max_tokens=500)

# 使用更便宜的模型
llm = ChatOpenAI(model="gpt-3.5-turbo")  # vs gpt-4
```

### 数据安全
- 不要上传敏感文档到第三方 API
- 考虑使用本地化部署
- 使用企业版 RAGFlow

### 性能优化
- 合理设置分块大小（500 tokens）
- 使用重叠保持上下文（50-100 tokens）
- 调整 Top-K 检索数量（3-5）

## 🎯 学习目标检查

### 完成基础阶段后，你应该能：
- [ ] 调用 OpenAI API
- [ ] 使用 Prompt Template
- [ ] 构建简单的 LLM Chain
- [ ] 理解对话记忆

### 完成进阶阶段后，你应该能：
- [ ] 配置向量数据库
- [ ] 实现文档检索
- [ ] 构建 RAG 应用
- [ ] 优化检索效果

### 完成实战阶段后，你应该能：
- [ ] 部署完整问答系统
- [ ] 处理多种文档格式
- [ ] 实现多轮对话
- [ ] 分析系统性能

## 💬 获取帮助

### 遇到问题？
1. 查看文档：`.agentdocs/learning/comprehensive-guide.md`
2. 检查示例代码
3. 搜索官方文档
4. 社区求助

### 常见错误
- **API 密钥错误**：检查环境变量设置
- **导入错误**：确认已安装所需依赖
- **文档加载失败**：检查文件路径和格式
- **检索效果差**：调整分块策略和参数

## 🎓 下一步学习

1. **深度学习**：PyTorch、TensorFlow
2. **Agent 开发**：LangChain Agents
3. **多模态**：CLIP、GPT-4V
4. **本地部署**：Llama、Mistral

---

**祝你学习愉快！** 🎉

有任何问题，随时查看详细文档或寻求社区帮助。
