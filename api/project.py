from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import project as crud
from crud import employee as emp_crud
from schemas import project as schemas
from dependency.dependency import get_db
from core.security import get_current_user
from schemas.auth import User

router = APIRouter()


@router.post("/assign-project/", response_model=schemas.Project)
def assign_project(project_assign: schemas.ProjectAssign, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        project = emp_crud.assign_project_to_employees(db, project_assign.project_id, project_assign.employee_ids)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return project

@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.create_project(db=db, project=project)

@router.get("/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.get("/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_projects(db, skip=skip, limit=limit)

@router.put("/{project_id}",response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_project = crud.update_project(db, project=project, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_project = crud.delete_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project