from pydantic import BaseModel, Field
from typing import Union, Literal

class ProjectQueryAddFileSchema(BaseModel):
    type: Literal['add_file']
    file_name: str
    path: str

class ProjectQueryRemoveFileSchema(BaseModel):
    type: Literal['remove_file']
    path: str

class ProjectQueryMoveFileSchema(BaseModel):
    type: Literal['move_file']
    source: str
    target: str

class ProjectQueryInfoSchema(BaseModel):
    type: Literal['project_info']

class ProjectQueryCreateSchema(BaseModel):
    type: Literal['create_project']
    project_name: str

class ProjectQueryArgSchema(BaseModel):
    query: Union[
        ProjectQueryAddFileSchema,
        ProjectQueryRemoveFileSchema,
        ProjectQueryInfoSchema,
        ProjectQueryMoveFileSchema,
        ProjectQueryCreateSchema
    ] = Field(..., discriminator='type')