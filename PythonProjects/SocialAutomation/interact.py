from time import sleep
from driver_helpers import driver, By, exceptions
import secrets

def like_picture(pic_page):
    driver.get(pic_page)
    sleep(0.25)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.25)
    try:
        love_button = driver.find_element(By.XPATH, secrets.like_button_selector)
        driver.execute_script("arguments[0].click();", love_button)
        print("liked picture")
        sleep(0.25)
    except exceptions.NoSuchElementException:
        print("no like button found")
        sleep(0.25)


def love_pictures(state):
    these_users = users[state].find({"iLikedPictures": False})
    for user in these_users:
        print("liking pics of user ", user["userName"], "age ", user["age"], "gender ", user["gender"], "from state", user["state"])
        driver.get(user["pictureLink"])
        sleep(0.25)
        picture_elements = driver.find_elements(By.XPATH, secrets.picture_link_selector)
        all_picture_links = [el.get_attribute("href") for el in picture_elements]
        picture_links = [all_picture_links[x] for x in range(3) if len(all_picture_links) > 3]

        for picture in picture_links:
            love_picture(picture)

        update_data(users[state], "_id", user["_id"], "jLikedPictures", True, False)

def follow_users(state):
    these_users = users[state].find({"xFollows": False})
    for user in these_users:
        print("liking pics of user ", user["userName"], "age ", user["age"], "gender ", user["gender"], "from state", user["state"])
        try:
            driver.get(user["profileLink"])
        except:
            print("unknown err getting ", user["profileLink"], " confirm to continue, CTRL-D to quit")
            should_continue = input()   
        try:
            follow = driver.find_element(By.XPATH, secrets.follow_selector)
            if follow.text == 'Follow':
                follow.click()
                update_data(these_users, "_id", user["_id"], "xFollows", True, False)
                
                print('now following user: ', user["userName"])
        except:
            print("no follow button found, moving to next iteration")