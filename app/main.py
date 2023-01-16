from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from app.models import User, Gender, Role, UserDTO

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Frodo",
        last_name="Baggins",
        gender=Gender.male,
        roles=[Role.student]),
    User(
        id=uuid4(),
        first_name="Bilbo",
        last_name="Baggins",
        gender=Gender.male,
        roles=[Role.student])
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.put("/api/v1/users")
async def update_user(userDTO: UserDTO):
    for user in db:
        if user.id == userDTO.id:
            if userDTO.first_name:
                user.first_name = userDTO.first_name
            if userDTO.last_name:
                user.last_name = userDTO.last_name
            return {"id": user}
    raise HTTPException(
        status_code=404,
        detail="User with id {user_id} not found"
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user}
    raise HTTPException(
        status_code=404,
        detail="User with id {user_id} not found"
    )
