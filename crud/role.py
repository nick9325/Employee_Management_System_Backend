from sqlalchemy.orm import Session
from models import role as models
from schemas import role as schemas

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

def update_role(db: Session, role:schemas.RoleCreate, role_id: int):
    db_role = db.query(models.Role).filter(models.Role.id == role_id).first()

    if db_role:
        db_role.name = role.name
        db.commit()
        db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = db.query(models.Role).filter(models.Role.id == role_id)

    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
