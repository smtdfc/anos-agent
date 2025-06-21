from pydantic import BaseModel,Field
from typing import Union

class ProjectQueryAddFileSchema(BaseModel):
  type: str = 'add_file'
  file_name:str
  path:str 

class ProjectQueryRemoveFileSchema(BaseModel):
  type: str = 'remove_file'
  path:str 

class ProjectQueryArgSchema(BaseModel):
  query: Union[ProjectQueryAddFileSchema,ProjectQueryRemoveFileSchema] = Field(..., description='Query')