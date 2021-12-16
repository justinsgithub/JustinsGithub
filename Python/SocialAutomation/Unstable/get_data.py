import re
import helpers
import pymongo


from time import sleep
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from constants import my_vars, my_selectors, base_url
from bot import login

uri = my_vars["uri"]
cluster = pymongo.MongoClient(uri)
united_states_db = cluster["unitedStates"]
city_data_db = cluster["CitiesData"]

united_states_users_data = cluster["UnitedStatesUsersData"]

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
        
        result = united_states_db[name].insert_one(state)
        print(result)

def get_completed_city_links(state_name):
    this_state = united_states_db[state_name].find_one({"name": state_name})
    completed_cities = this_state["completedCities"]
    return completed_cities
    
def get_cities_user_pages(state_name):
    
    print(f'getting cities data for {state_name}')
    this_state = united_states_db[state_name].find_one({"name": state_name})
    city_links = this_state["cityLinks"]
    completed_city_links = get_completed_city_links(state_name)
    print(f"{len(completed_city_links)} completed city links")
    
    user_links = [f'{link}/{my_vars["users"]}' for link in city_links]
    
    user_pages = [link for link in user_links if not link in completed_city_links]
        
    return user_pages
    

def get_city_data(state_name):
    cities_user_pages = get_cities_user_pages(state_name)
    
    
    for cities_users in cities_user_pages:
        driver.get(cities_users)
        sleep(1)
        city = dict()

        users_per_page = 20
        max_pages = 450

        number_of_users_text = driver.find_element(
            By.XPATH, my_selectors["num_users_selector"]
        ).text
        number_of_users = helpers.extract_numbers(number_of_users_text)        
        city_name = driver.find_element(By.XPATH, my_selectors["city_name_selector"]).text

        pages_to_scrape = number_of_users / users_per_page
        
        print("pages to scrape ", pages_to_scrape)

        if pages_to_scrape > 450:
            pages_to_scrape = 450

        
        city["name"] = city_name
        city["totalUsers"] = number_of_users
        city["pagesToScrape"] = int(pages_to_scrape)
        city["pagesScraped"] = 1        
        city["usersLink"] = cities_users
        city["completedScraping"] = False
                
                
        state_collection = city_data_db[state_name]
        
        print(city)

        result1 = state_collection.insert_one(city)
        print(f"finished inserting {city}, into {state_name} result = ",result1)
        
        result2 =  united_states_db[state_name].update_one(
            {"name": state_name},
            { "$addToSet": { "completedCities" : cities_users } }
            )
        
        print(f"added {city_name} to scraped cities for {state_name}, result = ", result2)
    
    
def scrape_user_page(state_name, city_name):
    user_details_elements = driver.find_elements(By.XPATH, secrets.user_details_selector)
    view_picture_elements = driver.find_elements(By.XPATH, secrets.view_pictures_selector)
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
        user["city"] = city_name
        user["state"] = state_name
        user["active"] = True
        user["fatalErr"] = False
    
        print(user)    
    
        result = united_states_users_data[city_name].insert_one(user)
        print(result)


def scrape_city_users(state_name:str):
    cities_to_scrape = city_data_db[state_name].find({"completedScraping": False})
    for city in cities_to_scrape:
        print(city)
        start_page = city["scrapedPages"] + 1
        end_page = city["pagesToScrape"]
        
        if start_page >= end_page:
            result =  city_data_db[state_name].update_one(
                {"_id": city["_id"]}, { "completedScraping" : True })            
            
            continue
   
        for x in range(start_page, end_page):
            
            page_to_get = f'{city["usersLink"]}?page={str(x)}'
            driver.get(page_to_get)
            sleep(1)
            scrape_user_page(state_name, city["name"])
            helpers.increment_data(united_states_db[state_name], "name", city["name"], "scrapedPages", 1)

def main():
    
    states = united_states_db.list_collection_names()

    login(driver, By, my_vars["username2"], my_vars["password2"])
    
    for state in states:
        get_city_data(state) 