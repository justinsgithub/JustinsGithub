from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
userid = "13802340"

goBack = 'browser.back()'

browser = webdriver.Chrome('/home/jewell/bin/chromedriver')  # Optional argument, if not specified will search path.
browser.get(url)
email_in = browser.find_element(By.XPATH, usernameForm)
email_in.send_keys(username)
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()
sleep(2)



####### START CUSTOM COMMANDS ########

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href^="/users/13802340"]'))).click()
print('clicked on profile link')
sleep(2)

#WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//p[@class="more"]/a[@href$="/friends"]'))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="container"]/div/p/a'))).click()
print('clicked on view all friends link')
sleep(2)


allLinks = browser.find_elements(By.TAG_NAME,  'a')


allLinksText = [link.text for link in allLinks]


for linkText in (allLinksText):
    if linkText != '':
        print(linkText)
