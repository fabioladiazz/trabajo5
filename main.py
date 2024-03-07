from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(
    title="Trabajo 5",
    description="Fabiola Diaz y Valerie Espinoza",
    version='0.0.1'
)

users = []
tasks = []

@app.post("/register")
async def create_user(username: str, correo: str, password: str):
    user_data = {
        "id": len(users) + 1,
        "username": username,
        "correo": correo,
        "password": password
    }
    users.append(user_data)
    return {
        "id": user_data["id"],
        "username": username,
        "correo": correo,
        "password": password,
        "message": "The user was created successfully",
        "status_code": 201
    }


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/tasks/create")
async def create_task(title: str, description: str, status: str, user_id: int):
    task_data = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": status,
        "user_id": user_id
    }
    tasks.append(task_data)
    return {
        "id": task_data["id"],
        "title": title,
        "description": description,
        "status": status,
        "user_id": user_id,
        "message": "The task was created successfully",
        "status_code": 201
    }

@app.get("/tasks/{user_id}")
async def get_tasks(user_id: int):
    user_tasks = [task for task in tasks if task["user_id"] == user_id]
    if not user_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for the user")
    return user_tasks

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
