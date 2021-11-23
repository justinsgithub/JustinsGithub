#!/bin/python3
"""social media automation tool"""
import re
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait as Wait

my_selects = {
    "username_input":
    '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[1]/div/div/input',
    "password_input":
    '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[2]/div/div/input',
    "login_button":
    '/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button'
}
my_variables = {
    "url":
    "https://fetlife.com/users/sign_in",
    "username":
    "lovedaddyj",
    "password":
    "Hockey1343!"
}

driver = webdriver.Chrome()


def enter_text(selectme, txt):
    el = driver.find_element(By.XPATH, selectme)
    el.send_keys(txt)


def clickit(selectme):
    el = driver.find_element(By.XPATH, selectme)
    el.click()


def gets_page(url):
    print("getting page")
    driver.get(url)
    return driver.title


def finds_this(selectme, num: int):
    if num == 1:
        print("finding element")
        el = driver.find_element(By.XPATH, selectme)
        return el

    if num == 2:
        print("finding list of elements")
        els = driver.find_elements(By.XPATH, selectme)
        return els


def gets_text(selectme, num: int):
    if num == 1:
        el = driver.find_element(By.XPATH, selectme)
        txt = el.text
        return txt

    if num == 2:
        els = driver.find_elements(By.XPATH, selectme)
        txts = [el.text for el in els]
        return txts


def gets_link(selectme, getMany: bool):
    if not getMany:
        el = driver.find_element(By.XPATH, selectme)
        link = el.get_attribute("href")
        return link

    if getMany:
        els = driver.find_elements(By.XPATH, selectme)
        links = [el.get_attribute("href") for el in els]
        return links
