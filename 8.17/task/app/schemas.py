from typing import List
from pydantic import BaseModel

class User(BaseModel):
    loginId: str
    nickname: str
    password: str
    email: str
    emailVerified: bool
    introduction: str
    image: str
    loginMethod: str

class UserCreate(BaseModel):
    loginId: str
    nickname: str
    password: str
    email: str