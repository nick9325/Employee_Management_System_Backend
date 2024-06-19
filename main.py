from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database
from database import SessionLocal


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Department endpoints
@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, department=department)

@app.get("/departments/{department_id}", response_model=schemas.Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@app.get("/departments/", response_model=list[schemas.Department])
def read_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_departments(db, skip=skip, limit=limit)

# Role endpoints
@app.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db=db, role=role)

@app.get("/roles/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@app.get("/roles/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_roles(db, skip=skip, limit=limit)

# Project endpoints
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)

# Employee endpoints
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.delete("/employees/{employee_id}", response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
