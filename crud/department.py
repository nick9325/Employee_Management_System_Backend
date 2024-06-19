from sqlalchemy.orm import Session
from models import department as models
from schemas import department as schemas

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

def update_department(db: Session, department: schemas.DepartmentCreate, department_id: int):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    if db_department:
        db_department.name = department.name
        db.commit()
        db.refresh(db_department)
    return db_department

def delete_department(db: Session, department_id: int):
    db_department = db.query(models.Department).filter(models.Department.id == department_id).first()
    if db_department:
        db.delete(db_department)
        db.commit()
    return db_department