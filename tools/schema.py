from pydantic import BaseModel, Field
from typing import Union, Literal

class CreateProjectSchema(BaseModel):
    name:str = Field(..., description='Project name')

class CreateItemSchema(BaseModel):
    project:str = Field(..., description='Project name')
    itemType:str = Field(..., description='Item type: "file" or "dir"')
    itemPath:str = Field(..., description='Item path. ex: dir/item_1/..etc')
    itemName:str = Field(..., description='Item name')