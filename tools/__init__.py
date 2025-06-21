from langchain_core.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel
from .schema import *

class ProjectQuery(BaseTool):
  name="anos_project_query"
  description="Access operations with the project including, getting file information, creating files, deleting files"
  args:Type[BaseModel] = ProjectQueryArgSchema

