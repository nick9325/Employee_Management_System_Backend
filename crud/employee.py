from sqlalchemy.orm import Session
from models.employee import Employee as EmployeeModel
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
