from typing import List

from pydantic import BaseModel
from pydantic.fields import Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
	"""Schema for Source used by the agent"""
	url:str = Field(description="URL of the source")

class AgentResponse(BaseModel):
	"""Schema for AgentResponse used by the agent"""
	answer:str = Field(description="The agent's answer to the question")
	sources: List[Source] = Field(default_factory=list, description="List of sources to use")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format= AgentResponse)
def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":[HumanMessage(content="search for 3 jobs posting for an ai engineer using langchain in Tel Aviv area on linkedin and list their details")]})
    print(result)


if __name__ == "__main__":
    main()
