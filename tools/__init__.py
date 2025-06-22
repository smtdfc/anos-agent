from langchain_core.tools import BaseTool
from work import ProjectManagement
from typing import Union,Type
from pydantic import BaseModel, Field
from .schema import *


class ProjectQuery(BaseTool):
    name: str = "project_query"
    description:str = (
        "Use this tool to manage a project. The `query` field must be an object with a `type` key.\n"
        "Available query types:\n"
        "- 'create_project': create a project, requires 'project_name'\n"
        "- 'add_file': add a file, requires 'file_name' and 'path'\n"
        "- 'remove_file': remove a file, requires 'path'\n"
        "- 'move_file': move a file, requires 'source' and 'target'\n"
        "- 'project_info': get project info, no additional fields\n\n"
        "**Examples**:\n"
        "- To create a project: `{'query': {'type': 'create_project', 'project_name': 'aurora'}}`\n"
        "- To add a file: `{'query': {'type': 'add_file', 'file_name': 'main.py', 'path': '/src'}}`\n"
    )
    
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