import os
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from .llm import *
from tools import ProjectQuery

custom_prefix = """
Bạn là một agent chuyên sử dụng tool. Hãy suy nghĩ theo từng bước và dùng đúng định dạng sau:
Thought: ...
Action: ...
Action Input: ...

Sau đó chờ kết quả từ tool rồi mới tiếp tục.
"""


class AnosAgent:
  def __init__(self,llm):
    self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    self.agent = initialize_agent(
      tools=[
        ProjectQuery()
      ],
      llm=llm,
      agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
      memory=self.memory,
      verbose=False,
      handle_parsing_errors=True,
      agent_kwargs={
          "prefix": custom_prefix
      }
    )
  
  def prompt(self,query: str) -> str:
    try:
        return self.agent.run(query)
    except Exception as e:
        print(e)
        return "Error when calling model !"
