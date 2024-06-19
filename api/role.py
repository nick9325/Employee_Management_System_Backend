from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import role as crud
from schemas import role as schemas
from dependency.dependency import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db=db, role=role)

@router.get("/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.get("/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_roles(db, skip=skip, limit=limit)


