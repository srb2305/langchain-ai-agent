import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

responce = model.invoke("Hello LangChain!")

print(responce)