from pydantic import BaseModel
from . import department,role

class EmployeeBase(BaseModel):
    name: str
    email: str
    department_id: int
    role_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    department: department.Department
    role: role.Role

    class Config:
        orm_mode = True
