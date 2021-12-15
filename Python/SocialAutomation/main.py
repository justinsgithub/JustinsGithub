import re
from time import sleep

import pymongo
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from constants import my_vars, my_selectors
from db import update_data
from bot import driver, login, get_state, love_pictures

uri = my_vars["uri"]
cluster = pymongo.MongoClient(uri)
users = cluster["users"]


login()

these_states = ["New Jersey"]

for state in these_states:
    this_state = get_state(state, users)
    love_pictures(this_state, users)

