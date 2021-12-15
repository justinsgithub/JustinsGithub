import re
from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from constants import my_vars, my_selectors, base_url
from db import update_data
from bot import login
import helpers
import pymongo

uri = my_vars["uri"]
cluster = pymongo.MongoClient(uri)
unitedStates_db = cluster["unitedStates"]
chrome_opts = Options()
chrome_opts.add_argument("user-data-dir=seleniumuser2")
driver = webdriver.Chrome(options=chrome_opts)



def get_state_data():
    driver.get(my_vars["us_places"])
    state_elements = driver.find_elements(By.XPATH, my_selectors["states_selector"])
    state_names = [state_element.text for state_element in state_elements]
    state_hrefs = [state_element.get_attribute("href") for state_element in state_elements]
    state_city_links = [state_href + "/" + my_vars["within"] for state_href in state_hrefs]
    
    for x in range(len(state_elements)):
       
        state = dict()
        sleep(1) 
        name = state_names[x]
        state["name"] = name
        state["href"] = state_hrefs[x]
        
        state["citiesLink"] = state_city_links[x]
        
        print(state)
        
        driver.get(state["href"])
        
        sleep(1)
        num_users = driver.find_element(By.XPATH, my_selectors["num_users_selector"]).text
        num_cities = driver.find_element(By.XPATH, my_selectors["num_cities_selector"]).text
        state["totalUsers"] = helpers.extract_numbers(num_users)
        state["totalCities"] = helpers.extract_numbers(num_cities)
        
        
        driver.get(state["citiesLink"])
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        city_elements = driver.find_elements(By.XPATH, my_selectors["cities_selector"])
        city_names = [city_element.text for city_element in city_elements]
        city_links = [city_element.get_attribute("href") for city_element in city_elements]
        
        state["cityLinks"] = city_links
        state["cityNames"] = city_names
        state["completedCities"] = []
        state["scrapedAllCities"] = False
        
        result = unitedStates_db[name].insert_one(state)
        print(result)
        
login(driver, By, my_vars["username2"], my_vars["password2"])

    
get_state_data()    

"""

this_state = "California"
driver.get(f"{secrets.us_places}/{this_state}")

united_states_database = cluster["UnitedStatesData"]

state = "California"

state_collection = united_states_database[state]


def get_state(this_state):
    try:
        driver.get(f"{secrets.us_places}/{this_state}")
        return True
    except Exception:
        print("error getting url, continue?")
        confirm = input()
        return False


def get_cities_data(this_state):

    if not this_state:
        return

    city_elements = driver.find_elements(By.XPATH, '//div[@class="mw8 nl2 nr2"]//a')

    for city_element in city_elements:
        users_per_page = 20
        max_pages = 450

        city_name = city_element.text

        city_link = city_element.get_attribute("href")

        city_users_link = city_link + "/kinksters"

        city_data = dict()

        driver.get(city_users_link)

        number_of_users_span = driver.find_element(
            By.XPATH, my_selectors["number_of_users_span_selector"]
        )

        number_of_users_text = number_of_users_span.text

        number_of_users = helpers.extract_numbers(number_of_users_text)
        print("number of users", number_of_users)

        pages_to_scrape = number_of_users / 20
        print("pages to scrape", pages_to_scrape)

        if pages_to_scrape > 450:
            pages_to_scrape = 450

        city_data["name"] = location_name
        city_data["usersLink"] = location_data
        city_data["numberOfUsers"] = number_of_users
        city_data["scrapedPages"] = 0
        city_data["pagesToScrape"] = pages_to_scrape

        print(city_data)
        # state_collection.insert_one(city_data)




def scrape_user_page(state):
    user_details_elements = driver.find_elements(By.XPATH, secrets.user_details_selector)
    view_picture_elements = driver.find_elements(By.XPATH,secrets.view_pictures_selector)
    username_elements = driver.find_elements(By.XPATH, secrets.user_name_selector)


    user_details_text = [el.text for el in user_details_elements]
    view_pictures_text = [el.text for el in view_picture_elements]
    user_profile_links = [el.get_attribute("href") for el in username_elements]
    user_picture_links = [link + "/pictures" for link in user_profile_links]
    usernames = [el.text for el in username_elements]
    
    user_ids = [helpers.delete_not_numbers(text) for text in user_profile_links]
    user_ages = [helpers.get_age(text) for text in user_details_text]
    user_genders = [helpers.get_gender(text) for text in user_details_text]
    user_styles = [helpers.get_this_word(text, -1) for text in user_details_text]
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
        user["state"] = state
        
        insert_data(secrets.users[state], user)
        print(user)

def get_user_pages():
    states = secrets.locations.find({})
    for state in states:
        print(state)
        start_page = state["scrapedPages"] + 1
        end_page = 450
        for x in range(start_page, end_page):
            sleep(5)
            page = state[userUrl] + pa + str(x)
            driver.get(page)
            scrape_user_page(state["name"])
            increment_data(secrets.locations, "name", state["name"], "scrapedPages", 1,
                           False)
"""