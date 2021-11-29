#!/bin/python3
"""social media automation tool"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def enter_text(selectme, txt):
    el = driver.find_element(By.XPATH, selectme)
    el.send_keys(txt)


def clickit(selectme):
    el = driver.find_element(By.XPATH, selectme)
    if not el:
        txt = 'cannot find element'
        print(txt)
        return False
    el.click()
    return True


def gets_page(url):
    print("getting page")
    driver.get(url)
    return driver.title


def finds_this(selectme, isMany: bool):
    if not isMany:
        print("finding element")
        el = driver.find_element(By.XPATH, selectme)
        if not el:
            txt = 'nothing found'
            print(txt)
            return False
        return el

    if isMany:
        print("finding list of elements")
        els = driver.find_elements(By.XPATH, selectme)
        if not els:
            txts = ['nothing', 'found']
            print(txts)
            return False
        return els


def gets_text(selectme, isMany: bool):
    if not isMany:
        el = driver.find_element(By.XPATH, selectme)
        if not el:
            txt = 'nothing found'
            return txt
        txt = el.text
        return txt

    if isMany:
        els = driver.find_elements(By.XPATH, selectme)
        if not els:
            txts = ['nothing', 'found']
            return txts
        txts = [el.text for el in els]
        return txts


def gets_link(selectme, isMany: bool):
    if not isMany:
        el = driver.find_element(By.XPATH, selectme)
        link = el.get_attribute("href")
        return link

    if isMany:
        els = driver.find_elements(By.XPATH, selectme)
        links = []
        for el in els:
            link = el.get_attribute("href")
            links.append(link)
        return links
