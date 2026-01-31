from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Task Planner API is running"}

from app.schemas import TaskCreate, TaskResponse
from app.models import Task

tasks = []

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title
    )

    tasks.append(new_task)

    return new_task