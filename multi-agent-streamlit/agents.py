from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# Chat-based LLM (CORRECT)
llm = ChatOpenAI(
    model="gpt-4o",   # or gpt-4 / gpt-3.5-turbo
    temperature=0.2
)

def researcher_agent(question: str) -> str:
    messages = [
        SystemMessage(content="You are a research agent. Gather factual, concise information."),
        HumanMessage(content=question)
    ]
    return llm.invoke(messages).content


def analyst_agent(research: str, question: str) -> str:
    messages = [
        SystemMessage(content="You are an analyst. Structure and interpret the research."),
        HumanMessage(content=f"Research:\n{research}\n\nQuestion:\n{question}")
    ]
    return llm.invoke(messages).content


def critic_agent(draft: str) -> str:
    messages = [
        SystemMessage(content="You are a critic. Identify errors, assumptions, or missing context."),
        HumanMessage(content=draft)
    ]
    return llm.invoke(messages).content


def final_agent(research: str, analysis: str, critique: str) -> str:
    messages = [
        SystemMessage(content="You are a senior AI assistant producing the final answer."),
        HumanMessage(content=f"""
Research:
{research}

Analysis:
{analysis}

Critique:
{critique}

Produce a clear, accurate final response.
""")
    ]
    return llm.invoke(messages).content
