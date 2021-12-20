import re

from time import sleep

import pymongo

from secrets import my_vars, my_selectors, user1, user2

import interactions as i

uri = my_vars["uri"]

cluster = pymongo.MongoClient(uri)

users = cluster["users"]

i.login(user2)
