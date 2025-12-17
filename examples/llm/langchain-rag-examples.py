"""
LangChain RAG（检索增强生成）示例
演示如何使用 LangChain 构建检索增强生成应用
"""

import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader

# ============================================================================
# 示例 1: 简单的 RAG 流程
# ============================================================================

def simple_rag_example():
    """简单的 RAG 应用示例"""
    print("=" * 60)
    print("示例 1: 简单 RAG 应用")
    print("=" * 60)

    print("RAG (Retrieval-Augmented Generation) 工作流程：")
    print("""
1. 文档加载 → 2. 文本分块 → 3. 向量化 → 4. 存储 → 5. 检索 → 6. 生成答案

代码示例：

# 1. 准备文档（假设有文本文件）
loader = TextLoader("knowledge.txt")
documents = loader.load()

# 2. 文本分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(documents)

# 3. 创建向量存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(splits, embeddings)

# 4. 创建检索器
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 5. 创建 QA 链
template = PromptTemplate(
    input_variables=["context", "question"],
    template='''基于以下上下文回答问题：

上下文：
{context}

问题：{question}

请提供准确、详细的回答。'''
)

llm = ChatOpenAI(model="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": template}
)

# 6. 问答
question = "文档中提到的关键技术有哪些？"
result = qa_chain({"query": question})
print(result["result"])
    """)


# ============================================================================
# 示例 2: 多文档处理
# ============================================================================

def multi_document_rag():
    """多文档 RAG 应用示例"""
    print("=" * 60)
    print("示例 2: 多文档处理")
    print("=" * 60)

    print("处理多个文档的 RAG 应用：")
    print("""
# 1. 加载多个文档
loader = DirectoryLoader(
    "knowledge_base/",
    glob="**/*.txt"  # 加载所有 txt 文件
)
documents = loader.load()

# 2. 文本分块（根据文档类型调整策略）
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\\n\\n", "\\n", "。", "！", "？"]
)
splits = text_splitter.split_documents(documents)

# 3. 向量化和存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(splits, embeddings)

# 4. 带过滤的检索
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 5,
        "filter": {"source": "technical_docs"}  # 过滤特定来源
    }
)
    """)


# ============================================================================
# 示例 3: 自定义检索策略
# ============================================================================

def custom_retrieval_example():
    """自定义检索策略示例"""
    print("=" * 60)
    print("示例 3: 自定义检索")
    print("=" * 60)

    print("不同的检索策略：")
    print("""
# 1. 相似度搜索（默认）
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# 2. 最大边际相关性搜索（MMR）
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "lambda_mult": 0.5  # 控制多样性和相关性平衡
    }
)

# 3. 过滤搜索
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 4,
        "filter": {
            "category": "技术文档",
            "date": {"$gte": "2024-01-01"}
        }
    }
)
    """)


# ============================================================================
# 示例 4: RAG 链的不同类型
# ============================================================================

def rag_chain_types():
    """RAG 链类型示例"""
    print("=" * 60)
    print("示例 4: RAG Chain 类型")
    print("=" * 60)

    print("四种 RAG 链类型：")
    print("""
1. Stuff Chain（默认）
   - 将所有检索文档塞进一个 prompt
   - 简单快速，但可能超出 token 限制

   qa_chain = RetrievalQA.from_chain_type(
       llm=llm,
       retriever=retriever,
       chain_type="stuff"
   )

2. Refine Chain
   - 逐个处理文档，迭代构建答案
   - 适合长文档总结

   qa_chain = RetrievalQA.from_chain_type(
       llm=llm,
       retriever=retriever,
       chain_type="refine"
   )

3. Map Reduce Chain
   - 先对每个文档单独总结，再综合答案
   - 适合多文档问答

   qa_chain = RetrievalQA.from_chain_type(
       llm=llm,
       retriever=retriever,
       chain_type="map_reduce"
   )

4. Map Rerank Chain
   - 对每个文档打分，选择最相关的
   - 适合需要精准答案的场景

   qa_chain = RetrievalQA.from_chain_type(
       llm=llm,
       retriever=retriever,
       chain_type="map_rerank"
   )
    """)


# ============================================================================
# 示例 5: 完整的 RAG 应用类
# ============================================================================

class RAGApplication:
    """RAG 应用完整示例类"""

    def __init__(self, knowledge_base_path, model_name="gpt-3.5-turbo"):
        self.knowledge_base_path = knowledge_base_path
        self.model_name = model_name
        self.llm = None
        self.vectorstore = None
        self.qa_chain = None
        self._initialize()

    def _initialize(self):
        """初始化 RAG 应用"""
        print("正在初始化 RAG 应用...")

        # 初始化组件
        self.llm = ChatOpenAI(model=self.model_name, temperature=0)
        self.embeddings = OpenAIEmbeddings()

        # 加载和分块文档
        loader = DirectoryLoader(
            self.knowledge_base_path,
            glob="**/*.txt"
        )
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        splits = text_splitter.split_documents(documents)

        # 创建向量存储
        self.vectorstore = Chroma.from_documents(splits, self.embeddings)

        # 创建检索器
        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        # 创建 QA 链
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""基于以下上下文回答问题：

上下文：
{context}

问题：{question}

请提供准确、详细的回答。如果上下文没有相关信息，请说明。"""
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )

    def query(self, question):
        """查询方法"""
        result = self.qa_chain({"query": question})
        return {
            "answer": result["result"],
            "sources": [doc.metadata["source"] for doc in result["source_documents"]]
        }

    def add_document(self, file_path):
        """添加新文档"""
        loader = TextLoader(file_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        splits = text_splitter.split_documents(documents)

        # 添加到向量存储
        self.vectorstore.add_documents(splits)


def rag_application_demo():
    """RAG 应用类演示"""
    print("=" * 60)
    print("示例 5: 完整 RAG 应用类")
    print("=" * 60)

    print("""
class RAGApplication:
    '''完整的 RAG 应用实现'''

    def __init__(self, knowledge_base_path):
        self.knowledge_base_path = knowledge_base_path
        self._initialize()

    def _initialize(self):
        # 初始化所有组件
        pass

    def query(self, question):
        '''执行查询'''
        result = self.qa_chain({"query": question})
        return {
            "answer": result["result"],
            "sources": result["source_documents"]
        }

    def add_document(self, file_path):
        '''动态添加文档'''
        pass

# 使用示例：
rag_app = RAGApplication("knowledge_base/")
result = rag_app.query("Python 的特点是什么？")
print(result["answer"])
print("来源:", result["sources"])
    """)


if __name__ == "__main__":
    print("\n🔍 LangChain RAG 应用示例\n")

    simple_rag_example()
    multi_document_rag()
    custom_retrieval_example()
    rag_chain_types()
    rag_application_demo()

    print("\n" + "=" * 60)
    print("📦 需要安装的依赖：")
    print("pip install langchain langchain-openai")
    print("pip install langchain-community")
    print("pip install chromadb")
    print("=" * 60)
    print("\n💡 接下来可以尝试：")
    print("1. 创建 knowledge_base/ 目录并放入文档")
    print("2. 设置 OPENAI_API_KEY")
    print("3. 运行示例代码")
    print("4. 查看 ragflow-integration.py 了解 RAGFlow 集成")
    print("=" * 60 + "\n")
