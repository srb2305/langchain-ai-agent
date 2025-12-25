#ConversationSummaryBufferMemory is a LangChain memory type that stores recent conversation messages in full 
# and older messages as a summarized version, keeping context while controlling token usage.

import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationSummaryBufferMemory

api_key = os.getenv("OPENAI_API_KEY")

# temperature=0 → makes output more deterministic (less randomness)
llm = ChatOpenAI(model = "gpt-4o", temperature=0)

buffer_summary_memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)

# verbose=True → prints internal prompt, memory, and reasoning (for debugging)
conversation_summary_buf = ConversationChain(llm=llm, memory=buffer_summary_memory, verbose=True)

print(conversation_summary_buf.predict(input="Hi, my name is GHAJINI."))
print(conversation_summary_buf.predict(input="I am planing a trip to thailand."))
print(conversation_summary_buf.predict(input="Remind me where i told you about my hobbies?"))