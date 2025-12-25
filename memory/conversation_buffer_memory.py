#ConversationBufferMemory is a LangChain memory type that stores the entire conversation history in order, 
# allowing the model to remember previous user and AI messages and maintain context.

#pip install langchain langchain-openai python-dotenv openai
#pip install langchain-classic (not required in latest langchain 1.x+ version)

import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

api_key = os.getenv("OPENAI_API_KEY")

# temperature=0 → makes output more deterministic (less randomness)
llm = ChatOpenAI(model = "gpt-4o", temperature=0)

# ConversationBufferMemory stores the entire conversation history if its True
# return_messages=False → stores memory as plain text (not message objects)
memory = ConversationBufferMemory(return_messages=True)

# verbose=True → prints internal prompt, memory, and reasoning (for debugging)
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

print(conversation.predict(input="Hi, my name is GHAJINI."))
print(conversation.predict(input="How are your today?"))
print(conversation.predict(input="Can you remind me what is my name"))

print(memory.chat_memory.messages)