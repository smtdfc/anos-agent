from langchain_core.tools import BaseTool
from work import  ProjectManagement
from typing import Optional, Type,Union
from pydantic import BaseModel
from .schema import *

class ProjectQuery(BaseTool):
    name: str = "project_query"
    description: str = "Query project: create project, create files, remove files, move files, get project info"

    def _run(
        self, 
        query: Union[
            ProjectQueryAddFileSchema,
            ProjectQueryRemoveFileSchema,
            ProjectQueryInfoSchema,
            ProjectQueryMoveFileSchema,
            ProjectQueryCreateSchema
        ]
    ) -> any:
        try:
            if query.type == 'create_project':
                return ProjectManagement.create(query.project_name)
            return f""
        except Exception as e:
            return f"Error: Unable to complete action: {str(e)}"