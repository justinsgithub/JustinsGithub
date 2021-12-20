import re

from time import sleep

from selenium import webdriver

from selenium.common import exceptions

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from secrets import my_vars, my_selectors, base_url, user1, user2

import helpers as h

import check_errors as ce

chrome_options = Options()

chrome_options.add_argument("user-data-dir=seleniumuser2")

driver = webdriver.Chrome(options=chrome_options)


def find_this_x(description: str):
    return driver.find_element(By.XPATH, description)


def find_these_x(description: str):
    return driver.find_elements(By.XPATH, description)


def find_this_xtext(description: str):
    return driver.find_element(By.XPATH, description).text


def find_these_xtext(description: str):
    els = driver.find_elements(By.XPATH, description)
    return [el.text for el in els]


def find_these_xhref(description: str):
    els = driver.find_elements(By.XPATH, description)
    return [el.get_attribute("href") for el in els]


def find_this_link(description: str):
    return driver.find_element(By.LINK_TEXT, description)


def find_these_links(description: str):
    return driver.find_elements(By.LINK_TEXT, description)


def jsclick(this_target):
    driver.execute_script("arguments[0].click();", this_target)
    sleep(0.2)


def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)


def login(user):

    driver.maximize_window()

    driver.get("https://beenverified.com")

    sleep(5)

    if not driver.title == my_vars["login_title"]:

        return

    username_input = find_this_x('//*[@id="login-email"]')

    password_input = find_this_x('//*[@id="login-password"]')

    log_button = find_this_x('//*[@id="submit"]')

    username_input.send_keys("")

    password_input.send_keys(user["password"])

    log_button.click()

    sleep(5)


def click_likes():

    try:
        likes = find_these_links(my_vars["like"])

        for like in likes:

            jsclick(like)

        sleep(1)

    except Exception:
        sleep(1)
        return


def give_likes(pic_link):
    try:
        driver.get(pic_link)

        ce.login_title(driver)

        sleep(1)

        scroll_to_bottom()

        click_likes()

        sleep(1)
    except Exception:
        return


def get_picture_links(site_user):

    driver.get(site_user["pictureLink"])

    sleep(1.0)

    ce.login_title(driver)

    return find_these_xhref(my_selectors["picture_link_selector"])


def print_confirmation(site_user):

    p1 = f'getting user {site_user["userName"]} age {site_user["age"]}'

    p2 = f'gender {site_user["gender"]} from state {site_user["state"]}'

    print(p1, p2)


def like_pictures(state, db_users, this_user):

    liked_pictures = this_user["liked_pictures"]

    this_query = {
        liked_pictures: False,
        "active": True,
        "fatalErr": False,
        "isMale": True
    }

    count = 0

    these_users = db_users[state].find(this_query)

    for user in these_users:

        print_confirmation(user)

        ce.count_400(driver, count)

        count += 1

        picture_links = get_picture_links(user)

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

        if year > 40:
            print("LAST POST OLDER THAN 2020, ONLY LIKING THIS PIC")

            scroll_to_bottom()

            click_likes()

            active_update = {"active": False}

            h.update_this(db_users[state], "_id", user["_id"], active_update)

        liked_update = {liked_pictures: True}

        h.update_this(db_users[state], "_id", user["_id"], liked_update)

        last_post_update = {"lastPicturePost": year}

        h.update_this(db_users[state], "_id", user["_id"], last_post_update)
