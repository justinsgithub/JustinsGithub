#!/bin/python3
"""social media automation tool"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Bot():
    """ init should contain any information that might change from bot to bot, such as login information, website url, and element selectors"""
    def __init__(self, bot):
        print("initializing new Bot")

        self.bot = bot
    
    def find_el(self, x):
        el = self.bot.find_element(By.XPATH, x)

    def start(self, x):
        print("starting driver, going to " + x)
        (self.bot.get(x)
