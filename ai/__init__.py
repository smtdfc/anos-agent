import os
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from .llm import *
from tools import CreateProjectTool

class AnosAgent:
  def __init__(self,llm):
    self.llm = llm
    self.tools = [
      CreateProjectTool(self),
      CreateItemTool(self)
    ]
    
    self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    self.agent = initialize_agent(
      tools=self.tools,
      llm=llm,
      agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
      memory=self.memory,
      verbose=False,
      handle_parsing_errors=True,
      agent_kwargs={
          "prefix": self.build_prefix('no_project')
      }
    )
  
  def build_prefix(self,project_name: str) -> str:
     return f"""
  You are a Code Agent, specialized in analyzing, generating, and refactoring code.
  You are currently working on the project: {project_name}
  
  Think step by step and follow the exact format below:
  Thought: ...
  Action: ...
  Action Input: ...
  
  Wait for the tool's response before proceeding.
  """

  def change_project(self, project_name: str)-> str:
     self.agent = initialize_agent(
        tools=self.tools,
        llm=self.llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=self.memory,
        verbose=False,
        handle_parsing_errors=True,
        agent_kwargs={
            "prefix": self.build_prefix(project_name)
        }
    )

  def prompt(self,query: str) -> str:
    try:
        return self.agent.run(query)
    except Exception as e:
        print(e)
        return "Error when calling model !"
