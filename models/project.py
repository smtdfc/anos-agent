from pydantic import BaseModel,Field

class Project:
  def __init__(self,name:str):
    self.name = name