# API CRUD con FastAPI

Este proyecto es una API básica usando FastAPI para gestionar tareas (CRUD).

## Endpoints

- `POST /tasks/`: Crear tarea
- `GET /tasks/`: Listar tareas
- `GET /tasks/{id}`: Obtener una tarea por ID
- `PUT /tasks/{id}`: Actualizar una tarea
- `DELETE /tasks/{id}`: Eliminar una tarea

## Cómo ejecutar

```bash
uvicorn main:app --reload

## url local
##http://127.0.0.1:8000/docs

##url publico
##https://crudfastapi-production.up.railway.app/docs