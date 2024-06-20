from sqlalchemy.orm import Session
from models.employee import Employee as EmployeeModel
from models.department import Department as DeptModel
from models.project import Project as ProjectModel
from models.role import Role as RoleModel
from schemas.employee import EmployeeCreate

def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = EmployeeModel(name=employee.name, email=employee.email,
                                  department_id=employee.department_id, role_id=employee.role_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EmployeeModel).offset(skip).limit(limit).all()

def get_employees_by_department_name(db: Session,department_name:str):
    return db.query(EmployeeModel).join(DeptModel).filter(DeptModel.name == department_name).all()

def get_employees_by_role_name(db: Session,role_name:str):
    return db.query(EmployeeModel).join(RoleModel).filter(RoleModel.name == role_name).all()

def get_employees_by_project_name(db: Session,project_name:str):
    return db.query(EmployeeModel).join(EmployeeModel.projects).filter(ProjectModel.name == project_name).all()

def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    db_employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db_employee.department_id = employee.department_id
        db_employee.role_id = employee.role_id
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee


def assign_project_to_employees(db: Session, project_id: int, employee_ids: list[int]):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise ValueError("Project not found")
    
    employees = db.query(EmployeeModel).filter(EmployeeModel.id.in_(employee_ids)).all()
    if not employees:
        raise ValueError("Employees not found")

    project.employees.extend(employees)
    db.commit()
    db.refresh(project)
    return project