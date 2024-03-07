from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(
    title="Trabajo 5",
    description="Fabiola Diaz y Valerie Espinoza",
    version='0.0.1'
)

users = []


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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
