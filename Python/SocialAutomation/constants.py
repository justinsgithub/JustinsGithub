#!/bin/python3

base_url = "https://fetlife.com"

my_vars = {
    "uri":
    "mongodb+srv://justinaawd:YhsGDjkfojaq0fC5@online-presence-cluster.rdnj4.mongodb.net/site1?retryWrites=true&w=majority",
    
    "home_page": base_url + "/home",
    
    "profile_url": base_url + "/users/",
    
    "us_places": "https://fetlife.com/p/united-states",
    

    "login_title": "Login | FetLife",

    "username1": "lemonjewell@yahoo.com",
    
        
    "password1": "Ilovelemon93",
    
    "username2": "lovedaddyj",
    
    "password2": "Hockey1343!",
    
    "users": "kinksters",

    "within": "related",
    
    "current_user_1":"lLikedPictures",
    
    "current_user_2": "jLikedPictures",
}

my_selectors = {
    
    "username_in":
    ("/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div["
     "1]/div/div/input"),
    
    "password_in":
    ("/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[1]/div["
     "2]/div/div/input"),
    
    "login_button":
    "/html/body/div[3]/div/div[3]/div/main/div/div[1]/form/div[2]/button",
    
    "view_pictures_selector":
    ("//main//div//a[@class='link gray hover-gray-300 dot-separated'][1]"),
    
    "picture_link_selector":
    ("//a[@class='aspect-ratio--1x1 relative db bg-animate "
     "no-underline "
     "overflow-hidden br1 tap-highlight-transparent bg-gray-900 "
     "hover-bg-gray-950']"),
    
    "follow_button_selector": '//button[@name="button"][@data-color="secondary"]',
    
    "following_button_selector": '//button[@name="button"][@data-color="lined"]',
    
    "love_button_selector": '//a[@title="Love"][text()="Love"]',
    
    "comment_input_selector": "//div[@id='new_comment']//form/div/div/textarea",
    
    "comment_button_selector": "//div[@id='new_comment']//form/div/div/textarea//button[1]",

    "states_selector" : '//*[@id="ptr-main-element"]//main/div[@class="mw8 nl2 nr2"]//a',
    
    "cities_selector"  : '//*[@id="ptr-main-element"]//main//div[@class="mw8 nl2 nr2"]//a',

    "num_users_selector" : '//*[@id="ptr-main-element"]/header/div/nav/div/a[2]//span',
    
    "num_cities_selector" : '//*[@id="ptr-main-element"]/header/div/nav/div/a[5]//span',
    
    "city_name_selector" : '//h1[@class="mv0 f4 f25-ns fw7 lh-copy tl secondary breakword"]',
    
}

