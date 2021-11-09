#!/usr/bin/python3

import os

print(os.listdir())

current_path = os.getcwd()
print(current_path)

current_directory_name = os.path.basename(current_path)
print(current_directory_name)

db = '.data'
if not os.path.exists(db):
    os.mkdir(db)

