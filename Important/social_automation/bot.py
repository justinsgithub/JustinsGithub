from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions

chrome_opts = Options()
chrome_opts.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_opts)
cluster = pymongo.MongoClient(uri)
db = cluster["site1"]
users_database = cluster["users"]
users = db["users"]
locations = db["locations"]
jusers = db["jusers"]
lusers = db["lusers"]
profile_url = base_url + "/users/"
login_button = "/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button"
user_name_selector = "//a[@class='link f5 fw7 secondary mr1']"

user_details_selector = "//div[@id='main-content']//main//div[@style='max-height: " \
                      "60px;']//span[@class='f6 fw7 gray-300']"
view_pictures_selector = "//main//div//a[@class='link gray hover-gray-300 dot-separated'][1]"
picture_link_selector = "//a[@class='aspect-ratio--1x1 relative db bg-animate " \
                      "no-underline " \
                   "overflow-hidden br1 tap-highlight-transparent bg-gray-900 " \
                   "hover-bg-gray-950']"
follow_button_selector = '//button[@name="button"][@data-color="secondary"]'
# follow_button_selector = '//button[@name="button"][1]'
following_button_selector = '//button[@name="button"][@data-color="lined"]'
# following_button_selector = '//button[@name="button"][2]'
love_button_selector = '//a[@title="Love"][text()="Love"]'
#love_button_selector = '//a[text()="Love"]'
#love_button_selector = '//a[contains(text(), "Love")]'
comment_input_selector = "//div[@id='new_comment']//form/div/div/textarea"
comment_button_selector = "//div[@id='new_comment']//form/div/div/textarea//button[1]"


def strips(my_string: str):
    return my_string.strip()


def lowers(my_string: str):
    new_string = my_string.lower()
    return new_string


def append_to_file(file_name: str, content: str):
    with open(file_name, "a") as file:
        file.write(f'{content}\n')


def write_to_file(file_name: str, content: str):
    with open(file_name, "w") as file:
        file.write(f'{content}\n')


def list_file(file_name: str):
    with open(file_name, "r") as file:
        my_list = [line.strip() for line in file.readlines()]
        return my_list


def delete_whitespace(my_strings: str):
    return re.sub("\s", "", my_strings)


def hyphenate(string_with_spaces: str):
    return re.sub("\s", "-", string_with_spaces.strip())


def get_this_word(sentence: str, array_position: int):
    seperated_sentence = re.split("\s", sentence)
    return seperated_sentence[array_position]


def delete_numbers(my_strings: str):
    return re.sub("\d", "", my_strings)


def delete_not_numbers(my_strings: str):
    return re.sub("\D", "", my_strings)


def get_age(content: str):
    return delete_not_numbers(get_this_word(content, 0))


def get_gender(content: str):
    return delete_numbers(get_this_word(content, 0))


def delete_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("deleting all data")
        collection.delete_many({thiskey: thisvalue})
        print("succesfully deleted")

    if not isMany:
        print("deleting single data")
        collection.delete_one({thiskey: thisvalue})
        print("succesfully deleted")


def insert_data(collection, data, isMany: bool):
    if isMany:
        print("inserting all data")
        collection.insert_many(data)
        print(data)

    if not isMany:
        print("inserting single data")
        collection.insert_one(data)
        print(data)


def all_data(collection):
    print("getting all data in collection")
    results = collection.find({})
    for result in results:
        print(result)
    return results


def query_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("getting all data in search")
        return collection.find({thiskey: thisvalue})

    if not isMany:
        print("getting first data matching query")
        return collection.find_one({thiskey: thisvalue})


def update_data(collection, thiskey, thisvalue, newkey, newvalue,
                isMany: bool):
    if isMany:
        collection.update_many({thiskey: thisvalue},
                               {"$set": {
                                   newkey: newvalue
                               }})
        print("data updated")

    if not isMany:
        collection.update_one({thiskey: thisvalue},
                              {"$set": {
                                  newkey: newvalue
                              }})
        print("data updated")


def count_data(collection):
    data_count = collection.count_documents({})
    print(data_count)
    return data_count


def increment_data(collection, querykey, queryvalue, incrementkey,
                   incrementvalue: int, isMany: bool):
    if isMany:
        print("incrementing data in query")
        collection.update_many({querykey: queryvalue},
                               {"$inc": {
                                   incrementkey: incrementvalue
                               }})
        print("data updated")

    if not isMany:
        print("incrementing data in query")
        collection.update_one({querykey: queryvalue},
                              {"$inc": {
                                  incrementkey: incrementvalue
                              }})
        print("data updated")


def login():
    username_in = "/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[" \
                     "1]/div/div/input"
    password_in = "/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div[" \
                     "2]/div/div/input"
    driver.maximize_window()
    driver.get(sign_in)
    sleep(10)
    username_input = driver.find_element(By.XPATH, username_in)
    password_input = driver.find_element(By.XPATH, password_in)
    log_button = driver.find_element(By.XPATH, login_button)
    username_input.send_keys(username)
    password_input.send_keys(password)
    log_button.click()
    sleep(10)


def scrape_user_page(state):
    user_details_elements = driver.find_elements(By.XPATH,
                                                 user_details_selector)
    user_details_text = [el.text for el in user_details_elements]
    view_picture_elements = driver.find_elements(By.XPATH,
                                                 view_pictures_selector)
    view_pictures_text = [el.text for el in view_picture_elements]
    username_elements = driver.find_elements(By.XPATH, user_name_selector)
    user_profile_links = [el.get_attribute("href") for el in username_elements]
    user_picture_links = [link + "/pictures" for link in user_profile_links]
    user_ids = [delete_not_numbers(text) for text in user_profile_links]
    usernames = [el.text for el in username_elements]
    user_ages = [get_age(text) for text in user_details_text]
    user_genders = [get_gender(text) for text in user_details_text]
    user_styles = [get_this_word(text, -1) for text in user_details_text]
    user_num_pics = [get_age(text) for text in view_pictures_text]
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
        user["iFollow"] = False
        user["followsMe"] = False
        user["iLikedPictures"] = False
        user["state"] = state
        insert_data(users_database[state], user, False)
        print(user)


def get_user_pages():
    states = locations.find({})
    for state in states:
        print(state)
        start_page = state["scrapedPages"] + 1
        end_page = 450
        for x in range(start_page, end_page):
            sleep(5)
            page = state["kinksterUrl"] + "?page=" + str(x)
            driver.get(page)
            scrape_user_page(state["name"])
            increment_data(locations, "name", state["name"], "scrapedPages", 1,
                           False)


def love_picture(pic_page):
    driver.get(pic_page)
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        love_button = driver.find_element(By.XPATH, love_button_selector)
        driver.execute_script("arguments[0].click();", love_button)
        print("liked picture")
    except exceptions.NoSuchElementException:
        print("no like button found")


def love_pictures():
    these_users = all_data(jusers)
    for user in these_users:
        page = user["pictureLink"]
        print(page)
        driver.get(page)
        sleep(5)
        picture_elements = driver.find_elements(By.XPATH,
                                                picture_link_selector)

        picture_links = [el.get_attribute("href") for el in picture_elements]

        picture_links = [
            picture_links[x] for x in range(4) if len(picture_links) > 4
        ]

        for picture in picture_links:
            love_picture(picture)
            print(picture)

        update_data(jusers, "_id", user["_id"], "iLikedPictures", True, False)
