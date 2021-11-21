#!/bin/python3
# -*- encoding: utf-8 -*-
import typer
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

promp = """
    
            () -->>  
    
    """
 

driver = webdriver.Chrome()    
tim_tech = 'https://techwithtim.net/'
h = 'http://'
hs = 'https://'

def sel_start(bot, url):
    bot.maximize_window()
    bot.get(url)
    print(bot.title)

def get_page(bot):
    page = typer.prompt("which page would you like me to get?" + promp)   
    options = typer.prompt("type Y to confirm, type U for insecure HTTP" + promp)
    get_page = hs + page 
    
    if options.lower() == 'u':
        get_page = h + page

    bot.get(get_page)

def run_program(bot):
    options = """
        G to get page 
        
        PS to print page source

        PT to print page title


        Q to quit
    """
    continues = True
    sel_start(bot, tim_tech)
    
    while continues:
        next_command = typer.prompt(options + promp)
        if next_command.lower() == 'q':
            bot.quit()
            return

        if next_command.lower() == 'g':
            get_page(bot)
        
        if next_command.lower() == 'pt':
            print(bot.title)

        if next_command.lower() == 'ps':
            print(bot.page_source)
            

run_program(driver)