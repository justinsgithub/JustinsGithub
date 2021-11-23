#!/bin/python3
"""social media automation tool"""
import bot
from bot import sleep, By, Ec, Wait
import db

uc = db.user_collection
lc = db.location_collection
delete_data = db.delete_data
all_data = db.all_data
insert_data = db.insert_data
query_data = db.query_data
update_data = db.update_data
count_data = db.count_data
increment_data = db.increment_data

gets_page = bot.gets_page
finds_this = bot.finds_this
gets_text = bot.gets_text
gets_link = bot.gets_link
clickit = bot.clickit
enter_text = bot.enter_text

v = bot.my_variables
url = v["url"]
uname = v["username"]
pword = v["password"]

s = bot.my_selects
uinput = s["username_input"]
pinput = s["password_input"]
lbutton = s["login_button"]

driver = bot.driver


def login():
    driver.maximize_window()
    gets_page(url)
    enter_text(uinput, uname)
    enter_text(pinput, pword)
    clickit(lbutton)
