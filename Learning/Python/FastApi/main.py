from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from typing import Optional
import os 
from pydantic import BaseModel
import uuid
import shutil
from datetime import datetime

db = "DataBase/Items"

def write_file(fname:str, fcontent):
    with open(fname, "w") as file:
        file.write(str(fcontent))

        
def append_file(fname:str, fcontent):
    with open(fname, "a") as file:
        file.write(str(fcontent))

def read_file(fname:str, datatype:str="string"):
    
    if not os.path.isfile(fname):
        return ""
    
    if datatype == "int":
        with open(fname, "r") as file:
            return int(file.read())

    if datatype == "float":
        with open(fname, "r") as file:
            return float(file.read())
    
    with open(fname, "r") as file:
        return file.read()
  
class User(BaseModel):
    username: str
    password: str


class Item(BaseModel):
    created_at: Optional[datetime] = datetime.date
    item_id: Optional[uuid.UUID] = None
    is_current: bool = True
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/login/")
async def create_user(user: User):
    os.mkdir(user.username)
    
    return user


@app.get("/items/")
async def get_items():
    item_ids = os.listdir(db)
    items = []
    for item_id in item_ids:        
        item = dict()
        item["item_id"] = item_id
        item["created_at"] = read_file(f"{db}/{item_id}/createdat")
        item["name"] = read_file(f"{db}/{item_id}/name")
        item["description"] = read_file(f"{db}/{item_id}/description")
        item["price"] = read_file(f"{db}/{item_id}/price")
        items.append(item)
        
    return items

@app.post("/items/")
async def create_item(item: Item):
    item.item_id = uuid.uuid4()
    current_date = datetime.now()
    formatted_date = f"{current_date.year}-{current_date.month}-{current_date.day}"
    item.created_at = formatted_date
    item_dir = f"{db}/{item.item_id}"
    os.mkdir(item_dir)
    write_file(f"{item_dir}/iscurrent", item.is_current)
    write_file(f"{item_dir}/name", item.name)
    write_file(f"{item_dir}/description", item.description)
    write_file(f"{item_dir}/price", item.price)
    write_file(f"{item_dir}/tax", item.tax)
    write_file(f"{item_dir}/createdat", item.created_at)

    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id):
    item_ids = os.listdir(db)
    if item_id in item_ids:
        shutil.rmtree(f"{db}/{item_id}", ignore_errors=True)
        return {"item_id": item_id}
    
    return {"message": "no item found"}

@app.put("/items/{item_id}")
async def update_item(item_id, item: Item):
    item_dir = f"{db}/{item_id}"
    
    if item.name:    
        write_file(f"{item_dir}/name", item.name)
    if item.description:
        write_file(f"{item_dir}/description", item.description)
    if item.price:
        write_file(f"{item_dir}/price", item.price)

    return item