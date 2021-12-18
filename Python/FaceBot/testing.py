#!/bin/python3
import os

import helpers as h

from getpass import getuser

from selenium import webdriver

from selenium.common import exceptions

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from time import sleep

import typer

chrome_options = Options()

prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("user-data-dir=selenium")

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

username = getuser()


onyourmind_class = "oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn b3i9ofy5 orhb3f3m czkt41v7 fmqxjp7s emzo65vh j83agx80 btwxx1t3 buofh1pr jifvfom9 l9j0dhe7 idiwt2bm kbf60n1y cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq"
onyourmind_class2 = (
    "rq0escxv buofh1pr df2bnetk hv4rvrfc dati1w0a l9j0dhe7 k4urcfbm du4w35lb gbhij3x4"
)

constants = {
    "base_url": "https://facebook.com",
    "login_title": "Facebook - Log In or Sign Up",
}

xpaths = {
    "username_input": '//*[@id="email"]',
    "password_input": '//*[@id="pass"]',
    "login_button": '//button[@type="submit"][1]',
    "onyourmind": f'//div[@class="{onyourmind_class}"][@role="button"]',
    "input_box": '//div[@style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"][@role="textbox"][@contenteditable="true"]',
    "post_button": '//div[@aria-label="Post"][@role="button"][@tabindex="0"]',
}


def login():

    if not os.path.isdir("secrets"):

        typer.secho("Welcome to your FaceBot", fg="green")

        os.mkdir("secrets")

    if not os.path.isfile("secrets/username"):

        h.ch_username()

    if not os.path.isfile("secrets/password"):

        h.ch_password()

    driver.get(constants["base_url"])

    sleep(2)

    with open("secrets/username") as file:
        username = file.read()

    with open("secrets/password") as file:
        password = file.read()

    if driver.title == constants["login_title"]:
        username_input = h.find_this_x(driver, xpaths["username_input"])
        password_input = h.find_this_x(driver, xpaths["password_input"])
        login_button = h.find_this_x(driver, xpaths["login_button"])

        username_input.send_keys(username)
        sleep(1)
        password_input.send_keys(password)
        sleep(1)
        login_button.click()

        await_command = typer.prompt("please confirm login was success")


def make_post():
    login()
    sleep(1)

    onyourmind = h.find_this_x(driver, xpaths["onyourmind"])

    onyourmind.click()

    sleep(2)

    inputbox = driver.find_element(By.XPATH, xpaths["input_box"])

    inputbox.send_keys("Hello from Justins new FB automation App")

    sleep(2)

    post_button = driver.find_element(By.XPATH, xpaths["post_button"])

    post_button.click()


def changepassword():

    h.ch_password()


def changeusername():

    h.ch_username()


make_post()
