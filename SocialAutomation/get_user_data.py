import re

import helpers

import pymongo

from time import sleep

from selenium.common import exceptions

from selenium.webdriver.common.by import By

from secrets import my_vars, my_selectors, base_url, user2

from get_city_data import login

uri = my_vars["uri"]

cluster = pymongo.MongoClient(uri)

united_states_db = cluster["unitedStates"]

city_data_db = cluster["CitiesData"]

united_states_users_data = cluster["UnitedStatesUsersData"]

driver = login(user2)

class User:
    def __init__(self, username):
        self.database = cluster["UnitedStatesUsers"]
        self.username = username

class Program:
    def __init__(self):
        print("finish later")

def scrape_user_page(state_name, city_name):

    user_details_elements = driver.find_elements(By.XPATH,
                                                 secrets.user_details_selector)

    view_picture_elements = driver.find_elements(
        By.XPATH, secrets.view_pictures_selector)

    username_elements = driver.find_elements(By.XPATH,
                                             secrets.user_name_selector)

    user_details_text = [el.text for el in user_details_elements]

    view_pictures_text = [el.text for el in view_picture_elements]

    user_profile_links = [el.get_attribute("href") for el in username_elements]

    user_picture_links = [link + "/pictures" for link in user_profile_links]

    usernames = [el.text for el in username_elements]

    user_ids = [
        helpers.delete_not_numbers(text) for text in user_profile_links
    ]

    user_ages = [helpers.get_age(text) for text in user_details_text]

    user_genders = [helpers.get_gender(text) for text in user_details_text]

    user_styles = [
        helpers.get_this_word(text, -1) for text in user_details_text
    ]

    user_num_pics = [helpers.get_age(text) for text in view_pictures_text]

    for x in range(len(user_num_pics)):

        user = dict()

        user["site_id"] = user_ids[x]

        user["profileLink"] = user_profile_links[x]

        user["pictureLink"] = user_picture_links[x]

        user["userName"] = usernames[x]

        user["age"] = user_ages[x]

        user["gender"] = user_genders[x]

        user["style"] = user_styles[x]

        user["numberOfPics"] = user_num_pics[x]

        user["jFollows"] = False

        user["lFollows"] = False

        user["xFollows"] = False

        user["followsMe"] = False

        user["iLikedPictures"] = False

        user["jLikedPictures"] = False

        user["lLikedPictures"] = False

        user["xLikedPictures"] = False

        user["city"] = city_name

        user["state"] = state_name

        user["active"] = True

        user["fatalErr"] = False

        print(user)

        result = united_states_users_data[city_name].insert_one(user)

        print(result)


def scrape_city_users(state_name: str):

    cities_to_scrape = city_data_db[state_name].find(
        {"completedScraping": False})

    for city in cities_to_scrape:

        print(city)

        start_page = city["scrapedPages"] + 1

        end_page = city["pagesToScrape"]

        if start_page >= end_page:

            result = city_data_db[state_name].update_one(
                {"_id": city["_id"]}, {"completedScraping": True})

            continue

        for x in range(start_page, end_page):

            page_to_get = f'{city["usersLink"]}?page={str(x)}'

            driver.get(page_to_get)

            sleep(1)

            scrape_user_page(state_name, city["name"])

            helpers.increment_data(united_states_db[state_name], "name",
                                   city["name"], "scrapedPages", 1)
