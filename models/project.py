from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy.orm import relationship
from models.employee_project import association_table

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)

    employees = relationship("Employee", secondary=association_table, back_populates="projects")

