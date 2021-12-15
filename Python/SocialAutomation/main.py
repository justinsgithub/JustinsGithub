import re
from time import sleep

import pymongo
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from constants import my_vars, my_selectors
from db import update_data
from bot import login, get_state, love_pictures

uri = my_vars["uri"]
cluster = pymongo.MongoClient(uri)
users = cluster["users"]

chrome_opts = Options()
chrome_opts.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_opts)


login(driver, By, my_vars["username1"], my_vars["password1"])
# wyoming
#these_states = ["Wisconsin", "West Virginia", "Virginia", "Vermont"]
these_states = [ "Missouri", "Iowa", "Massachusetts", "Tennessee"]
for state in these_states:
    this_state = get_state(state, users)
    love_pictures(this_state, users, driver, By, my_vars["current_user_1"])
