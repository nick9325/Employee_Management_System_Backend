from fastapi import FastAPI
from api import employee, department, role, project, auth
from models import department as deptModel,employee as employeeModel,project as projectModel,role as roleModel
from db.database import engine


deptModel.Base.metadata.create_all(bind=engine)
employeeModel.Base.metadata.create_all(bind=engine)
projectModel.Base.metadata.create_all(bind=engine)
roleModel.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Mounting API routers
app.include_router(employee.router, prefix="/employees", tags=["employees"])
app.include_router(department.router, prefix="/departments", tags=["departments"])
app.include_router(role.router, prefix="/roles", tags=["roles"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(auth.router, tags=["Authentication"])
