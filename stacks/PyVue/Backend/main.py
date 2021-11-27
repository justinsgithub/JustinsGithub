#!/bin/python3
from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
database = 'database'

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/randomuser")
async def randomuser():
    num_of_requests = len(os.listdir(database + '/randomuser'))
    new_request_id = num_of_requests + 1
    os.mkdir(database + '/randomuser/' + str(new_request_id))
    response = requests.get('https://randomuser.me/api')
    response.raise_for_status()
    data = response.json()
    print("RESULTS")
    print(data["results"])
    print("")
    print("GENDER")
    print(data["results"][0]["gender"])
    print("")
    print("NAME")
    print(data["results"][0]["name"]["first"])
    print(data["results"][0]["name"]["last"])
    print("")
    return data

@app.get("/randomusernum")
async def randomusernum():
    num_of_requests = len(os.listdir(database + '/randomuser'))
    jsonnum = str(num_of_requests)
    return {"numOfRequests": jsonnum}

