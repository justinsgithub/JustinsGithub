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
from selenium.webdriver.chrome.options import Options


from fetlifeglobals import password, myusername, url, usernameForm, passwordForm
from fetlifeglobals import loginButton, placesLink, seattleLink, kinstersLink
from fetlifeglobals import nextPage, userLink


import os
################################################################################
######################## IMPORTS END ###########################################
################################################################################

################################################################################
######################## GLOBALS BEGIN #########################################
################################################################################
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('/home/jewell/bin/chromedriver')
browser = webdriver.Chrome(options=chrome_options)
usersList = []
passedUsers = []

picSelector1 = '//div[@class="span-13 append-1 breakword"]/a'
picSelector2 = '//div[@class="span-13 append-1 breakword"]/a[2]'
picSelector3 = '//div[@class="span-13 append-1 breakword"]/a[3]'
picSelector4 = '//div[@class="span-13 append-1 breakword"]/a[4]'
picSelector5 = '//div[@class="span-13 append-1 breakword"]/a[5]'

currentPath = os.getcwd()
state = os.path.basename(currentPath)

################################################################################
######################## GLOBALS END ###########################################
################################################################################

def login():
    browser.get(url)
    email_in = browser.find_element(By.XPATH, usernameForm)
    email_in.send_keys(myusername)
    pw_in = browser.find_element(By.XPATH, passwordForm)
    pw_in.send_keys(password)
    login_btn = browser.find_element(By.XPATH, loginButton)
    login_btn.click()
    sleep(1)

def getPlaces():
    places = browser.find_element(By.XPATH, placesLink)
    places.click()


def getKinsters():
    lowerCaseState = state.lower()
    capitalizedState = lowerCaseState.capitalize()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, capitalizedState))).click() # CAPITALIZED
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/kinksters"]'))).click()

def getPages(startRange, endRange):
    for x in range(startRange, endRange): # VARIES
        try:
            selectorStart = 'a[href$="/kinksters?page={}"]'
            selector = selectorStart.format(x) 
            print(selector)
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
            print('clicked on next page link')
            userLinks = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/users/"][class~="mr1"]')
            print('found all user links')
            userNames = [userLink.text for userLink in userLinks]
            print('found all usernames')
            for userName in userNames:
                usersList.append(userName)
        except Exception:
            pass

def trackPasses():
    fileToOpen = state + 'PassedUsers.txt'
    for user in passedUsers:
        passedUsersFile = open(fileToOpen, "a")
    passedUsersFile.close()


def loveUserPic(picSelector, user):
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, picSelector))).click()
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()


def loveUserPics():
    passCount = 0 
    totalLikedPictures = 0
    for userName in usersList:
        try:
            loveUserPic(picSelector1, userName)
            totalLikedPictures = totalLikedPictures + 1 
            loveUserPic(picSelector2, userName)
            totalLikedPictures = totalLikedPictures + 1 
            loveUserPic(picSelector3, userName)
            totalLikedPictures = totalLikedPictures + 1 
            loveUserPic(picSelector4, userName)
            totalLikedPictures = totalLikedPictures + 1 
            loveUserPic(picSelector5, userName)
            totalLikedPictures = totalLikedPictures + 1 
            print('total liked pictures = ' + format(totalLikedPictures))
        except Exception:
            passedUsers.append(userName)
            passCount = passCount + 1
            print('total liked pictures = ' + format(totalLikedPictures))
            print('total passes = ' + format(passCount))
            pass

def runProgram():
    login()
    getPlaces()
    getKinsters()
    getPages(2,50)
    loveUserPics()
    trackPasses()


runProgram()
