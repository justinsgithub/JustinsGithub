from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# need the below imports to work with Explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
fetlife = myclient["fetlife"]
databaseList = myclient.list_database_names()

#states = [
#  { "name": "followers", "amount": 341},
#  { "category": "friends", "amount": 658},
#  { "category": "following", "amount": 3414},
#]


#x = fetLifeStats.insert_many(states)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

#for stat in fetLifeStats.find():
# print(stat)

#for stat  in fetLifeStats.find({},{ "category": 0 }):
#    print(stat)



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
sleep(1)



places = browser.find_element(By.XPATH, placesLink)
places.click()
sleep(1)


fetlifeStates = fetlife["states"]

userLinks = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/p/united-states/"]')
print('found all place links')
states = [userLink.text for userLink in userLinks]
print('found all states')
print(len(states))
for state in states:
    newState = {"name": state}
    fetlifeStates.insert_one(newState)
