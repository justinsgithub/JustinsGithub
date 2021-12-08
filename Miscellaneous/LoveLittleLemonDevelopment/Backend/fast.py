#!/bin/python3
from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime

app = FastAPI()
database = "Database"
page_request_db = database + "/SiteStatistics/PageRequests"

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8125",
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
    this_date = str(datetime(2021, 12, 8, 14, 0, 27, 430276))
    return {"today's date": this_date}

@app.get("/logrequest")
async def root():
    number_of_requests = len(os.listdir(page_request_db))
    new_request_id = str(number_of_requests + 1)
    os.mkdir(page_request_db + "/" + new_request_id)    
    return {"logged request": new_request_id}
