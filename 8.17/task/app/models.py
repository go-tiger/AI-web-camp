from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime
import bcrypt

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, comment='유저 고유 id')
    loginId = Column(String(10), unique=True, index=True, nullable=False, comment='유저 로그인아이디')
    nickname = Column(String(10), unique=True, nullable=False, comment='유저 닉네임')
    password = Column(String(100), nullable=False, comment='유저 비밀번호(암호화)')
    email = Column(String(50), unique=True, nullable=False, comment='유저 이메일')
    emailVerified = Column(Boolean, default=False, comment='이메일 인증 여부')
    introduction = Column(String(255), default='', comment='유저 자기소개')
    image = Column(String(255), default='/./images/baseprofile.png', comment='유저 프로필 사진')
    loginMethod = Column(String(6), default='local', comment='로그인 구분')
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, comment='계정 생성 시간')
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False, comment='계정 정보 수정 시간')

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
