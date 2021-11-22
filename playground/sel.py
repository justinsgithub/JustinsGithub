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

promp = "+=($)-->> "
 

driver = webdriver.Chrome()    
tim_tech = 'https://techwithtim.net/'
h = 'http://'
hs = 'https://'

def sel_start(url):
    driver.maximize_window()
    driver.get(url)
    print(driver.title)

def get_page():
    page = typer.prompt("which page would you like me to get?" + promp)   
    options = typer.prompt("type Y to confirm, type U for insecure HTTP" + promp)
    get_page = hs + page 
    
    if options.lower() == 'u':
        get_page = h + page

    driver.get(get_page)

def find_elements():
    pass



def run_program():
    options = """
        G to get page 
        
        PS to print page source

        PT to print page title


        Q to quit
    """
    continues = True
    sel_start(tim_tech)
    
    while continues:
        next_command = typer.prompt(options + promp)
        if next_command.lower() == 'q':
            driver.quit()
            return

        if next_command.lower() == 'g':
            get_page(driver)
        
        if next_command.lower() == 'pt':
            print(driver.title)

        if next_command.lower() == 'ps':
            print(driver.page_source)
            
        if next_command.lower() == 'fe':
            find_elements()

run_program()

