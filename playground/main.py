#!/bin/python3
# -*- encoding: utf-8 -*-
from fastapi import FastAPI
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

app = FastAPI()

selenium_started = False

root_gets = 0

def track_visits(tracker):
    tracker = tracker + 1
    return tracker

@app.get("/")
async def root():
    message = track_visits(root_gets)
    return {"total requests": message}

@app.get("/selenium/start")
async def seleniumstart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://google.com')
    varia = driver.title
    driver.quit()
    sleep(3)
    return {"message": "Welcome To Selenium", "message2": varia}


@app.get("/selenium/techwithtim")
async def seleniumapi():
    driver = webdriver.Chrome()
    url = 'https://techwithtim.net/'
    driver.maximize_window();
    driver.get(url)
    print(driver.title)
    driver.quit()

    return {"message": driver.title}