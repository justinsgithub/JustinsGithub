import re
from time import sleep

from constants import my_vars, my_selectors, base_url
from db import update_data
import helpers


def login(this_driver, By, username, password):
    username_in = my_selectors["username_in"]
    password_in = my_selectors["password_in"]
    login_button = my_selectors["login_button"]
    this_driver.maximize_window()
    this_driver.get(my_vars["home_page"])
    sleep(5)
    if not this_driver.title == my_vars["login_title"]:
        return

    username_input = this_driver.find_element(By.XPATH, username_in)
    password_input = this_driver.find_element(By.XPATH, password_in)
    log_button = this_driver.find_element(By.XPATH, login_button)
    username_input.send_keys(username)
    password_input.send_keys(password)
    log_button.click()
    sleep(5)
    
def get_state(state_name, these_users):
    these_states = these_users.list_collection_names()
    print(these_states)

    for state in these_states:
        if state == state_name:
            return state


def love_picture(pic_link, this_driver, By):
    this_driver.get(pic_link)
    if this_driver.title == my_vars["login_title"]:
        this_driver.quit()
        quit()
    sleep(1)
    this_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    try:
        love_links = this_driver.find_elements(By.LINK_TEXT, "Love")
        num_comments = 0
        for love_link in love_links:
            this_driver.execute_script("arguments[0].click();", love_link)
            num_comments += 1
            sleep(0.2)
        print(f"liked {num_comments} comments")
    except Exception:
        print("ERROR CLICKING LINK")
        sleep(1.0)


def love_pictures(state, db_users, this_driver, By, current_user):
    count = 0
    this_query = {current_user: False, "active": True, "fatalErr": False}
    these_users = db_users[state].find(this_query)
    # list() may mutate objects!!
    for user in these_users:
        p1 = f'getting user {user["userName"]} age {user["age"]}'
        p2 = f'gender {user["gender"]} from state {user["state"]}'
        if count == 200:
            print("hit 200 quitting now")
            this_driver.quit()
            quit()
        #if user["gender"] == "M":
        count += 1
        print(p1, p2)
        try:
            this_driver.get(user["pictureLink"])
            if this_driver.title == my_vars["login_title"]:
                this_driver.quit()
                quit()
            sleep(1.0)
        except Exception:
            print("unknown error, continue?")
            this_driver.quit()
            quit()
            sleep(1.0)

        picture_link_selector = my_selectors["picture_link_selector"]
        picture_elements = this_driver.find_elements(By.XPATH,
                                                picture_link_selector)

        picture_links = [el.get_attribute("href") for el in picture_elements]

        if len(picture_links) == 0:
            print("NO PICTURES OR COULD NOT FIND PAGE, PASSING")
            update_data(db_users[state], "_id", user["_id"], "fatalErr", True,
                        False)

            continue

        if len(picture_links) > 3:
            picture_links = [picture_links[x] for x in range(3)]

        try:
            this_driver.get(picture_links[0])
            if this_driver.title == my_vars["login_title"]:
                this_driver.quit()
                quit()
        except Exception:
            continue

        last_post = this_driver.find_element(
            By.XPATH, '//*[@id="ptr-main-element"]//div/main//a/time').text
        year = helpers.last_number_in_string(last_post)
        print(f"last post was {last_post}")

        if year < 40:
            for picture_link in picture_links:
                love_picture(picture_link, this_driver, By)

            update_data(db_users[state], "_id", user["_id"], current_user,
                        True, False)

        else:
            print("last post older than 2020, passing")
            update_data(db_users[state], "_id", user["_id"], "active", False,
                        False)

        update_data(db_users[state], "_id", user["_id"], "lastPicturePost",
                    year, False)
