import re

from time import sleep

from selenium import webdriver

from selenium.common import exceptions

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from secrets import my_vars, my_selectors, base_url, user1, user2

import helpers as h

import check_errors as ce

chrome_opts = Options()

chrome_opts.add_argument("user-data-dir=selenium")

driver = webdriver.Chrome(options=chrome_opts)

def find_this_x(description:str):
    return driver.find_element(By.XPATH, description)

def find_these_x(description:str):
    return driver.find_elements(By.XPATH, description)

def find_this_xtext(description:str):
    return driver.find_element(By.XPATH, description).text

def find_this_link(description:str):
    return driver.find_element(By.LINK_TEXT, description)

def find_these_links(description:str):
    return driver.find_elements(By.LINK_TEXT, description)

def jsclick(target):
    driver.execute_script("arguments[0].click();", like)
    
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



def login(user):

    driver.maximize_window()

    driver.get(my_vars["home_page"])

    sleep(3)

    if not driver.title == my_vars["login_title"]:

        return

    username_input = find_this_x(my_selectors["username_in"])

    password_input = find_this_x(my_selectors["password_in"])

    log_button = find_this_x(my_selectors["login_button"])

    username_input.send_keys(user["username"])

    password_input.send_keys(user["password"])

    log_button.click()

    sleep(3)


def click_likes():

    try:

        likes = find_these_links(my_vars["like"])

        for like in likes:

            jsclick(like)
            
            sleep(0.2)

    except Exception:

        ce.unknown_err(driver)


def give_likes(pic_link):

    driver.get(pic_link)

    ce.login_title(driver)

    sleep(1)

    scroll_to_bottom()
    
    sleep(1)

    click_likes()


def get_pictures_link(site_user):

    try:

        driver.get(site_user["pictureLink"])

        sleep(1.0)

        ce.login_title(driver)

    except Exception:

        ce.unknown_err(driver)


def print_confirmation(site_user):

    p1 = f'getting user {site_user["userName"]} age {site_user["age"]}'

    p2 = f'gender {site_user["gender"]} from state {site_user["state"]}'

    print(p1, p2)


def like_pictures(state, db_users, this_user, this_query):

    liked_pictures = this_user["liked_pictures"]

    count = 0

    these_users = db_users[state].find(this_query)

    for user in these_users:

        print_confirmation(user)

        ce.count_200(driver, count)

        count += 1

        get_pictures_link(user)

        picture_link_selector = my_selectors["picture_link_selector"]

        picture_elements = find_these_x(picture_link_selector)

        picture_links = [el.get_attribute("href") for el in picture_elements]

        if len(picture_links) == 0:

            print("NO PICTURES OR COULD NOT FIND PAGE, PASSING")

            update = {"fatalErr": True}

            h.update_this(db_users[state], "_id", user["_id"], update)

            continue

        if len(picture_links) > 3:

            picture_links = [picture_links[x] for x in range(3)]

        try:

            driver.get(picture_links[0])

            ce.login_title(driver)

        except Exception:

            continue

        last_post = find_this_xtext(my_selectors["last_post"])

        year = h.last_number_in_string(last_post)

        print(f"last post was {last_post}")

        if year < 40:

            for picture_link in picture_links:

                give_likes(picture_link)

            liked_update = {liked_pictures: True}

            h.update_this(db_users[state], "_id", user["_id"], liked_update)

        else:

            print("last post older than 2020, passing")

            active_update = {"active": False}

            h.update_this(db_users[state], "_id", user["_id"], active_update)

        last_post_update = {"lastPicturePost": year}

        h.update_this(db_users[state], "_id", user["_id"], last_post_update)
