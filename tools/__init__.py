from langchain_core.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel
from .schema import *

class ProjectQuery(BaseTool):
  name:str="anos_project_query"
  description:str="Access operations with the project including, getting file information, creating files, deleting files"
  args:Type[BaseModel] = ProjectQueryArgSchema

