from pydantic import BaseModel,Field
from typing import Union

class ProjectQueryAddFileSchema(BaseModel):
  type: str = 'add_file'
  file_name:str
  path:str 

class ProjectQueryRemoveFileSchema(BaseModel):
  type: str = 'remove_file'
  path:str 

class ProjectQueryMoveFileSchema(BaseModel):
  type: str = 'move_file'
  source:str 
  target:str 

class ProjectQueryInfoSchema(BaseModel):
  type: str = 'project_info'

class ProjectQueryCreateSchema(BaseModel):
  type: str = 'create_project'
  project_name:str



class ProjectQueryArgSchema(BaseModel):
  query: Union[
    ProjectQueryAddFileSchema,
    ProjectQueryRemoveFileSchema,
    ProjectQueryInfoSchema,
    ProjectQueryMoveFileSchema,
    ProjectQueryCreateSchema
  ] = Field(..., description='Query')