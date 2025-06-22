from langchain_core.tools import BaseTool
from work import ProjectManagement
from typing import Union,Type
from pydantic import BaseModel, Field
from .schema import *


class ProjectQuery(BaseTool):
    name: str = "project_query"
    description: str = "Query project: create project, create files, remove files, move files, get project info"
    args_schema: Type[BaseModel] = ProjectQueryArgSchema  

    def _run(self, query: BaseModel) -> any:
        try:
            query_obj = query.query 
            if query_obj.type == 'create_project':
                logging.info(f'Creating project: {query_obj.project_name}')
                return ProjectManagement.create(query_obj.project_name)
            return f"Query type '{query_obj.type}' unsupported !"
        except Exception as e:
            return f"Error: Unable to complete action: {str(e)}"