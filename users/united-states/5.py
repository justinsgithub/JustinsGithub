#!/bin/env/python3
import re
import os
from time import sleep
from selenium import webdriver
#from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
USERNAME_FORM = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input'
PASSWORD_FORM = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input'
LOGIN_BUTTON = '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
PLACES_LINK = '/html/body/nav[1]/div[1]/div[1]/ul/li[5]/a'
USERNAME='lovelittlelemon'
PASSWORD="Ilovelemon93"
URL = 'https://www.fetlife.com/users/sign_in'
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('/home/justin/bin/chromedriver')
bot = webdriver.Chrome(options=chrome_options)
def login():
    ''' login into social media site '''
    bot.get(URL)
    print('got url')
    email_in = bot.find_element(By.XPATH, USERNAME_FORM)
    email_in.send_keys(USERNAME)
    print('entered email')
    pw_in = bot.find_element(By.XPATH, PASSWORD_FORM)
    pw_in.send_keys(PASSWORD)
    print('entered password')
    login_btn = bot.find_element(By.XPATH, LOGIN_BUTTON)
    login_btn.click()
    print('clicked login')


def get_page(page_url):
    bot.get(page_url)

def get_page_content(selector):
    links = bot.find_elements(
            By.XPATH, selector)
    print('found data')
    link_text = [link.text for link in links]
    return link_text

def get_href(selector):
    links = bot.find_elements(
            By.XPATH, selector)
    print('found data')
    link_text = [link.get_attribute("href") for link in links]
    return link_text

def save_data(file_name, new_data):
    with open(file_name, "a") as file:
        file.write(f'{new_data}\n')

def save_data_list(datalist, ln):
    for item in datalist:
        save_data(ln, item)


login()
sleep(0.5)

with open('us_places_all.txt') as file:
    for place in file.readlines():
        place = place.strip()
        page = 'https://fetlife.com/p/united-states/' + place + '/kinksters'
        get_page(page)
        kinkster_list = get_href('//main//div//a[@class="link f5 fw7 secondary mr1"]')

        for a in kinkster_list:
            try:
                get_page(a)
                sleep(0.3)
                button = '//div[@class="button"]//a[@rel="nofollow"]'  
                follow_button = bot.find_element(By.XPATH, button)
                follow_button.click()
            except Exception:
                pass
