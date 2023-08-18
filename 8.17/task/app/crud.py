from sqlalchemy.orm import Session
from . import models, schemas
import bcrypt
from datetime import datetime

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        loginId=user.loginId,
        nickname=user.nickname,
        password=hashed_password,
        email=user.email,
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_find_loginId(db: Session, loginId: str):
    return db.query(models.User).filter(models.User.loginId == loginId).first()

def get_user_find_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_find_nickname(db: Session, nickname: str):
    return db.query(models.User).filter(models.User.nickname == nickname).first()
