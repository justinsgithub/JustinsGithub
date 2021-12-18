import re

from time import sleep

from selenium import webdriver

from selenium.common import exceptions

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from secrets import my_vars, my_selectors, base_url

from db import update_data

import helpers

import pymongo

uri = my_vars["uri"]

cluster = pymongo.MongoClient(uri)

united_states_db = cluster["unitedStates"]

"""

def get_states(these_users):

    these_states = these_users.list_collection_names()

    print(these_states)

    completed_states = [

        "Connecticut", "Colorado", "Michigan", "New York", "Utah", "Montana",

        "Texas", "North Dakota", "Ohio"

    ]

    states_to_get = 0

    for state in these_states:

        if not state in completed_states:

            print(state)

            states_to_get += 1

            print(states_to_get)

    get_these_states = [x for x in these_states if not x in completed_states]

    print(get_these_states, len(get_these_states))

    return get_these_states

get_states(users)


def get_completed_city_links(state_name):

    this_state = united_states_db[state_name].find_one({"name": state_name})

    completed_cities = this_state["completedCities"]

    return completed_cities

def get_cities_user_pages(state_name):

    

#    states = united_states_db.list_collection_names()

#    state_1 = states[0]

    

    print(f'getting cities data for {state_name}')

    this_state = united_states_db[state_name].find_one({"name": state_name})

    print(this_state)

    city_links = this_state["cityLinks"]

    completed_city_links = get_completed_city_links(state_name)

    print(f"{len(completed_city_links)} completed city links")

    

    

    user_links = [f'{link}/{my_vars["users"]}' for link in city_links]

    

    user_pages = [link for link in user_links if not link in completed_city_links]

    

    #for link in user_links:

    #    print(link)

        

    return user_pages

get_cities_user_pages("California")

"""
