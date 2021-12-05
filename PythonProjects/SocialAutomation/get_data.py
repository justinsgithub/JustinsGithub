import secrets 
import helpers

from secrets import pa, userUrl, us_places
from driver_helpers import driver, By
from mongo_helpers import insert_data, increment_data



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
        
        insert_data(secrets.users[state], user, False)
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