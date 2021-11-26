import secrets
from bot import driver, By

from helpers import delete_not_numbers, get_this_word, get_age, get_gender


class UsersPage:

    user_details_elements = driver.find_element(By.XPATH,
                                                secrets.user_details_selector)

    user_details_text = [el.text for el in user_details_elements]

    view_picture_elements = driver.find_elements(
        By.XPATH, secrets.view_pictures_selector)

    view_pictures_text = [el.text for el in view_picture_elements]

    username_elements = driver.find_elements(By.XPATH,
                                             secrets.user_name_selector)

    user_profile_links = [el.get_attribute("href") for el in username_elements]

    user_picture_links = [link + "/pictures" for link in user_profile_links]

    user_ids = [delete_not_numbers(text) for text in user_profile_links]

    usernames = [el.text for el in username_elements]

    user_ages = [get_age(text) for text in user_details_text]

    user_genders = [get_gender(text) for text in user_details_text]

    user_styles = [get_this_word(text, -1) for text in user_details_text]

    user_num_pics = [get_age(text) for text in view_pictures_text]


class PicturesPage:

    picture_elements = driver.find_elements(By.XPATH,
                                            secrets.picture_link_selector)

    picture_links = [el.get_attribute("href") for el in picture_elements]

    picture_links = [
        picture_links[x] for x in range(4) if len(picture_links) > 4
    ]

    follow_button_selector = driver.find_element(
        By.XPATH, secrets.follow_button_selector)


class PicturePage:

    love_button = driver.find_element(By.XPATH, secrets.love_button_selector)

    comment_input = driver.find_element(By.XPATH,
                                        secrets.comment_input_selector)

    comment_button = driver.find_element(By.XPATH,
                                         secrets.comment_button_selector)
