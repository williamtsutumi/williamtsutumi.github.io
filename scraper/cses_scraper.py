import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import pathlib
import os


def scrape_cses():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
        with open("scraper/output/tmp.json", "w") as outfile:
            json.dump(output, outfile)

        size_saved = pathlib.Path('scraper/output/cses.json').stat().st_size
        size_current = pathlib.Path('scraper/output/tmp.json').stat().st_size
        if size_current > size_saved:
            with open("scraper/output/cses.json", "w") as outfile:
                json.dump(output, outfile)

        os.remove("scraper/output/tmp.json")

    driver.quit()


def format_date(text):
    date = datetime.strptime(text, '%Y-%m-%d')
    return date.strftime('%d/%m/%y')


def authenticate(driver):
    driver.get("https://cses.fi/login")
    user = driver.find_element(By.ID, 'nick')
    user.send_keys('williamkt')
    pwd = driver.find_element(By.NAME, 'pass')
    pwd.send_keys('WaGJiyHG00C')

    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()
    time.sleep(2)
