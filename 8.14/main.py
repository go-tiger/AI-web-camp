from fastapi import FastAPI
from dto.dto import User, Short
from datetime import date, datetime, time, timedelta

_sample = [
    {"id": 1, "loginId": "123", "nickname": "123", "password": "123", "email": "123@123.45", "image":"123.png", "createdAt": date.today(), "updatedAt": date.today()},
    {"id": 2, "loginId": "2", "nickname": "2", "password": "2", "email": "2@123.45", "createdAt": date.today(), "updatedAt": date.today()}
    ]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = None
    for _user_data in _sample:
        if _user_data["id"] == user_id:
            user = User(**_user_data)
    return user