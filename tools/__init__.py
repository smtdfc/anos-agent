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

class CreateItemTool(BaseTool):
    name: str = "create_project_item"
    description: str = (
        "Create a new item in project. Input should be a JSON string with fields: "
        '{"project": "...", "itemType": "file|dir", "itemPath": "...", "itemName": "..."}'
    )
    
    _agent: any = PrivateAttr()

    def __init__(self, agent, **kwargs):
        super().__init__(**kwargs)
        self._agent = agent

    def _run(self, input: str) -> str:
        try:
            data = json.loads(input)
            item = CreateItemSchema(**data)

            logging.info(f'[Project:{item.project}] Creating item: {item.itemName}')
            # result = ProjectManagement.create(...)
            # self._agent.change_project(...)
            return f"Successfully created item: {item.itemName} in project {item.project}"
        except Exception as e:
            logging.error(f"CreateItemTool error: {e}")
            return f"Failed to create item. Error: {e}"
