from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from dto.dto import User, Short, LoginUser, checkId, checkEmail, checkNickname, UserUpdate
from datetime import date, datetime, time, timedelta
from typing import Union

import logging
import sys

mylogger = logging.getLogger("mylogger")

formatter = logging.Formatter('[%(levelname)s] %(message)s')

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

mylogger.addHandler(handler)
mylogger.setLevel(logging.DEBUG)

_sample_shorts = [
    {"id": 1, "userId": 1, "originalUrl": "https://naver.com", "shortUrl": "https://url.kr/sturl1", "createdAt": date.today()},
    {"id": 2, "userId": 1, "originalUrl": "https://google.com", "shortUrl": "https://url.kr/sturl2", "createdAt": date.today()}
    ]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 로그인
@app.post("/login")
async def login(loginUser: LoginUser):
    mylogger.debug(loginUser)
    return loginUser

# 로그아웃
@app.post("/logout")
async def logout():
    # Response.delete_cookie(key="access_token")
    return RedirectResponse("/", 200)

# 회원가입
@app.post("/join")
async def join(joinUser: User):
    mylogger.debug(joinUser)
    return joinUser

# 아이디 중복체크
@app.get("/users/check/id")
async def check_id(id: checkId):
    mylogger.debug(id)
    return id

# 이메일 중복체크
@app.get("/users/check/email")
async def check_email(email: checkEmail):
    mylogger.debug(email)
    return email

# 닉네임 중복체크
@app.get("/users/check/nickname")
async def check_nickname(nickname: checkNickname):
    mylogger.debug(nickname)
    return nickname

# 마이페이지(조회)
@app.get("/users/info/{id}")
async def mypage(id):
    mylogger.debug(id)
    return id

# 마이페이지(수정)
@app.patch("/users/info/{id}")
async def mypage_edit(userUpdate: UserUpdate):
    mylogger.debug(userUpdate)
    userUpdate = {key: value for key, value in userUpdate.model_dump().items() if value is not None}
    mylogger.debug(userUpdate)
    return userUpdate

# 이메일 인증
@app.post("/users/email/{id}")
async def email_verified(emailVerified: checkEmail):
    mylogger.debug(emailVerified)
    return emailVerified

# 이메일 인증코드 확인
@app.post("/users/email-code-check/{id}")
async def email_code_check(emailCode: checkEmail):
    mylogger.debug(emailCode)
    return emailCode

# 단축주소 페이지(조회)
@app.get("/shorts")
async def shorts():
    mylogger.debug(_sample_shorts)
    return _sample_shorts

# 단축주소 생성
@app.post("/shorts")
async def shorts_add(shorts: Short):
    mylogger.debug(shorts)
    return shorts

# 단축주소 유저 조회
@app.get("/shorts/users/{id}")
async def shorts_users(id: int):
    shorts = []
    for _user_sample_shorts in _sample_shorts:
        if _user_sample_shorts["userId"] == id:
            shorts.append(Short(**_user_sample_shorts))
    mylogger.debug(shorts)
    return shorts

# 단축주소 단일 조회
@app.get("/shorts/list/{id}")
async def shorts_list(id: int):
    shorts = []
    for _user_sample_shorts in _sample_shorts:
        if _user_sample_shorts["id"] == id:
            shorts.append(Short(**_user_sample_shorts))
    mylogger.debug(shorts)
    return shorts