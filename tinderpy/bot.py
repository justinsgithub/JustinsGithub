from selenium import webdriver
from time import sleep
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("/home/jewell/bin/chromedriver")


password = 'Iloveme93'
username = 'lemonjewell@yahoo.com'


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://tinder.com')

sleep(2)

loginButton = driver.find_element_by_xpath('//*[@id="q-1565082725"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
loginButton.click()
sleep(2)

iAccept = driver.find_element_by_xpath('//div[@class="Pos(r) Maw(900px) Mx(a)"]/div/div/button[1]')
iAccept.click()
sleep(2)

#fb_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
fb_btn = driver.find_element_by_xpath('//*[@id="q-1343742289"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_btn.click()
sleep(1)

        # switch to login popup
base_window = driver.window_handles[0]
driver.switch_to_window(driver.window_handles[1])

email_in = driver.find_element_by_xpath('//*[@id="email"]')
email_in.send_keys(username)

pw_in = driver.find_element_by_xpath('//*[@id="pass"]')
pw_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//input[@name="login"]')
login_btn.click()

driver.switch_to_window(base_window)
sleep(3)

allowLocation = driver.find_element_by_xpath('//button[@aria-label="Allow"]')
allowLocation.click()
sleep(1)

notInterested = driver.find_element_by_xpath('//button[@aria-label="Not interested"]')
notInterested.click()
sleep(1)

#popup_1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
#popup_1.click()

#popup_2 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
#popup_2.click()

#popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
#popup_3.click()

like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')

dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')

while True:
    sleep(0.5)
    try:
        like_btn.click()
    except Exception:
        try:
            popup_2.click()
        except Exception:
            match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()
