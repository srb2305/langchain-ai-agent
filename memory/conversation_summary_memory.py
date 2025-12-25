#ConversationSummaryMemory is a LangChain memory type that does not store full chat history. 
#Instead, it continuously summarizes the conversation and keeps only the latest summary as memory.

import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationSummaryMemory

api_key = os.getenv("OPENAI_API_KEY")

# temperature=0 → makes output more deterministic (less randomness)
llm = ChatOpenAI(model = "gpt-4o", temperature=0)

summary_memory = ConversationSummaryMemory(llm=llm)

# verbose=True → prints internal prompt, memory, and reasoning (for debugging)
conversation_summary = ConversationChain(llm=llm, memory=summary_memory, verbose=True)

print(conversation_summary.predict(input="Hi, my name is GHAJINI."))
print(conversation_summary.predict(input="I live in indias cleanest city, INDORE."))
print(conversation_summary.predict(input="I love travelling"))
print(conversation_summary.predict(input="Can you remind me where i live?"))