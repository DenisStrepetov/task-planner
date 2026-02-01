from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.database import engine
from app import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Task Planner API is running"}

from app.schemas import TaskCreate, TaskResponse
from app.models import Task

tasks = []

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task