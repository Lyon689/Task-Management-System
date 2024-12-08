from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    priority = Column(Integer, default=1) # 1 = Low, 2 = Medium, 3 = High
    status = Column(Boolean, default=False) # False = Pending, True = Compeleted

