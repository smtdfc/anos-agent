from models import Project 
from datetime import datetime
import os
import json


def create_config_file(path: str, name:str) -> None:
  config ={
    "name":name,
    "create_time":datetime.now()
  }
  
  with open(f'{path}/.anos_agent.json',mode='w+') as f:
    f.write(json.dumps(config))

class ProjectManagement:
  @staticmethod
  def create(name: str) -> Project:
    if os.path.exists(name) and os.path.isdir(name):
      raise Exception(f'Cannot create project: Dir {name} are ready exist !')
    
    os.mkdir(name)
    create_config_file(f'./${name}',name)
    
    return Project(
      name=name
    )