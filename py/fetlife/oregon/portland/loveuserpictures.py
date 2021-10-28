from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pymongo import MongoClient

mongoURL = "mongodb://localhost:27017/"
db = MongoClient(mongoURL)
database = db["fetlife"]
portlandUsers = database["portlandUsers"]

url = 'https://fetlife.com/users/sign_in'
bot = webdriver.Chrome('/home/jewell/bin/chromedriver')
bot.get(url)
bot.maximize_window();



password = 'Ilovelemon93'
username = 'lemonjewell@yahoo.com'

usernameForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
passwordForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
loginButton = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
placesLink = '/html/body/nav[1]/div[1]/ul/li[5]/a'
kinstersLink = '/html/body/div[3]/div/header/div/div[2]/a[2]/div/div'
nextPage = '/html/body/div[3]/div/div[2]/div/main/footer/div[1]/a[3]'
body = bot.find_element(By.XPATH, '/html/body')
email_in = bot.find_element(By.XPATH, usernameForm)
pw_in = bot.find_element(By.XPATH, passwordForm)
login_btn = bot.find_element(By.XPATH, loginButton)

#bot.back()
email_in.send_keys(username)
pw_in.send_keys(password)
login_btn.click()



roundsCompleted = 0
passes = 0
for user in portlandUsers.find():
        lovedPictures = user["lovedPictures"]
        userName = user["userName"]
        if lovedPictures == False:
            try:
                userQuery = {"userName": userName}
                didLovePictures = False
                lovedPictures = 0 
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
                WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a'))).click()
                body.send_keys(Keys.PAGE_DOWN)
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
                lovedPictures = lovedPictures + 1
                didLovePictures = True
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
                WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[2]'))).click()
                body.send_keys(Keys.PAGE_DOWN)
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
                lovedPictures = lovedPictures + 1
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="q"]'))).send_keys(user)
                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
                WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href^="/users/"][class~="mr1"]'))).click()
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="span-13 append-1 breakword"]/a[3]'))).click()
                body.send_keys(Keys.PAGE_DOWN)
                WebDriverWait(bot, 1).until(EC.element_to_be_clickable((By.XPATH,'//a[@title="Love"]'))).click()
                lovedPictures = lovedPictures + 1
                newUserData = { "$set": { "didLovePictures": didLovePictures, "lovedPictures": lovedPictures } }
                portlandUsers.update_one(userQuery, newUserData)
                roundsCompleted = roundsCompleted + 1
                print(format(roundsCompleted) + ' rounds completed')
            except Exception:
                newUserData = { "$set": { "didLovePictures": didLovePictures, "lovedPictures": lovedPictures } }
                portlandUsers.update_one(userQuery, newUserData)
                if lovedPictures == 0:
                    print("could not find any pictures for user" + userName)
                if lovedPictures == 1:
                    print("could only find 1 picture for user" + userName)
                if lovedPictures == 2:
                    print("could only find 2 pictures for user" + userName)
                if lovedPictures == 3:
                    print("Random error, don't know the problem")
                passes = passes + 1 
                print(format(passes) + ' passes so far')
                pass
