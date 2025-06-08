import os
from utils import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

def call_llm(query, project_context):
    course_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2N2E4YTY5ZGU5OTI3Yjg1N2Q1YTYzOTgiLCJleHAiOjE3NTQ2MTEyMDB9.QqqmLjBXJXntJEaFe1w8QHj18jdVKBCeqErJ2kgBhuU'
    llm = ChatOpenAI(temperature=0.0, course_api_key=course_api_key)

    prompt = (
        f"Вот информация о студенте:\n{query}\n\n"
        f"Ниже представлены проекты. Выбери 3 наиболее релевантных.\n\n"
        f"{project_context}\n\n"
        f"Ответи списком с названиями 3 проектов."
    )

    messages = [
        SystemMessage(content="Ты выступаешь как рекомендательная система."),
        HumanMessage(content=prompt)
    ]
    return llm(messages).content.strip()
