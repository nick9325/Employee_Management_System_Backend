from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str
    age: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
