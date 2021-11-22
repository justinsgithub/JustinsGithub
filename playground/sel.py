#!/bin/python3
# -*- encoding: utf-8 -*-
import typer
from selenium import webdriver
from time import sleep
import os
from re import sub
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from secrets import social1, my_selectors

s1url = social1["url"]
s1username = social1["username"]
s1password = social1["password"]
s1username_form = my_selectors["username_form"]
s1password_form = my_selectors["password_form"]
s1login_button = my_selectors["login_button"]

promp = "+=($)-->> "
 

driver = webdriver.Chrome()    
tim_tech = "https://techwithtim.net/"

def sel_start(url):
    driver.maximize_window()
    driver.get(url)
    print(driver.title)

def get_page():
    page = typer.prompt("which page would you like me to get?" + promp)   
    driver.get(page)

def select_element(select_this):
    target_element = driver.find_element(By.XPATH, select_this)
    if not target_element:
        typer.echo("No such element")
        return ''
    
    return target_element

def get_text(select_this):
    return select_this.text

def get_href(select_this):
    return select_this.get_attribute("href")

def get_texts(select_this):
    content = [this_element.text for this_element in select_this]
    return content

def get_hrefs(select_this):
    all_links = [this_element.get_attribute("href") for this_element in select_this]
    return all_links

def select_elements(select_this):
    target_elements = driver.find_elements(By.XPATH, select_this)
    if not target_elements:
        typer.echo("No such elements")
        return ['']
    
    return target_elements

def clickit(select_this):
    select_this.click()

def fillin(select_this, characters):
    select_this.send_keys(characters)

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
        if next_command.lower() == "q":
            driver.quit()
            return

        if next_command.lower() == "g":
            get_page(driver)
        
        if next_command.lower() == "pt":
            print(driver.title)

        if next_command.lower() == "ps":
            print(driver.page_source)
            
        if next_command.lower() == "se":
            el = typer.prompt(promp + 'which element?')
            select_element(el)

        if next_command.lower() == "sae":
            select_elements()

run_program()
