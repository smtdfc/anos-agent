from langchain_core.tools import BaseTool
from typing import Optional, Type,Union
from pydantic import BaseModel
from .schema import *

class ProjectQuery(BaseTool):
    name: str = "project_query"
    description: str = "Query project: create files, remove files, move files, get project info"

    def _run(
        self, 
        query: Union[
            ProjectQueryAddFileSchema,
            ProjectQueryRemoveFileSchema,
            ProjectQueryInfoSchema,
            ProjectQueryMoveFileSchema
    ]) -> str:
        return f""