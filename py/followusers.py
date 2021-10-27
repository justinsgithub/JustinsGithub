from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# need the below imports to work with Explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException



password = 'Ilovelemon93'
username = 'lemonjewell@yahoo.com'
url = 'https://fetlife.com/users/sign_in'
usernameForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
passwordForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
loginButton = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
placesLink = '/html/body/nav[1]/div[1]/ul/li[5]/a'
seattleLink = '/html/body/div[3]/div/header/div/div[2]/div/a[1]'
kinstersLink = '/html/body/div[3]/div/header/div/div[2]/a[2]/div/div'
nextPage = '/html/body/div[3]/div/div[2]/div/main/footer/div[1]/a[3]'
userLink = '/html/body/div[3]/div/div[2]/div/main/div/div[18]/div/div/div/div[1]/div[2]/div[1]/a'
goBack = 'browser.back()'
washingtonLink = 'a[@href=""]'
browser = webdriver.Chrome('/home/jewell/bin/chromedriver')  # Optional argument, if not specified will search path.
browser.get(url)
email_in = browser.find_element(By.XPATH, usernameForm)
email_in.send_keys(username)
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()

#for pageNumber in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
#for pageNumber in [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]:

db = 'Database/Fetlife/Users/Washington/Spokane/Tofollow/'
for pageNumber in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
    pageFile = format(pageNumber)
    fileToOpen = db + pageFile
    with open(fileToOpen) as file:
        for user in file:
            try:
                user = user.strip() #preprocess line
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
                print('entering in search bar')
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
                print('clicked search button')
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
                print('clicked user profile')
                WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,'Follow'))).click()
                print('clicked follow button')
                followedUsersFile = open("Database/Fetlife/Users/Washington/Spokane/followed", "a")
                followedUsersFile.write(user + "\n")
            except Exception:
                pass
