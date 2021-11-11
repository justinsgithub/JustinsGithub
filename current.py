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
def dir_x(a): # directory name
    os.mkdir(a)
def dirs_x(a): # list
    for b in a:
        dir_x(b)
def w_x(a,b): # file, string
    with open(a, "a") as file:
        file.write(f'{b}\n')
def ws_x(a, b): # list, filename 
    for item in a:
        w_x(b, item)

def get_x(a): # url
    bot.get(a)
def get_xx(a): # url
    b = f"https://fetlife.com/{a}"
    bot.get(b)
def get_xa(a, b): # selector, attribute
    c = bot.find_element(By.XPATH, a)
    d = c.get_attribute(b)
    return c
def gets_xa(a,b): # selector, attribute
    c = bot.find_elements(By.XPATH, a)
    e = [d.get_attribute(b) for d in c]
    return e
def get_xt(a): # selector
    b = bot.find_element(By.XPATH, a)
    c = b.text
    return c
def gets_xt(a): # selector
    b = bot.find_elements(By.XPATH, a)
    c = [d.text for d in b]
    return c

def r_x(a): # file
    b = []
    with open(a) as c:
        for a in c.readlines():
            d = a.strip()
            b.append(d)
    return b
def sub_x(a,b,c): # string, pattern to remove, pattern to replace
    d = re.sub(b,c,a)
    return(d)
def subs_x(a,b,c): # list, pattern to remove, pattern to replace
    d = []
    for e in a:
        f = sub_x(e,b,c)
        d.append(f)
    return d
def strip_x(a): # string
    b = a.strip()
    return(b)
def strips_x(a): # list
    b = []
    for c in a:
        d = c.strip()
        b.append(d)
    return b
def lower_x(a): # string
    b = a.lower()
    return(b)
def lowers_x(a): # list
    b = []
    for c in a:
        d = c.lower()
        b.append(d)
    return b


def scrape_x(a2,a3): # file, selector
    dir = os.getcwd()
    a1 = r_x(a2)
    for a in a1: 
        os.chdir(dir)
        os.chdir(a)
        b = f'p/united-states/{a}/kinksters'
        get_xx(b)
        c = gets_xt(a3)
        d = lowers_x(c)
        e = strips_x(d)
        f = subs_x(e,' ','-')
        dirs_x(f)



def ws_X(a,b):
    num = len(os.listdir())
    c = bot.find_elements(By.XPATH, a)
    e = [d.get_attribute(b) for d in c]
    f = [d.text for d in c]
    adir = os.getcwd()
    for x in range(len(c)):
        os.chdir(adir)
        new_dir = str(num)
        os.mkdir(new_dir)
        os.chdir(new_dir)
        username = f[x] 
        url = e[x]
        w_x('username', username)
        w_x('url', url)
        num += 1
    os.chdir(adir)

def scrapes_x(a2,a3,a4): # dir, selector, attribute
    dir = os.getcwd()
    os.chdir(a2)
    new_dir = os.getcwd()
    a1 = os.listdir()
    for a in a1: 
        b = f'p/united-states/{a2}/{a}/kinksters'
        get_xx(b)
        os.chdir(dir)
        os.chdir(new_dir)
        ws_X(a3,a4)

login()
sleep(0.5)
scrapes_x('california', '//main//div//a[@class="link f5 fw7 secondary mr1"]', "href")
