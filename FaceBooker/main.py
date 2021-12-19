#!/bin/python3
"""
testing functions before using in main 
"""


import os

import helpers as h

from getpass import getuser

from selenium import webdriver

from selenium.common import exceptions

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from time import sleep

import datetime

import typer

app = typer.Typer()

chrome_options = Options()

prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("user-data-dir=seleniumfacebook")

username = getuser()

begin = """
        
"""
end = """
        
"""

friends_links_a = 'a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 m9osqain b1v8xokw"]'
onyourmind_class = "oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn b3i9ofy5 orhb3f3m czkt41v7 fmqxjp7s emzo65vh j83agx80 btwxx1t3 buofh1pr jifvfom9 l9j0dhe7 idiwt2bm kbf60n1y cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq"


num_friends_class = (
    "d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua e9vueds3 j5wam9gi b1v8xokw q66pz984"
)

constants = {
    "base_url": "https://www.facebook.com",
    "login_title": "Facebook - Log In or Sign Up",
}

xpaths = {
    "username_input": '//*[@id="email"]',
    "password_input": '//*[@id="pass"]',
    "login_button": '//button[@type="submit"][1]',
    "onyourmind": f'//div[@class="{onyourmind_class}"][@role="button"]',
    "input_box": '//div[@style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"][@role="textbox"][@contenteditable="true"]',
    "post_button": '//div[@aria-label="Post"][@role="button"][@tabindex="0"]',
    "profile_link": '//a[@href="/me/"]',
    "num_of_friends": f'//span[@class="{num_friends_class}"]',
    "friend_links": f"//div//div//div//div//{friends_links_a}",
    "friend_name": '//h1[@class="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl"][@tabindex="-1"]',
}


@app.command()
def changepassword(
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    )
):

    with open("secrets/password", "w") as file:

        file.write(password)

    typer.secho(f"{begin}     password updated{end}", fg="green")


@app.command()
def changeusername(
    username: str = typer.Option(..., prompt=True, confirmation_prompt=True)
):

    with open("secrets/username", "w") as file:

        file.write(username)

    typer.secho(f"{begin}     username updated{end}", fg="green")


def login():
    if not os.path.isdir("secrets"):

        message = f"{begin}       Welcome to your FaceBooker{end}"

        typer.secho(message, fg="green")

        os.mkdir("secrets")

        message2 = "       be sure to run changeusername and changepassword"

        typer.secho(f"{begin}message{end}", fg="green")

    if not os.path.isfile("secrets/username"):
        message = "    no username found, run command changeusername to add"

        typer.secho(f"{begin}{message}{end}", fg="red")

        return

    if not os.path.isfile("secrets/password"):
        message = "    no password found, run command changepassword to add"

        typer.secho(f"{begin}{message}{end}", fg="red")

        return

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    driver.get(constants["base_url"])

    sleep(2)

    with open("secrets/username") as file:
        username = file.read()

    with open("secrets/password") as file:
        password = file.read()

    if driver.title == constants["login_title"]:
        username_input = h.find_this_x(driver, xpaths["username_input"])
        password_input = h.find_this_x(driver, xpaths["password_input"])
        login_button = h.find_this_x(driver, xpaths["login_button"])

        username_input.send_keys(username)
        sleep(1)
        password_input.send_keys(password)
        sleep(1)
        login_button.click()
        sleep(1)

    return driver


@app.command()
def getnumfriends(gui: bool = False):

    if not gui:

        chrome_options.add_argument("--headless")

    driver = login()

    sleep(1)

    driver.get(f"{constants['base_url']}/me/")

    sleep(1)

    my_profile_link = driver.current_url

    if not os.path.isfile("secrets/myprofilelink"):

        with open("secrets/myprofilelink", "w") as file:

            file.write(my_profile_link)

    driver.get(f"{my_profile_link}friends")

    num_of_friends = h.find_this_xtext(driver, xpaths["num_of_friends"])

    num_friends = int(num_of_friends.strip())

    with open("secrets/currentfriendcount", "w") as file:

        file.write(str(num_friends))

    current_date = datetime.datetime.now()

    formatted_date = f"{current_date.year}-{current_date.month}-{current_date.day}"

    friend_history = f"{formatted_date} {str(num_of_friends)}\n"

    with open("secrets/runningfriendcount", "a") as file:

        file.write(friend_history)

    driver.get(constants["base_url"])

    driver.quit()

    message = f"recorded number of friends ({num_of_friends}) to current and history"

    typer.secho(message, fg="green")

    driver.quit()


@app.command()
def getfriendslist(gui: bool = False):

    if not gui:

        chrome_options.add_argument("--headless")

    driver = login()

    driver.get(f"{constants['base_url']}/me/")

    sleep(1)

    my_profile_link = driver.current_url

    if not os.path.isfile("secrets/myprofilelink"):

        with open("secrets/myprofilelink", "w") as file:

            file.write(my_profile_link)

    driver.get(f"{my_profile_link}friends")

    h.scroll_to_bottom(driver)

    sleep(10)

    friend_elements = h.find_these_x(driver, xpaths["friend_links"])

    last_friend_elements = []

    while not len(friend_elements) == len(last_friend_elements):

        last_friend_elements = friend_elements

        h.scroll_to_bottom(driver)

        sleep(10)

        friend_elements = h.find_these_x(driver, xpaths["friend_links"])

        m1 = f"{begin}         found {len(friend_elements)} friend links so far{end}"

        m2 = f'{begin}         last list last element = {last_friend_elements[len(last_friend_elements) - 1].get_attribute("href")}{end}'

        m3 = f"{begin}         current list last element = {friend_elements[len(friend_elements) - 1].get_attribute('href')}{end}"

        typer.secho(m1, fg="green")

        typer.secho(m2, fg="red")

        typer.secho(m3, fg="blue")

    if not os.path.isdir("secrets/friends"):

        os.mkdir("secrets/friends")

    for friend_element in friend_elements:

        link = friend_element.get_attribute("href")

        friend_id = h.get_fb_id(link)

        typer.secho(f"{begin}friend id: {friend_id}{end}")

        typer.secho(f"{begin}friend link: {link}{end}")

        compare_this = f'{constants["base_url"]}/{friend_id}/friends_mutual'

        typer.secho(f"is {compare_this} == {link}? {compare_this == link}")

        if compare_this == link:

            friend_path = f"secrets/friends/{friend_id}"

            if not os.path.isdir(friend_path):

                os.mkdir(friend_path)

    confirm_complete = f'{begin}"        COMPLETED GETTING FRIENDS LIST"{end}'

    typer.secho(confirm_complete, fg="green")

    driver.quit()


@app.command()
def countfriends(names: bool = False):

    if names:

        name_count = 0

        for friend_id in friend_ids:

            if os.path.isfile(f"secrets/friends/{friend_id}/name"):

                name_count += 1

        message = f"found {name_count} names for {len(friend_ids)} friends"

        typer.secho(message, fg="green")

        return

    friend_ids = os.listdir("secrets/friends")

    typer.secho(f"found {len(friend_ids)} friend ids", fg="green")


@app.command()
def getfriendsnames(gui: bool = False):

    if not gui:

        chrome_options.add_argument("--headless")

    driver = login()

    friend_ids = os.listdir("secrets/friends")

    for friend_id in friend_ids:

        if not os.path.isfile(f"secrets/friends/{friend_id}/name"):

            driver.get(f"{constants['base_url']}/{friend_id}")

            sleep(2)

            headers = driver.find_elements(By.XPATH, "//h1")

            if headers:

                friend_name = headers[len(headers) - 1].text

                typer.secho(f"{begin}    friend name is {friend_name}{end}", fg="green")

                name_file = f"secrets/friends/{friend_id}/name"

                if not os.path.isfile(name_file):

                    with open(name_file, "w") as file:

                        file.write(friend_name)

    confirm_complete = f'{begin}"        COMPLETED GETTING FRIENDS NAMES"{end}'

    typer.secho(confirm_complete, fg="green")

    driver.quit()


@app.command()
def post(gui: bool = False):

    if not gui:
        chrome_options.add_argument("--headless")

    driver = login()

    onyourmind = h.find_this_x(driver, xpaths["onyourmind"])

    onyourmind.click()

    sleep(2)

    inputbox = driver.find_element(By.XPATH, xpaths["input_box"])

    message = f"{begin}    What message would you like to post?{end}"

    post_message = typer.prompt(message)

    inputbox.send_keys(post_message)

    sleep(2)

    post_button = driver.find_element(By.XPATH, xpaths["post_button"])

    post_button.click()

    driver.quit()


if __name__ == "__main__":

    app()
