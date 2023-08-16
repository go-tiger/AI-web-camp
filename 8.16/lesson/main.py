from fastapi import FastAPI
from pydantic import BaseModel
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

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/{item_id}")
async def create_item(item: Item):
    mylogger.debug(item)
    return None