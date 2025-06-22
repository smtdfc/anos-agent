from pydantic import BaseModel, Field
from typing import Union, Literal

class CreateProjectSchema(BaseModel):
    name:str = Field(..., description='Project name')