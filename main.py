from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo para recibir la tarea (sin id)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Modelo para mostrar la tarea (con id)
class Task(TaskCreate):
    id: int

# Simulación de base de datos
fake_db: List[Task] = []
task_id_counter = 1  # Contador global para IDs

# Crear una nueva tarea
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    fake_db.append(new_task)
    task_id_counter += 1
    return new_task

# Obtener todas las tareas
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return fake_db

# Obtener una tarea por ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in fake_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Actualizar una tarea
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_data: TaskCreate):
    for index, task in enumerate(fake_db):
        if task.id == task_id:
            updated_task = Task(id=task_id, **updated_data.dict())
            fake_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Eliminar una tarea
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(fake_db):
        if task.id == task_id:
            del fake_db[index]
            return {"mensaje": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
