from pydantic import BaseModel
from typing import List


class ProjectBase(BaseModel):
    name: str
    description: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class ProjectAssign(BaseModel):
    project_id: int
    employee_ids: List[int]

