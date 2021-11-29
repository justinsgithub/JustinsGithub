#!/bin/python3
"""social media automation tool"""
import re
from secrets import (my_variables, my_selects, us_url, follow_selector,
                     profile_link_selector, num_users_selector)
import bot
import db
from time import sleep
from selenium.webdriver.common.by import By

driver = bot.driver

user_collection = db.user_collection
location_collection = db.location_collection

delete_data = db.delete_data
all_data = db.all_data
insert_data = db.insert_data
query_data = db.query_data
update_data = db.update_data
count_data = db.count_data
increment_data = db.increment_data

finds_this = bot.finds_this
gets_text = bot.gets_text
gets_link = bot.gets_link
clickit = bot.clickit
enter_text = bot.enter_text

url = my_variables["url"]
uname = my_variables["username"]
pword = my_variables["password"]

uinput = my_selects["username_input"]
pinput = my_selects["password_input"]
lbutton = my_selects["login_button"]


def login():
    driver.maximize_window()
    driver.get(url)
    enter_text(uinput, uname)
    enter_text(pinput, pword)
    clickit(lbutton)


def fetch_data():
    driver.get(us_url)
    us_names = gets_text('//main/div//a', 2)
    for state in us_names:
        driver.get(us_url)
        state_selector = driver.find_element(By.LINK_TEXT, state)
        state_href = state_selector.get_attribute("href")
        user_link = state_href + "/users"
        driver.get(user_link)
        sleep(1)
        num_users_text = gets_text(num_users_selector, 1)
        rm_comma = re.sub(",", "", num_users_text)
        num_users = int(rm_comma)
        update_data(location_collection, "name", state, "numberOfUsers",
                    num_users, False)
        pages_available = num_users / 20
        update_data(location_collection, "name", state, "pages_available",
                    pages_available, False)


def update_data2():
    us_states = all_data(location_collection)
    state_names = [state["name"] for state in us_states]
    for state in state_names:
        formatted_state = re.sub("\s", "-", state)
        clean_state = formatted_state.strip()
        lower_state = clean_state.lower()
        user_url = "https://examplesite.com/p/united-states/" + lower_state + "/users"
        update_data(location_collection, "name", state, "userUrl", user_url,
                    False)


def get_users():
    us_states = all_data(location_collection)
    base_user_url = "https://examplesite.com/users/"
    delete_this = ""
    for state in us_states:
        driver.get(state["userUrl"])
        profile_links = gets_link(profile_link_selector, True)
        print(profile_links)
        user_ids = []
        for link in profile_links:
            print(link)
            user_id = re.sub(base_user_url, delete_this, link)
            user_ids.append(user_id)
            print(user_id)

        print(user_ids)
        update_data(location_collection, "name", state["name"], "users",
                    user_ids, False)


def follow_users():
    all_users = all_data(user_collection)
    for x in range(count_data(user_collection)):
        profile_url = all_users[x]["profile_url"]
        print("getting ", profile_url)
        try:
            driver.get(profile_url)
        except:
            print(
                "could not get profile page, could be critical error, breaking now"
            )
            return
        try:
            follow = driver.find_element(By.XPATH, follow_selector)

            if follow.text == 'Follow':
                follow.click()
                update_data(user_collection, "profile_url", profile_url,
                            "imFollowing", True, False)
                iFollow = all_users[x]["imFollowing"]
                this_id = all_users[x]["_id"]
                print('now following user id: ', this_id, iFollow)

        except:
            print("no follow button found, moving to next iteration")