from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

_sample = [
    {"id": 1, "loginId": "123", "nickname": "123", "password": "123", "email": "123@123.45", "image":"123.png", "createdAt": date.today(), "updatedAt": date.today()},
    {"id": 2, "loginId": "2", "nickname": "2", "password": "2", "email": "2@123.45", "createdAt": date.today(), "updatedAt": date.today()}
    ]

app = FastAPI()

class User(BaseModel):
    id: int
    loginId: str
    nickname: str
    password: str
    email: str
    emailVerified: bool = False
    introduction: str = ""
    image: str = "/./images/baseprofile.png"
    loginMethod: str = "local"
    createdAt: datetime
    updatedAt: datetime


class Short(BaseModel):
    id: int
    userId: int
    originalUrl: str
    shortUrl: str
    createdAt: datetime

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