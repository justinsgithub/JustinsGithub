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
from fetlifeglobals import loginButton, placesLink, kinstersLink
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
STATE_CITY_USERS = fetlifeDatabase["STATE_CITY_USERS"] # CAMELCASE

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

userCount = 0
STATE_CITY_USERS = fetlifeDatabase["STATE_CITY_USERS"] # CAMELCASE

places = browser.find_element(By.XPATH, placesLink)
places.click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'STATE'))).click() # CAPITALIZED
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="STATE/related"]'))).click() # LOWERCASE
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CITY'))).click() # CAPITALIZED
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/kinksters"]'))).click()
for x in range(2, 200): # VARIES
    selectorStart = 'a[href$="/kinksters?page={}"]'
    selector = selectorStart.format(x) 
    print(selector)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
    print('clicked on next page link')
    userLinks = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/users/"][class~="mr1"]')
    print('found all user links')
    userNames = [userLink.text for userLink in userLinks]
    print('found all usernames')
    for userName in userNames:
        user = {
            "userName": userName,
            "userCount": userCount + 1,
            "followedByLemon": False,
            "numberOfLemonLovedPictures": 0
        }
        STATE_CITY_USERS.insert_one(user)
        userCount = userCount + 1
