#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import os
import pyautogui
from PIL import Image, ImageDraw, ImageColor


def pageClick(x, y):
    sleep(0.25)
    pyautogui.click(x, y)
def pageClickRight(x, y):
    sleep(0.25)
    pyautogui.rightClick(x,y)
def scrollUp(x):
    sleep(0.25)
    pyautogui.scroll(x)
def scrollDown(x):
    sleep(0.25)
    pyautogui.scroll(x)
def keyPress(key):
    sleep(0.25)
    pyautogui.press(key)
def hotKey(key1, key2):
    sleep(0.25)
    pyautogui.hotkey(key1, key2)
def enterText(text):
    sleep(0.25)
    pyautogui.write(text, interval=0.25)


def initiate():
    sleep(1)
    hotKey('win', 'down')

def findPicLink():
    hotKey('ctrl', 'f')
    enterText('pic')
    keyPress('enter')
    keyPress('esc')
    hotKey('shift', 'tab')
    hotKey('shift', 'tab')
    hotKey('ctrl', 'enter')



def openTab():
    sleep(1)
    hotKey('ctrl', 'enter')
    sleep(3)
    hotKey('ctrl', 'tab')

def openUserPages():
    for x in range(20):
        keyPress('enter')
        keyPress('esc')
        keyPress('tab')
        openTab()
        hotKey('ctrl', 'f')

def closeTabs(amount):
    for x in range(amount):
        #hotKey('ctrl', 'w')
        pageClick(470,75)
    pageClick(832,208)



def loveButton():
    sleep(1)
    pageClick(317,530)

def pageDown():
    sleep(1)
    keyPress('pagedown')

def goBack():
    hotKey('alt', 'left')

def lovePicture():
    sleep(2)
    hotKey('ctrl', 'f')
    enterText('options')
    keyPress('enter')
    keyPress('esc')
    loveButton()
    hotKey('ctrl', 'w')

def findPictures():
    hotKey('ctrl', 'tab')
    hotKey('ctrl', 'f')
    enterText('Newest')
    keyPress('enter')
    keyPress('esc')
    keyPress('tab')
    hotKey('ctrl', 'enter')
    keyPress('tab')
    hotKey('ctrl', 'enter')
    keyPress('tab')
    hotKey('ctrl', 'enter')
    hotKey('ctrl', 'w')
    lovePicture()
    #hotKey('ctrl', 'enter')
    #keyPress('tab')
    #hotKey('ctrl', 'enter')
    #keyPress('tab')
    #hotKey('ctrl', 'enter')


def like2ndPic():
    hotKey('ctrl', 'tab')
    lovePicture()

def like1stPic():
    hotKey('ctrl', 'tab')
    lovePicture()

def like3rdPic():
    hotKey('ctrl', 'tab')
    lovePicture()


def nextPage():
    sleep(1)
    hotKey('ctrl', 'f')
    enterText('Next')
    keyPress('enter')
    keyPress('esc')
    keyPress('enter')

def likeUserPics():
    findPicLink()
    openTab()
    findPictures()
    like1stPic()
    like2ndPic()
    like3rdPic()


def likeNextUsersPics():
    closeTabs(4)
    likeUserPics()

#initiate()
#likeUserPics()
#likeNextUsersPics()


sleep(1)
hotKey('win', 'down')

for x in range(200):
    sleep(1)
    nextPage()
    sleep(2)
    for x in range(20):
        findPicLink()
    hotKey('ctrl', 'tab')
    for x in range(20):
        sleep(1)
        pageClick(1077,322)
        sleep(1)
        hotKey('ctrl', 'w')
