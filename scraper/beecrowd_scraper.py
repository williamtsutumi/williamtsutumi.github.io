import time
import json
from configs import BeecrowdConfigs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import pathlib
import os


def scrape_beecrowd():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    conf = BeecrowdConfigs()
    driver.get(conf.bc_url)
    time.sleep(2)

    num_pages = int(driver.find_element(By.ID, "table-info").text.split()[-1])
    output = []
    for i in range(1, num_pages+1):
        driver.get(conf.get_page(i))
        time.sleep(1)
        rows_data = extract_table_info(driver)
        for row in rows_data:
            output.append(row)

    if output:
        with open("scraper/output/tmp.json", "w") as outfile:
            json.dump(output, outfile)

        size_saved = pathlib.Path('scraper/output/beecrowd.json').stat().st_size
        size_current = pathlib.Path('scraper/output/tmp.json').stat().st_size
        if size_current > size_saved:
            with open("scraper/output/beecrowd.json", "w") as outfile:
                json.dump(output, outfile)

        os.remove("scraper/output/tmp.json")

    driver.quit()


def extract_table_info(driver):
    submissions = []
    lines = driver.find_elements(By.XPATH, '//table/tbody/tr')
    for i, line in enumerate(lines):
        table_datas = line.find_elements(By.TAG_NAME, 'td')
        try:
            sub = {
                'id': table_datas[0].text,
                'date': format_date(table_datas[-1].text.split()[0][:-1]),
                'problem': table_datas[1].text,
                'url': table_datas[1].find_element(By.TAG_NAME, 'a').get_attribute('href'),
            }
            print("sub: " + str(sub))
            submissions.append(sub)
        except:
            print('exception parsing table row ' + str(i))

    return submissions


def format_date(text):
    date = datetime.strptime(text, '%m/%d/%y')
    return date.strftime('%d/%m/%y')
