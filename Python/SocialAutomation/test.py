import re
from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from constants import my_vars, my_selectors, base_url
from db import update_data
import helpers

import pymongo

uri = my_vars["uri"]
cluster = pymongo.MongoClient(uri)
users = cluster["users"]

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
"""