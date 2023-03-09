import os
import requests
from pydantic import BaseModel
from enum import Enum
from fastapi import FastAPI, HTTPException

app = FastAPI()


class Category(Enum):
    WATCHES = 'watches'
    AVIONICS = 'avionics'


class Items(BaseModel):
    name: str
    price: float
    count: int
    type: Category


items = {
    0: Items(name='fenix5', price=999.90,   count=45, type=Category.WATCHES),
    1: Items(name='fenix 6', price=199.90,   count=45, type=Category.WATCHES),
    2: Items(name='G450',    price=12999.90, count=5,  type=Category.AVIONICS)
}


@app.get('/')
def index() -> dict[str, dict[int, Items]]:
    return {'items': items}


@app.get('/item_name/{name}')
def get_item_name(item_name) -> Items:
    if item_name not in items:
        raise HTTPException(status_code=400, detail='item does not exist')
    return items[item_name]


if __name__ == '__main__':
    # os.system(r'cd C:\Users\medvi\OneDrive\Desktop\Cellenium\app\fast_api')
    # os.system(r'uvicorn main:app --reload')
    print(requests.get('http://127.0.0.1:8000/item_name/0').json())
