import re

from time import sleep

import pymongo

from secrets import my_vars, my_selectors, user1, user2

import interactions as i

uri = my_vars["uri"]

cluster = pymongo.MongoClient(uri)

users = cluster["users"]

i.login(user2)

# wyoming

# these_states = ["Missouri", "Massachusetts","Wisconsin", "West Virginia", "Virginia", "Vermont"]

these_states = [
    "Washington", "New York", "New Jersey", "Tennessee", "Wisconsin"
]

for state in these_states:

    i.like_pictures(state, users, user2)
