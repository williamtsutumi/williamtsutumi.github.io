import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import pathlib
import os

from definitions import TMP_JSON, CSES_JSON


def scrape_cses():
    driver = webdriver.Chrome()
    driver.maximize_window()

    authenticate(driver)

    driver.get("https://cses.fi/problemset/")
    time.sleep(2)

    tasklists = driver.find_elements(By.CLASS_NAME, "task-list")
    tasklists.pop(0)
    urls = []
    for tlist in tasklists:
        tasks = tlist.find_elements(By.TAG_NAME, "li")
        for task in tasks:
            try:
                task.find_element(By.CLASS_NAME, "full")  # if didn't find throws exception
                url = task.find_element(By.TAG_NAME, 'a').get_attribute('href')
                urls.append(url)
            except:
                pass
            try:
                task.find_element(By.CLASS_NAME, "zero")  # if didn't find throws exception
                url = task.find_element(By.TAG_NAME, 'a').get_attribute('href')
                urls.append(url)
            except:
                pass

    output = []
    for url in urls:
        driver.get(url)
        time.sleep(1)

        anchors = driver.find_elements(By.TAG_NAME, 'a')
        for anchor in anchors:
            try:
                url = anchor.get_attribute('href').split('/')
                if not ('result' in url):
                    continue

                output.append({
                    "problem": driver.title.replace("CSES - ", ""),
                    "date": format_date(anchor.text.split(' ')[0]),
                })
            except:
                pass

    if output:
        with open(TMP_JSON, "w") as outfile:
            json.dump(output, outfile)

        size_saved = pathlib.Path(CSES_JSON).stat().st_size
        size_current = pathlib.Path(TMP_JSON).stat().st_size
        if size_current > size_saved:
            with open(CSES_JSON, "w") as outfile:
                json.dump(output, outfile)

        os.remove(TMP_JSON)

    driver.quit()


def format_date(text):
    date = datetime.strptime(text, '%Y-%m-%d')
    return date.strftime('%d/%m/%y')


def authenticate(driver):
    driver.get("https://cses.fi/login")
    print("CSES authentication")
    user = driver.find_element(By.ID, 'nick')
    username = input("Username: ")
    user.send_keys(username)
    pwd = driver.find_element(By.NAME, 'pass')
    password = input("Password: ")
    pwd.send_keys(password)

    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()
    time.sleep(2)
