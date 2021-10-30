################################################################################
######################## IMPORTS BEGIN #########################################
################################################################################
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pymongo import MongoClient

from fetlifeglobals import password, username, url, usernameForm, passwordForm
from fetlifeglobals import loginButton, placesLink, seattleLink, kinstersLink
from fetlifeglobals import nextPage, userLink
################################################################################
######################## IMPORTS END ###########################################
################################################################################

################################################################################
######################## GLOBALS BEGIN #########################################
################################################################################
browser = webdriver.Chrome('/home/jewell/bin/chromedriver')

myClient = MongoClient("mongodb://localhost:27017/")
fetlifeDatabase = myClient["fetlife"]
utahUsers = fetlifeDatabase["utahUsers"]

usersList = []
################################################################################
######################## GLOBALS END ###########################################
################################################################################

def login():
    browser.get(url)
    email_in = browser.find_element(By.XPATH, usernameForm)
    email_in.send_keys(username)
    pw_in = browser.find_element(By.XPATH, passwordForm)
    pw_in.send_keys(password)
    login_btn = browser.find_element(By.XPATH, loginButton)
    login_btn.click()
    sleep(1)


login()

for user in utahUsers.find():
    userName = user["userName"]
    lovedPictures = user["numberOfLemonLovedPictures"]
    if lovedPictures == 0:
        usersList.append(userName)

usersList[2:105] = []


passCount = 0 
totalLikedPictures = 0
for userName in usersList:
    userToUpdate = {"userName": userName}
    lovedPictures = 0
    try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(userName)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        
        lovedPictures = 1
        newValues = { "$set": { "numberOfLemonLovedPictures": lovedPictures } }
        utahUsers.update_one(userToUpdate, newValues)
        totalLikedPictures = totalLikedPictures + 1 
        
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(userName)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[2]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        
        lovedPictures = 2
        newValues = { "$set": { "numberOfLemonLovedPictures": lovedPictures } }
        utahUsers.update_one(userToUpdate, newValues)
        totalLikedPictures = totalLikedPictures + 1 

        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(userName)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[3]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
        
        lovedPictures = 3
        newValues = { "$set": { "numberOfLemonLovedPictures": lovedPictures } }
        utahUsers.update_one(userToUpdate, newValues)
        totalLikedPictures = totalLikedPictures + 1 
        print('total liked pictures = ' + format(totalLikedPictures))
    except Exception:
        newValues = { "$set": { "numberOfLemonLovedPictures": lovedPictures } }
        utahUsers.update_one(userToUpdate, newValues)
        passCount = passCount + 1
        print('total liked pictures = ' + format(totalLikedPictures))
        print('total passes = ' + format(passCount))
        pass
