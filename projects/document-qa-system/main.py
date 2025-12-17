"""
文档问答系统 - 实战项目
基于 LangChain 和 RAGFlow 的智能文档问答系统

功能特性：
- 支持多种文档格式（PDF、TXT、DOCX）
- 智能文本分块
- 向量化存储和检索
- 多轮对话
- 答案溯源
- Web 界面
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# 添加项目路径
sys.path.append(str(Path(__file__).parent))

# ============================================================================
# 配置管理
# ============================================================================

class Config:
    """系统配置"""

    # LLM 配置
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME = "gpt-3.5-turbo"
    TEMPERATURE = 0.1

    # 文档处理配置
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    MAX_CHUNKS_PER_QUERY = 5

    # 检索配置
    SIMILARITY_THRESHOLD = 0.7

    # 存储配置
    VECTOR_STORE_PATH = "./data/vectorstore"
    KNOWLEDGE_BASE_PATH = "./data/knowledge"

    # RAGFlow 配置（可选）
    RAGFLOW_BASE_URL = os.getenv("RAGFLOW_BASE_URL", "http://localhost:9380")
    RAGFLOW_API_KEY = os.getenv("RAGFLOW_API_KEY", "")

    # Web 配置
    WEB_HOST = "127.0.0.1"
    WEB_PORT = 8000


# ============================================================================
# 文档处理器
# ============================================================================

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentProcessor:
    """文档处理器"""

    @staticmethod
    def load_document(file_path: str) -> List:
        """
        加载文档

        Args:
            file_path: 文档路径

        Returns:
            文档内容列表
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 根据文件扩展名选择加载器
        if file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
        elif file_path.suffix.lower() == ".docx":
            loader = UnstructuredWordDocumentLoader(str(file_path))
        elif file_path.suffix.lower() == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")
        else:
            raise ValueError(f"不支持的文件格式: {file_path.suffix}")

        return loader.load()

    @staticmethod
    def split_text(documents: List, chunk_size: int = 500, chunk_overlap: int = 50) -> List:
        """
        文本分块

        Args:
            documents: 文档列表
            chunk_size: 块大小
            chunk_overlap: 重叠大小

        Returns:
            分块后的文档列表
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?"]
        )
        return text_splitter.split_documents(documents)

    @staticmethod
    def process_file(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List:
        """
        完整处理文档

        Args:
            file_path: 文件路径
            chunk_size: 块大小
            chunk_overlap: 重叠大小

        Returns:
            处理后的文档块
        """
        # 加载文档
        documents = DocumentProcessor.load_document(file_path)

        # 文本分块
        splits = DocumentProcessor.split_text(documents, chunk_size, chunk_overlap)

        # 添加元数据
        for doc in splits:
            doc.metadata["source_file"] = Path(file_path).name

        return splits


# ============================================================================
# 向量存储管理
# ============================================================================

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

class VectorStoreManager:
    """向量存储管理器"""

    def __init__(self, persist_directory: str):
        """
        初始化向量存储管理器

        Args:
            persist_directory: 存储目录
        """
        self.persist_directory = persist_directory
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None

    def create_vectorstore(self, documents: List) -> Chroma:
        """
        创建向量存储

        Args:
            documents: 文档列表

        Returns:
            向量存储对象
        """
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        return self.vectorstore

    def load_vectorstore(self) -> Chroma:
        """
        加载现有向量存储

        Returns:
            向量存储对象
        """
        if os.path.exists(self.persist_directory):
            self.vectorstore = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        return self.vectorstore

    def add_documents(self, documents: List) -> None:
        """
        添加文档到向量存储

        Args:
            documents: 文档列表
        """
        if self.vectorstore is None:
            self.create_vectorstore(documents)
        else:
            self.vectorstore.add_documents(documents)

    def similarity_search(self, query: str, k: int = 5) -> List:
        """
        相似度搜索

        Args:
            query: 查询文本
            k: 返回文档数量

        Returns:
            相关文档列表
        """
        if self.vectorstore is None:
            raise ValueError("向量存储未初始化")

        return self.vectorstore.similarity_search(query, k=k)


# ============================================================================
# RAG 问答系统
# ============================================================================

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

class DocumentQASystem:
    """文档问答系统"""

    def __init__(self, config: Config):
        """
        初始化问答系统

        Args:
            config: 配置对象
        """
        self.config = config
        self.vectorstore_manager = VectorStoreManager(config.VECTOR_STORE_PATH)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=config.MODEL_NAME,
            temperature=config.TEMPERATURE
        )

        # 创建提示模板
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""基于以下上下文信息回答问题。

上下文信息：
{context}

问题：{question}

请提供准确、详细的回答。如果上下文没有相关信息，请说明。回答应基于提供的上下文。"""
        )

        self.qa_chain = None

    def build_qa_chain(self) -> ConversationalRetrievalChain:
        """
        构建问答链

        Returns:
            问答链对象
        """
        if self.vectorstore_manager.vectorstore is None:
            raise ValueError("向量存储未初始化")

        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            memory=self.memory,
            retriever=self.vectorstore_manager.vectorstore.as_retriever(
                search_kwargs={"k": self.config.MAX_CHUNKS_PER_QUERY}
            ),
            combine_docs_chain_kwargs={"prompt": self.prompt}
        )

        return self.qa_chain

    def add_knowledge_base(self, file_paths: List[str]) -> None:
        """
        添加知识库文档

        Args:
            file_paths: 文件路径列表
        """
        all_documents = []

        for file_path in file_paths:
            try:
                documents = DocumentProcessor.process_file(
                    file_path,
                    self.config.CHUNK_SIZE,
                    self.config.CHUNK_OVERLAP
                )
                all_documents.extend(documents)
                print(f"✓ 已处理: {file_path}")
            except Exception as e:
                print(f"✗ 处理失败: {file_path}, 错误: {e}")

        # 添加到向量存储
        self.vectorstore_manager.add_documents(all_documents)
        print(f"\n总共处理了 {len(all_documents)} 个文档块")

    def query(self, question: str) -> Dict[str, Any]:
        """
        问答查询

        Args:
            question: 问题

        Returns:
            回答结果
        """
        if self.qa_chain is None:
            self.build_qa_chain()

        result = self.qa_chain({"question": question})

        # 获取相关文档
        docs = self.vectorstore_manager.similarity_search(question, k=3)
        sources = [doc.metadata.get("source_file", "未知来源") for doc in docs]

        return {
            "answer": result["answer"],
            "sources": list(set(sources)),  # 去重
            "chat_history": result.get("chat_history", [])
        }

    def chat(self, question: str) -> str:
        """
        简单对话（返回字符串）

        Args:
            question: 问题

        Returns:
            回答文本
        """
        result = self.query(question)
        return result["answer"]


# ============================================================================
# 示例使用
# ============================================================================

def main():
    """主函数 - 演示系统使用"""
    print("=" * 60)
    print("📚 文档问答系统演示")
    print("=" * 60)

    # 检查 API 密钥
    if not Config.OPENAI_API_KEY:
        print("⚠️  请设置 OPENAI_API_KEY 环境变量")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return

    # 创建配置
    config = Config()

    # 初始化问答系统
    qa_system = DocumentQASystem(config)

    # 创建目录
    os.makedirs(config.KNOWLEDGE_BASE_PATH, exist_ok=True)
    os.makedirs(config.VECTOR_STORE_PATH, exist_ok=True)

    # 示例文档（需要先创建）
    sample_docs = [
        "data/knowledge/python-guide.txt",
        "data/knowledge/ml-basics.txt"
    ]

    print("\n1. 准备知识库...")
    if not Path(sample_docs[0]).exists():
        print(f"⚠️  示例文档不存在: {sample_docs[0]}")
        print("请先创建示例文档再运行")
        return

    # 添加知识库
    qa_system.add_knowledge_base(sample_docs)

    print("\n" + "=" * 60)
    print("💬 开始问答（输入 'quit' 退出）")
    print("=" * 60)

    while True:
        question = input("\n🤔 问题: ")

        if question.lower() == 'quit':
            break

        try:
            result = qa_system.query(question)
            print(f"\n💡 回答: {result['answer']}")
            print(f"📚 来源: {', '.join(result['sources'])}")
        except Exception as e:
            print(f"❌ 错误: {e}")


if __name__ == "__main__":
    main()
