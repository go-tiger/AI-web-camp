from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

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