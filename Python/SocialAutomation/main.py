import re

from time import sleep

import pymongo

from secrets import my_vars, my_selectors, user1, user2

from db import update_data

import bot

uri = my_vars["uri"]

cluster = pymongo.MongoClient(uri)

users = cluster["users"]

liked_pictures = user1["liked_pictures"]

males_only = { liked_pictures: False, "active": True, "fatalErr": False, "isMale": True, }

bot.login(user1)

# wyoming

# these_states = ["Massachusetts","Wisconsin", "West Virginia", "Virginia", "Vermont"]

these_states = ["Missouri", "Iowa", "Tennessee"]

for state in these_states:

    bot.like_pictures(state, users, user1, males_only)

