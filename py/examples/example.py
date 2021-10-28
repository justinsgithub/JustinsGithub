from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pymongo import MongoClient

mongoURL = "MONGOURL"
db = MongoClient(mongoURL)
database = db["exampleDatabase"]
exampleSiteUsers = database["exampleSiteUsers"]

url = 'https://example.com/users/sign_in'
bot = webdriver.Chrome('/home/exampleuser/bin/chromedriver')
bot.get(url)
bot.maximize_window();



password = 'examplepassword'
username = 'example@example.com'

usernameForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
passwordForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
loginButton = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
placesLink = '/html/body/nav[1]/div[1]/ul/li[5]/a'
usersLink = '/html/body/div[3]/div/header/div/div[2]/a[2]/div/div'
nextPage = '/html/body/div[3]/div/div[2]/div/main/footer/div[1]/a[3]'
body = bot.find_element(By.XPATH, '/html/body')
email_in = bot.find_element(By.XPATH, usernameForm)
pw_in = bot.find_element(By.XPATH, passwordForm)
login_btn = bot.find_element(By.XPATH, loginButton)

email_in.send_keys(username)
pw_in.send_keys(password)
login_btn.click()


userList = []
roundsCompleted = 0
passes = 0
for user in exampleSiteUsers.find({},{"_id":0, "userName":1, "lovedPictures":1 }):
    lovedPictures = user["lovedPictures"]
    userName = user["userName"]
    if lovedPictures == False:
            userList.append(userName)

for user in userList:
    try:
        userQuery = {"userName": user}
        didLikePictures = False
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="EXAMPLECLASS"]'))).click()
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="EXAMPLECLASS"]/a'))).click()
        body.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Like"]'))).click()
        lovedPictures = 1
        didLikePictures = True
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="EXAMPLECLASS"]'))).click()
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="EXAMPLECLASS"]/a[2]'))).click()
        body.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Like"]'))).click()
        lovedPictures = 2
        didLikePictures = True
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
        WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="EXAMPLECLASS"]'))).click()
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="EXAMPLECLASS"]/a[3]'))).click()
        body.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Like"]'))).click()
        lovedPictures = 3
        didLikePictures = True
        newUserData = { "$set": { "didLikePictures": didLikePictures, "lovedPictures": lovedPictures } }
        exampleSiteUsers.update_one(userQuery, newUserData)
        roundsCompleted = roundsCompleted + 1
        print('liked ' + format(lovedPictures) + ' of' + user + ' pictures')
        print(format(roundsCompleted) + ' rounds completed')
    except Exception:
        newUserData = { "$set": { "didLikePictures": didLikePictures, "lovedPictures": lovedPictures } }
        exampleSiteUsers.update_one(userQuery, newUserData)
        passes = passes + 1 
        print('liked ' + format(lovedPictures) + ' of' + user + ' pictures')
        print(format(passes) + ' passes so far')
        pass
