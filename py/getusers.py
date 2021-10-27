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
print('entered email')
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
print('entered pword')
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()
print('clicked login')



places = browser.find_element(By.XPATH, placesLink)
places.click()
print('clicked places')

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'California'))).click()
print('clicked on California')

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="california/related"]'))).click()
print('clicked on cities within')

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Los Angeles'))).click()
print('clicked on Los Angeles')

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/kinksters"]'))).click()
print('clicked on kinsters')

db = "Database/Fetlife/Users/California/LA/Tofollow/"
for x in range(2, 200):
    selectorStart = 'a[href$="/kinksters?page={}"]'
    selector = selectorStart.format(x) 
    print(selector)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
    print('clicked on next page link')
    userLinks = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/users/"][class~="mr1"]')
    print('found all user links')
    userNames = [userLink.text for userLink in userLinks]
    print('found all usernames')
    userNamesFile = open(db + format(x), "a")
    totalUsersFile = open(db + "allusers", "a")
    print('opened file to write users')
    for userName in userNames:
        userNamesFile.write(userName + "\n")
        totalUsersFile.write(userName + "\n")
    userNamesFile.close()
    totalUsersFile.close()
    print('closed file')
