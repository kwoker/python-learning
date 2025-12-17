"""
LangChain 基础示例
演示 LangChain 的核心组件：LLM、Prompt、Chain
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# ============================================================================
# 示例 1: 基础 LLM 调用
# ============================================================================

def basic_llm_example():
    """基础 LLM 调用示例"""
    print("=" * 60)
    print("示例 1: 基础 LLM 调用")
    print("=" * 60)

    # 初始化 LLM（需要设置 OPENAI_API_KEY 环境变量）
    # llm = ChatOpenAI(
    #     model="gpt-3.5-turbo",
    #     temperature=0.7
    # )

    # 如果没有 API 密钥，可以使用模拟响应
    print("LLM 调用示例（需要 API 密钥）:")
    print("""
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    response = llm.invoke("解释一下什么是机器学习")
    print(response.content)
    """)

    print("\n注意: 需要设置环境变量 OPENAI_API_KEY")
    print("export OPENAI_API_KEY='your-api-key-here'\n")


# ============================================================================
# 示例 2: Prompt Template 使用
# ============================================================================

def prompt_template_example():
    """Prompt Template 使用示例"""
    print("=" * 60)
    print("示例 2: Prompt Template")
    print("=" * 60)

    # 创建提示词模板
    template = PromptTemplate(
        input_variables=["topic", "audience"],
        template="请用简单的方式向{audience}解释{topic}。"
    )

    print("Prompt Template 示例:")
    print(template.format(topic="机器学习", audience="初学者"))

    # 结合 LLM 使用（需要 API 密钥）
    print("""
    # 完整示例：
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=template)

    result = chain.run(topic="机器学习", audience="初学者")
    print(result)
    """)


# ============================================================================
# 示例 3: LLMChain 组合使用
# ============================================================================

def llm_chain_example():
    """LLMChain 使用示例"""
    print("=" * 60)
    print("示例 3: LLMChain")
    print("=" * 60)

    # 创建翻译链
    translation_template = PromptTemplate(
        input_variables=["text", "language"],
        template="将以下文本翻译成{language}：{text}"
    )

    print("翻译 Chain 示例:")
    print("""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    translation_chain = LLMChain(
        llm=llm,
        prompt=translation_template
    )

    result = translation_chain.run(
        text="Hello, how are you?",
        language="中文"
    )
    print(result)  # 输出: 你好，你怎么样？
    """)


# ============================================================================
# 示例 4: 对话记忆
# ============================================================================

def conversation_memory_example():
    """对话记忆示例"""
    print("=" * 60)
    print("示例 4: 对话记忆")
    print("=" * 60)

    print("带记忆的对话 Chain 示例:")
    print("""
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    memory = ConversationBufferMemory()

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    # 第一轮对话
    conversation.predict(input="我叫张三")

    # 第二轮对话（模型会记住之前的对话）
    conversation.predict(input="我的名字是什么？")
    # 输出: 你的名字是张三
    """)


# ============================================================================
# 示例 5: 实用工具函数
# ============================================================================

def create_qa_chain():
    """创建问答链的实用函数"""
    print("=" * 60)
    print("示例 5: 实用函数")
    print("=" * 60)

    print("""
def create_qa_bot():
    '''创建一个简单的问答机器人'''
    template = PromptTemplate(
        input_variables=["question"],
        template="作为一个专业的助手，请回答以下问题：\\n{question}"
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo")
    qa_chain = LLMChain(llm=llm, prompt=template)

    return qa_chain

# 使用示例：
qa_bot = create_qa_bot()
answer = qa_bot.run(question="Python 的主要特点是什么？")
print(answer)
    """)


if __name__ == "__main__":
    print("\n🚀 LangChain 基础示例\n")

    basic_llm_example()
    prompt_template_example()
    llm_chain_example()
    conversation_memory_example()
    create_qa_chain()

    print("\n" + "=" * 60)
    print("📚 接下来可以尝试：")
    print("1. 安装 langchain-openai: pip install langchain-openai")
    print("2. 设置 OPENAI_API_KEY 环境变量")
    print("3. 取消注释代码中的实际调用")
    print("4. 查看 langchain-rag-examples.py 了解 RAG 应用")
    print("=" * 60)
