#!/bin/env/python3
import re
import os

with open('us_places_all.txt') as file:
    for place in file.readlines():
        place = place.strip()
        os.mkdir(place)
