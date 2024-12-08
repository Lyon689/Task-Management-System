from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    priority: int
    status: bool

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: int | None = None
    status: bool | None = None

class Task(TaskBase):
    id:int


    class Config:
        orm_mode = True