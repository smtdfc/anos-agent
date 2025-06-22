from langchain_core.tools import BaseTool
from work import ProjectManagement
from typing import Union,Type
from pydantic import BaseModel, Field
from .schema import *
import logging

class CreateProjectTool(BaseTool):
    name: str = "create_project"
    description: str = "Create a new project"
    args_schema: Type[BaseModel] = CreateProjectSchema

    def __init__(self, agent, **kwargs):
        self.agent = agent 
        super().__init__(**kwargs)  

    def _run(self, name: str) -> any:
        logging.info(f'Creating project: {name}')
        result = self.project_manager.create(name)
        self.agent.change_project(name)
        return result