import re

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

password = 'Ilovelemon93'
username = 'lemonjewell@yahoo.com'
url = 'https://fetlife.com/users/sign_in'
usernameForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
passwordForm = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
loginButton = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
placesLink = '/html/body/nav[1]/div[1]/ul/li[5]/a'
userid = "13802340"

goBack = 'browser.back()'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("/home/jewell/bin/chromedriver")

browser = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.
browser.get(url)
email_in = browser.find_element(By.XPATH, usernameForm)
email_in.send_keys(username)
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()



####### START CUSTOM COMMANDS ########

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href^="/users/13802340"]'))).click()
sleep(2)



allLinks = browser.find_elements(By.TAG_NAME,  'h4')


allLinksText = [link.text for link in allLinks]


audienceFile = open("Database/Fetlife/Audience/audience", "w")
followingFile = open("Database/Fetlife/Audience/following", "w")
followerFile = open("Database/Fetlife/Audience/followers", "w")
friendFile = open("Database/Fetlife/Audience/friends", "w")

for linkText in (allLinksText):

    following = re.search("^Following", linkText)
    followers = re.search("^Followers", linkText)
    friends = re.search("^Friends", linkText)



    if following:
        splitString = re.split("\s", linkText)
        numberF = splitString[1]
        print(linkText)
        audienceFile.write(linkText + "\n")
        followingFile.write(numberF + "\n")

    if followers:
        splitString = re.split("\s", linkText)
        numberF = splitString[1]
        print(linkText)
        audienceFile.write(linkText + "\n")
        followerFile.write(numberF + "\n")

    if friends:
        splitString = re.split("\s", linkText)
        numberF = splitString[1]
        print(linkText)
        audienceFile.write(linkText + "\n")
        friendFile.write(numberF + "\n")

audienceFile.close()
followingFile.close()
followerFile.close()
friendFile.close()
