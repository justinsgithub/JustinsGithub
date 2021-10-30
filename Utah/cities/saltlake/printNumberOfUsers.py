from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pymongo import MongoClient
myClient = MongoClient("mongodb://localhost:27017/")
fetlifeDatabase = myClient["fetlife"]
washingtonUsers = fetlifeDatabase["washingtonUsers"]

userList = []
for user in washingtonUsers.find():
    userName = user["userName"]
    userList.append(userName)

print(len(userList))
