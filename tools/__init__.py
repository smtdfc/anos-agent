from langchain_core.tools import BaseTool
from work import ProjectManagement
from typing import Union,Type
from pydantic import BaseModel, Field
from .schema import *


class CreateProjectTool(BaseTool):
    name: str = "create_project"
    description:str = 'Create a new project'
    
    args_schema: Type[BaseModel] = CreateProjectSchema  

    def _run(self, name:str) -> any:
        logging.info(f'Creating project: {name}')
        return ProjectManagement.create(name)
