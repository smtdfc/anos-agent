from langchain_core.tools import BaseTool
from work import ProjectManagement
from typing import Union,Type
from pydantic import BaseModel, Field
from .schema import *
import logging

from pydantic import PrivateAttr

class CreateProjectTool(BaseTool):
    name: str = "create_project"
    description: str = "Create a new project"
    args_schema: Type[BaseModel] = CreateProjectSchema

    _agent: any = PrivateAttr()

    def __init__(self, agent, **kwargs):
        super().__init__(**kwargs)
        self._agent = agent

    def _run(self, name: str) -> any:
        logging.info(f'Creating project: {name}')
        result = ProjectManagement.create(name)
        self._agent.change_project(name)
        return result