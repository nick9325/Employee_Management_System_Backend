from sqlalchemy import Table, Column, Integer, ForeignKey
from db.database import Base

association_table = Table(
    "employee_project",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id")),
    Column("project_id", Integer, ForeignKey("projects.id"))
)
