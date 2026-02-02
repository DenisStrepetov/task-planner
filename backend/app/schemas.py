from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    completed: bool

class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True