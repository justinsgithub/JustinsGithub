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

goBack = 'browser.back()'

chrome_options = Options()
chrome_options.add_argument("/home/jewell/bin/chromedriver")


browser = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.
browser.get(url)
email_in = browser.find_element(By.XPATH, usernameForm)
email_in.send_keys(username)
pw_in = browser.find_element(By.XPATH, passwordForm)
pw_in.send_keys(password)
login_btn = browser.find_element(By.XPATH, loginButton)
login_btn.click()
sleep(2)

#WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/pictures"]'))).click()
#sleep(2)

#WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/statuses"]'))).click()


WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/home/statuses"]'))).click()
sleep(2)


browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)


buttonList = browser.find_elements(By.CSS_SELECTOR,  'a[title="Love"]')


totalLikedStatusesFile = open('Database/Fetlife/Users/likedstatusescount', "a")
print(len(buttonList))
for x in range(len(buttonList)):
    try:
        buttonList[x].click()
        totalLikedStatusesFile.write("1\n")
        sleep(1)
    except Exception:
        pass

totalLikedStatusesFile.close()
browser.quit()
