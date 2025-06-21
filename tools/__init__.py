from langchain_core.tools import BaseTool
from typing import Optional, Type,Union
from pydantic import BaseModel
from .schema import *

class ProjectQuery(BaseTool):
    name: str = "project_query"
    description: str = "Query project"

    def _run(self, query: Union[ProjectQueryAddFileSchema,ProjectQueryRemoveFileSchema]) -> str:
        return f""