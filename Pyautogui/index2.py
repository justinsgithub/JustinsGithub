#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import os
import pyautogui
from PIL import Image, ImageDraw, ImageColor
from pymongo import MongoClient


379,242
690,240
475,324
712,325
453,384
675,418
406,470
705,492
404,550
686,577
352,638
688,643
273,718
702,715

def pageClick(x, y):
    pyautogui.click(x, y)

def scrollUp(x):
    sleep(3)
    pyautogui.scroll(x)

def scrollDown(x):
    sleep(3)
    pyautogui.scroll(x)

def printCoordinates():    
    sleep(3)
    print(pyautogui.position())

scrollDown(-30)
pageClick(628,581)


#18 tabs
#for coordinate in table.find({},{"_id":0, "x":1, "y":1}):
#    pyautogui.click(x, y)
