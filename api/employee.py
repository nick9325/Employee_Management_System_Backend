from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import employee as crud
from schemas.employee import Employee, EmployeeCreate
from dependency.dependency import get_db
from core.security import get_current_user
from schemas.auth import User

router = APIRouter()


@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.create_employee(db=db, employee=employee)

@router.get("/{employee_id}", response_model=Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.get("/", response_model=list[Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_employees(db, skip=skip, limit=limit)

@router.get("/department_name/{department_name}", response_model=list[Employee])
def read_employees_by_department(department_name:str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    employees = crud.get_employees_by_department_name(db, department_name = department_name)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found for this department")
    return employees

@router.get("/role_name/{role_name}", response_model=list[Employee])
def read_employees_by_role_name(role_name:str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    employees = crud.get_employees_by_role_name(db, role_name = role_name)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found for this department")
    return employees

@router.get("/project_name/{project_name}", response_model=list[Employee])
def read_employees_by_project(project_name:str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    employees = crud.get_employees_by_project_name(db, project_name = project_name)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found for this project")
    return employees


@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.delete("/{employee_id}", response_model=Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_employee = crud.delete_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

