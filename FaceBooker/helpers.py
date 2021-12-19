import re
import os
from selenium.webdriver.common.by import By
import typer
from time import sleep

"""
            RE HELPERS
"""

def get_fb_id(link:str):
    this_id = re.sub(r"https://www.facebook.com/", "", link)
    this_id = re.sub(r"/friends_mutual", "", this_id)
    return this_id.strip()
    
def get_friends_mutual(link:str):
    id_plus_mutual = re.sub(r"https://www.facebook.com/", "", link)
    return id_plus_mutual.strip()
    
def delete_whitespace(my_strings: str):

    return re.sub("\s", "", my_strings)


def hyphenate(string_with_spaces: str):

    return re.sub("\s", "-", string_with_spaces.strip())


def get_this_word(sentence: str, array_position: int):

    seperated_sentence = re.split("\s", sentence)

    return seperated_sentence[array_position]


def get_last_word(sentence: str):

    word_array = re.split("\s", sentence)

    last_word = len(word_array) - 1

    return word_array[last_word]


def last_number_in_string(this_string):

    numbers_and_white_space = re.sub("\D", " ", this_string)

    stripped_ws = numbers_and_white_space.strip()

    number_string_array = re.split("\s", stripped_ws)

    last_number_string = len(number_string_array) - 1

    return int(number_string_array[last_number_string])


def delete_numbers(my_strings: str):

    return re.sub("\d", "", my_strings)


def delete_not_numbers(my_strings: str):

    return re.sub("\D", "", my_strings)


def extract_numbers(my_strings: str):

    my_string = my_strings.strip()

    number_string = re.sub("\D", "", my_string)

    return int(number_string)


"""
            BUILT-IN HELPERS
"""


def ch_username():

    this_prompt = "Enter your Facebook username"

    if os.path.isfile("secrets/username"):

        this_prompt = "Enter your new Facebook username"

    username = typer.prompt(this_prompt)

    with open("secrets/username", "w") as file:

        file.write(username)


def ch_password():

    this_prompt = "Enter your Facebook password"

    if os.path.isfile("secrets/password"):

        this_prompt = "Enter your new Facebook password"

    password = typer.prompt("Enter your new Facebook password")

    with open("secrets/password", "w") as file:

        file.write(password)


def strips(my_string: str):

    return my_string.strip()


def lowers(my_string: str):

    new_string = my_string.lower()

    return new_string


def append_to_file(file_name: str, content: str):

    with open(file_name, "a") as file:

        file.write(f"{content}\n")


def write_to_file(file_name: str, content: str):

    with open(file_name, "w") as file:

        file.write(f"{content}\n")


def list_file(file_name: str):

    with open(file_name, "r") as file:

        my_list = [line.strip() for line in file.readlines()]

        return my_list


"""
            WEBDRIVER HELPERS
"""


def find_this_x(wdriver, description: str):
    return wdriver.find_element(By.XPATH, description)


def find_these_x(wdriver, description: str):
    
    return wdriver.find_elements(By.XPATH, description)


def find_this_xtext(wdriver, description: str):
    return wdriver.find_element(By.XPATH, description).text


def find_these_xtext(wdriver, description: str):
    els = wdriver.find_elements(By.XPATH, description)
    return [el.text for el in els]


def find_these_xhref(wdriver, description: str):
    els = wdriver.find_elements(By.XPATH, description)
    return [el.get_attribute("href") for el in els]


def find_this_link(wdriver, description: str):
    return wdriver.find_element(By.LINK_TEXT, description)


def find_these_links(wdriver, description: str):
    return wdriver.find_elements(By.LINK_TEXT, description)


def jsclick(wdriver, this_target):
    wdriver.execute_script("arguments[0].click();", this_target)


def scroll_to_bottom(wdriver):
    wdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
