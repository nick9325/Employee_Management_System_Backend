from pydantic import BaseModel

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str
    description: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    email: str
    department_id: int
    role_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    department: Department
    role: Role

    class Config:
        orm_mode = True
