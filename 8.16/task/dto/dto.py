from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from typing import Union

class User(BaseModel):
    loginId: str
    nickname: str
    password: str
    email: str
    emailVerified: bool = False
    introduction: str = ""
    image: str = "/./images/baseprofile.png"
    loginMethod: str = "local"
    createdAt: Union[datetime, None] = datetime.today()
    updatedAt: Union[datetime, None] = datetime.today()

class UserUpdate(BaseModel):
    nickname: Union[str, None] = None
    password: Union[str, None] = None
    email: Union[str, None] = None
    introduction: Union[str, None] = None
    image: Union[str, None] = None
    updatedAt: Union[datetime, None] = datetime.today()

class Short(BaseModel):
    userId: Union[int, None] = None
    originalUrl: str
    shortUrl: Union[str, None] = "생성될 단축 url"
    createdAt: Union[datetime, None] = datetime.today()

class LoginUser(BaseModel):
    loginId: str
    password: str

class checkId(BaseModel):
    id: str

class checkEmail(BaseModel):
    email: str

class checkNickname(BaseModel):
    nickname: str