from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import role as crud
from schemas import role as schemas
from dependency.dependency import get_db
from core.security import get_current_user
from schemas.auth import User

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.create_role(db=db, role=role)

@router.get("/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.get("/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_roles(db, skip=skip, limit=limit)

@router.put("/{role_id}", response_model=schemas.Role)
def update_role(role_id: int, role: schemas.RoleCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_role = crud.update_role(db, role=role, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/{role_id}", response_model=schemas.Role)
def delete_role(role_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_role = crud.delete_role(db,role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role


