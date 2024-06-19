from sqlalchemy.orm import Session
import models, schemas

# Department CRUD
def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_department(db: Session, department_id: int):
    return db.query(models.Department).filter(models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Department).offset(skip).limit(limit).all()

# Role CRUD
def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Role).offset(skip).limit(limit).all()

# Project CRUD
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()

# Employee CRUD
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(name=employee.name, email=employee.email,
                                  department_id=employee.department_id, role_id=employee.role_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db_employee.department_id = employee.department_id
        db_employee.role_id = employee.role_id
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
