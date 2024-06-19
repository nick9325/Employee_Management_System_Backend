from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import department as crud
from schemas import department as schemas
from dependency.dependency import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)

@router.get("/{department_id}", response_model=schemas.Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@router.get("/", response_model=list[schemas.Department])
def read_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_departments(db, skip=skip, limit=limit)

@router.put("/{department_id}", response_model=schemas.Department)
def update_department(department_id: int,department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud.update_department(db, department = department, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@router.delete("/{department_id}", response_model=schemas.Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.delete_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department