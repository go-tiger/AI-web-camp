from datetime import datetime, timedelta
from typing import Union

from fastapi import Body, Depends, FastAPI, HTTPException, Header, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated

from jose import JWTError, jwt
from passlib.context import CryptContext

import logging
import sys

mylogger = logging.getLogger("mylogger")

formatter = logging.Formatter('[%(levelname)s] %(message)s')

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

mylogger.addHandler(handler)
mylogger.setLevel(logging.DEBUG)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str


class Board(BaseModel):
    id: Union[int, None] = None
    title: str
    desc: str
    created_at: Union[datetime, None] = None
    user_id: Union[str, None] = None

class User(BaseModel):
    id: int
    user_id: str
    hashed_password: str
    user_name: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

app = FastAPI()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


user_list = [
    {"userId": "james", "hashed_password": get_password_hash("jjjj")},
    {"userId": "alice", "hashed_password": get_password_hash("aaaa")},
]

session_list = [

]

# def decode_hashed_password(hashed_password: str):
#     _len = len(hashed_password)
#     _prefix = hashed_password[0]
#     decode_password = "{}{}".format(_prefix, _len) * 2
#     return decode_password

# def create_client_ticket(user_id: str):
#     user_ticket = user_id + datetime.now().strftime("%Y-%m-%d")
#     return user_ticket

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: str = payload.get("sub")
    return user_id

@app.post("/boards")
async def insert_board(board: Board, authorization: str = Header(None)):
    mylogger.info(board)
    mylogger.info(authorization)
    return {"res": True}

@app.get("/users")
async def get_user_token(token: Token):
    print(token)
    paylode = jwt.decode(token.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: str = paylode.get("sub")
    return {"user_id": user_id}

@app.post("/login")
async def login(user_id: Annotated[str, Body()], password: Annotated[str, Body()]):
    access_token = None
    for user_info in user_list:
        if user_id == user_info["userId"]:
            _db_password = user_info["hashed_password"]
            is_verify = verify_password(password, _db_password)
            if is_verify:
                session_list.append({"num": len(session_list), "loginId": user_id, "loginAt": datetime.now()})
                token_obj = {"sub": user_id}
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(token_obj, access_token_expires)
    if access_token is not None:
        return {"access_token": access_token}
    else:
        return {"message": "login failed"}
    ## 로그인 할 때
    ## param: id, pw
    ## step 1: userid가 있는지 없는지 확인
    ## step 2: 만약 userid가 있다면 비밀번호가 맞는지 확인
    ## step 3: 비밀번호는 서버도 실제로 어떤 값을 저장해두었는지 알수가 없도록 저장
        ## 사용자는 서버에게 비밀번호를 보낼때 서버가 알아보지 못하는 값으로 바뀌어서 들어온다
        ## 서버는 실제 저장된 비밀번호, 근데 그 비밀번호는 우리도 모른다. 유저도 보낸 비밀번호
        ## 어떤한 공개된 약속을 통해서 사용자가 보낸 비밀번호와 서버가 저장되어 있는 비밀번호를
        ## 서로 해동해서 일치하는지 확인 해야함
    ## step 4: 만약 해독된 비밀번호가 유저가 보낸 비밀번호와 일치하면 로그인
    ## step 5: 서버는 해당 유저아이디를 세션이라는 공간에 저장해둔다.
    ## step 6: 서버는 클라이언트에 임시 티켓을 발급해주어 그 이후에도 쓸 수 있게 되돌려준다