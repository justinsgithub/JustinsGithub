import pymongo


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from secrets import uri

client = pymongo.MongoClient(uri)

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/collections")
async def get_collections():
    collections = client["users"].list_collection_names()
    return {"collections": collections}