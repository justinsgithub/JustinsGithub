#!/bin/python3
"""social media automation tool"""
import bot
import db


sleep = bot.sleep
by = bot.By
byx = by.XPATH
ec = bot.Ec
wait = bot.Wait
re = bot.re

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

def fetch_data():
    driver.get("https://fetlife.com/p/united-states")
    us_names1 = gets_text('//main/div//a', 2)
    for state in us_names1:
        driver.get("https://fetlife.com/p/united-states")
        state_selector = driver.find_element(by.LINK_TEXT, state)
        state_href = state_selector.get_attribute("href")
        kinkster_link = state_href + "/kinksters"
        driver.get(kinkster_link)
        sleep(1)
        num_kinksters_text = gets_text('//*[@id="main-content"]/div/header/div/div[2]/a[2]/div/div/span', 1)
        rm_comma = bot.re.sub(",","",num_kinksters_text)
        num_kinksters = int(rm_comma)
        update_data(lc, "name", state, "numberOfKinksters", num_kinksters, False)
        pages_available = num_kinksters / 20
        update_data(lc, "name", state, "pages_available", pages_available, False)

login()
fetch_data()
