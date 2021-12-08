#!/bin/python3
"""social media automation tool"""

import secrets
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_opts = Options()
chrome_opts.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_opts)


def enter_text(my_selector:str, my_text:str):
    try:
        el = driver.find_element(By.XPATH, my_selector)
        el.send_keys(my_text)
        return True
    except exceptions.NoSuchElementException:
        return False
    
def input_this(my_selector:str, my_text:str):
    is_entered = enter_text(my_selector, my_text)
    while not is_entered:
        print("element not found, enter new XPATH or CTRL-D to Quit")
        new_el = input()
        is_entered = enter_text(new_el)    



def click(my_selector:str):
    try:
        el = driver.find_element(By.XPATH, my_selector)
        el.click()
        return True
    except exceptions.NoSuchElementException:
        return False
        
def click_this(my_selector:str):
    is_clicked = click(my_selector)
    while not is_clicked:
        print("element not found, enter new XPATH or CTRL-D to Quit")
        new_el = input()
        is_clicked = click(new_el)    
        

def find_this(my_selector:str):
    el = driver.find_element(By.XPATH, my_selector)
    return el

def find_these(my_selector:str):
    els = driver.find_elements(By.XPATH, my_selector)
    return els

def login():
    driver.maximize_window()
    driver.get(secrets.sign_in)
    sleep(5)
    try:
        username_input = driver.find_element(By.XPATH, secrets.username_in)
        password_input = driver.find_element(By.XPATH, secrets.password_in)
        log_button = driver.find_element(By.XPATH, secrets.login_button)
        username_input.send_keys(secrets.username)
        password_input.send_keys(secrets.password)
        log_button.click()
        sleep(5)
    except:
        print("unknown err logging in, confirm to continue, CTRL-D to quit")
        should_continue = input()   