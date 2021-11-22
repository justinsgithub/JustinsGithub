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

app = typer.Typer()
promp = """
    
            +=($)-->>  
    
    """
 

driver = webdriver.Chrome()    
tim_tech = 'https://techwithtim.net/'
h = 'http://'
hs = 'https://'

@app.command()
def start(url):
    driver.maximize_window()
    driver.get(url)
    print(driver.title)

@app.command()
def get_page(unsecure: bool = False):
    page = typer.prompt("which page would you like me to get?" + promp)   
    options = typer.prompt("type Y to confirm, type U for insecure HTTP" + promp)
    get_page = hs + page 
    
    if options.lower() == 'u':
        get_page = h + page

    driver.get(get_page)

@app.command()
def main():
    options = """
        G to get page 
        
        PS to print page source

        PT to print page title


        Q to quit
    """
    continues = True
    start(driver, tim_tech)
    
    while continues:
        next_command = typer.prompt(options + promp)
        if next_command.lower() == 'q':
            driver.quit()
            return

        if next_command.lower() == 'g':
            get_page()
        
        if next_command.lower() == 'pt':
            typer.echo(driver.title)

        if next_command.lower() == 'ps':
            typer.echo(driver.page_source)


if __name__ == "__main__":
    app()