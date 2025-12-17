"""
RAGFlow 集成示例
演示如何使用 RAGFlow 构建企业级 RAG 应用
"""

import requests
import json
from typing import List, Dict, Any

# ============================================================================
# RAGFlow API 客户端
# ============================================================================

class RAGFlowClient:
    """RAGFlow API 客户端"""

    def __init__(self, base_url: str, api_key: str):
        """
        初始化 RAGFlow 客户端

        Args:
            base_url: RAGFlow 服务器地址，如 "http://localhost:9380"
            api_key: API 密钥
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_dataset(self, name: str, description: str = "") -> Dict[str, Any]:
        """
        创建数据集

        Args:
            name: 数据集名称
            description: 数据集描述

        Returns:
            创建的数据集信息
        """
        url = f"{self.base_url}/api/v1/dataset"
        payload = {
            "name": name,
            "description": description
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def upload_document(self, dataset_id: str, file_path: str) -> Dict[str, Any]:
        """
        上传文档到数据集

        Args:
            dataset_id: 数据集 ID
            file_path: 文档路径

        Returns:
            上传结果
        """
        url = f"{self.base_url}/api/v1/dataset/{dataset_id}/document"
        # 注意：实际实现需要处理文件上传
        print(f"上传文档: {file_path} 到数据集: {dataset_id}")
        return {"status": "success", "document_id": "doc_123"}

    def parse_document(self, dataset_id: str, document_id: str) -> Dict[str, Any]:
        """
        解析文档

        Args:
            dataset_id: 数据集 ID
            document_id: 文档 ID

        Returns:
            解析结果
        """
        url = f"{self.base_url}/api/v1/dataset/{dataset_id}/document/{document_id}/parse"
        payload = {
            "chunk_method": "manual",  # 或 "automatic"
            "chunk_method": {
                "chunk_token_count": 128,
                "chunk_overlap_rate": 0.2
            }
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def create_chat(self, dataset_ids: List[str], name: str) -> Dict[str, Any]:
        """
        创建聊天会话

        Args:
            dataset_ids: 关联的数据集 ID 列表
            name: 聊天会话名称

        Returns:
            创建的聊天会话信息
        """
        url = f"{self.base_url}/api/v1/chat"
        payload = {
            "name": name,
            "dataset_ids": dataset_ids,
            "llm": {
                "model_name": "gpt-3.5-turbo",
                "temperature": 0.1
            }
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def chat(self, chat_id: str, question: str, history: List[Dict] = None) -> Dict[str, Any]:
        """
        发送聊天消息

        Args:
            chat_id: 聊天会话 ID
            question: 问题
            history: 对话历史（可选）

        Returns:
            AI 回复
        """
        url = f"{self.base_url}/api/v1/chat/{chat_id}/question"
        payload = {
            "question": question,
            "history": history or []
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()


# ============================================================================
# 示例 1: 基本的 RAGFlow 使用流程
# ============================================================================

def ragflow_basic_workflow():
    """RAGFlow 基本工作流程示例"""
    print("=" * 60)
    print("示例 1: RAGFlow 基本工作流程")
    print("=" * 60)

    print("""
RAGFlow 工作流程：
1. 创建数据集 → 2. 上传文档 → 3. 解析文档 → 4. 创建聊天 → 5. 开始对话

示例代码：

# 1. 初始化客户端
client = RAGFlowClient(
    base_url="http://localhost:9380",
    api_key="your-api-key"
)

# 2. 创建数据集
dataset = client.create_dataset(
    name="技术文档库",
    description="存储技术文档和教程"
)
dataset_id = dataset["data"]["id"]

# 3. 上传文档
client.upload_document(dataset_id, "docs/python-guide.txt")
client.upload_document(dataset_id, "docs/ml-intro.txt")

# 4. 解析文档（可选，等待解析完成）
client.parse_document(dataset_id, "doc_123")

# 5. 创建聊天会话
chat = client.create_chat(
    dataset_ids=[dataset_id],
    name="技术助手"
)
chat_id = chat["data"]["id"]

# 6. 开始对话
response = client.chat(chat_id, "Python 有哪些特点？")
print(response["data"]["answer"])
    """)


# ============================================================================
# 示例 2: 批量文档处理
# ============================================================================

def batch_document_processing():
    """批量文档处理示例"""
    print("=" * 60)
    print("示例 2: 批量文档处理")
    print("=" * 60)

    print("""
批量处理文档的最佳实践：

def process_documents(client, dataset_id, doc_paths):
    '''批量处理文档'''
    results = []

    for doc_path in doc_paths:
        try:
            # 上传文档
            upload_result = client.upload_document(dataset_id, doc_path)
            doc_id = upload_result["document_id"]

            # 解析文档
            parse_result = client.parse_document(dataset_id, doc_id)

            results.append({
                "document": doc_path,
                "status": "success",
                "chunks": parse_result["data"]["chunk_count"]
            })

            print(f"✓ 已处理: {doc_path}")

        except Exception as e:
            results.append({
                "document": doc_path,
                "status": "error",
                "error": str(e)
            })
            print(f"✗ 处理失败: {doc_path}, 错误: {e}")

    return results

# 使用示例：
doc_paths = [
    "docs/python-basics.txt",
    "docs/advanced-python.txt",
    "docs/ml-guide.txt"
]
results = process_documents(client, dataset_id, doc_paths)
    """)


# ============================================================================
# 示例 3: 多轮对话
# ============================================================================

def multi_turn_conversation():
    """多轮对话示例"""
    print("=" * 60)
    print("示例 3: 多轮对话")
    print("=" * 60)

    print("""
实现多轮对话：

def chat_with_history(client, chat_id):
    '''带历史记录的多轮对话'''
    history = []

    while True:
        question = input("\\n请输入问题 (输入 'quit' 退出): ")

        if question.lower() == 'quit':
            break

        # 发送消息并获取回复
        response = client.chat(chat_id, question, history)

        # 更新历史记录
        history.append({"question": question})
        history.append({"answer": response["data"]["answer"]})

        print(f"\\n🤖 AI: {response['data']['answer']}")
        print(f"📚 来源: {response['data']['reference']}")

    return history

# 开始多轮对话
chat_history = chat_with_history(client, chat_id)
    """)


# ============================================================================
# 示例 4: LangChain + RAGFlow 集成
# ============================================================================

def langchain_ragflow_integration():
    """LangChain 与 RAGFlow 集成示例"""
    print("=" * 60)
    print("示例 4: LangChain + RAGFlow 集成")
    print("=" * 60)

    print("""
结合 LangChain 的灵活性和 RAGFlow 的企业级能力：

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class HybridRAGSystem:
    '''混合 RAG 系统'''

    def __init__(self, ragflow_client, llm):
        self.ragflow = ragflow_client
        self.llm = llm
        self.template = PromptTemplate(
            input_variables=["context", "question"],
            template='''基于以下上下文回答问题：

上下文：
{context}

问题：{question}

请提供专业、详细的回答。'''
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.template)

    def query(self, chat_id, question):
        # 1. 从 RAGFlow 获取上下文
        ragflow_response = self.ragflow.chat(chat_id, question)

        # 2. 使用 LangChain 生成最终答案
        final_answer = self.chain.run(
            context=ragflow_response["data"]["answer"],
            question=question
        )

        return {
            "answer": final_answer,
            "sources": ragflow_response["data"]["reference"]
        }

# 使用示例：
hybrid_system = HybridRAGSystem(ragflow_client, llm)
result = hybrid_system.query(chat_id, "解释机器学习的基本概念")
    """)


# ============================================================================
# 示例 5: 实际部署考虑
# ============================================================================

def deployment_considerations():
    """RAGFlow 部署注意事项"""
    print("=" * 60)
    print("示例 5: 部署注意事项")
    print("=" * 60)

    print("""
部署 RAGFlow 的最佳实践：

1. Docker 部署
   docker pull ragflow/ragflow:latest
   docker run -d -p 9380:9380 ragflow/ragflow

2. 环境配置
   - 内存: 建议 8GB+
   - 存储: SSD，足够的磁盘空间存储向量
   - GPU: 可选，加速嵌入和推理

3. 安全配置
   - 使用 API Key 认证
   - 配置 HTTPS
   - 限制访问 IP

4. 性能优化
   - 合理设置 chunk_size (128-512 tokens)
   - 调整 chunk_overlap (0.1-0.3)
   - 使用异步处理批量文档

5. 监控和维护
   - 监控 API 响应时间
   - 定期清理过期数据
   - 备份向量数据库

6. 成本控制
   - 设置 token 使用限制
   - 实施缓存策略
   - 优化检索参数（k 值）
    """)


if __name__ == "__main__":
    print("\n🚀 RAGFlow 集成示例\n")

    ragflow_basic_workflow()
    batch_document_processing()
    multi_turn_conversation()
    langchain_ragflow_integration()
    deployment_considerations()

    print("\n" + "=" * 60)
    print("📦 RAGFlow 安装和启动：")
    print("1. 下载 RAGFlow: https://ragflow.io/download")
    print("2. Docker 部署: docker run -d -p 9380:9380 ragflow/ragflow")
    print("3. 访问控制台: http://localhost:9380")
    print("4. 获取 API Key")
    print("=" * 60)
    print("\n💡 学习建议：")
    print("1. 先用 Docker 部署 RAGFlow 体验")
    print("2. 通过 Web 界面熟悉功能")
    print("3. 再使用 API 进行开发")
    print("4. 对比 LangChain 和 RAGFlow 的适用场景")
    print("=" * 60 + "\n")
