import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from pprint import pprint

from system_prompt import system_prompt

api_key = os.getenv("OPENAI_API_KEY")

# Wikipedia Tool Setup
api_wrapper = WikipediaAPIWrapper()
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
llm = ChatOpenAI(model="gpt-4o")

#create the agent (Execute logic to built-in)

agent = create_agent(
    model = llm,
    tools = [wiki_tool],

    system_prompt=system_prompt
)

#use the agent directly

#response = agent.invoke({"messages": [("user","Who are you ?")]})
#response = agent.invoke({"messages": [("user","Shani dev ke sath surya devta ki pooja ya name le sakte hai ya nhi ?")]})

response = agent.invoke({
    "messages": [
        ("user", "Shani dev ke sath surya devta ki pooja ya name le sakte hai ya nhi ?"),
        ("user", "shani dev and surya dev ka beej mantra btaiye ?")
    ]
})

print(response["messages"][-1].content)
#pprint(response) #Pretty Print
