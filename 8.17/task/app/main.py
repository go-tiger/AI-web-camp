from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from jose import JWTError, jwt
from datetime import datetime, timedelta
import bcrypt

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/join/", response_model=schemas.User)
def join(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_find_loginId = crud.get_user_find_loginId(db, loginId=user.loginId)
    if db_user_find_loginId:
        return JSONResponse(content={"errorMessage": "이미 가입된 아이디입니다."}, status_code=409)
    
    db_user_find_email = crud.get_user_find_email(db, email=user.email)
    if db_user_find_email:
        return JSONResponse(content={"errorMessage": "이미 가입된 이메일입니다."}, status_code=409)
    
    db_user_find_nickname = crud.get_user_find_nickname(db, nickname=user.nickname)
    if db_user_find_nickname:
        return JSONResponse(content={"errorMessage": "이미 가입된  닉네임입니다."}, status_code=409)
    
    crud.create_user(db, user)
    return JSONResponse(content={"message": "가입이 완료되었습니다."}, status_code=201)
