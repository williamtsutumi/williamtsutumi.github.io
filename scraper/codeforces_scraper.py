import time
import json
from configs import CodeforcesConfigs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime


def scrape_codeforces():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    conf = CodeforcesConfigs()
    driver.get(conf.cf_url)
    time.sleep(2)

    show_unoficial_checkbox = driver.find_element(By.ID, 'showUnofficial')
    if not show_unoficial_checkbox.is_selected():
        show_unoficial_checkbox.click()

    num_pages = find_num_pages(driver, conf)
    output = []
    for i in range(1, num_pages+1):
        driver.get(conf.get_page(i))
        time.sleep(1)

        rows_data = extract_table_info(driver, conf)
        for row in rows_data:
            output.append(row)

    if output:
        with open("scraper/output/codeforces.json", "w") as outfile:
            json.dump(output, outfile)

    driver.quit()


def find_num_pages(driver, conf):
    pagination = driver.find_element(By.CLASS_NAME, conf.pagination_class_name)
    last = pagination.find_elements(By.XPATH, conf.page_numbers_xpath)[-1].text
    print('number of pages found: ' + last)
    return int(last)


def extract_table_info(driver, conf):
    submissions = []
    lines = driver.find_elements(By.XPATH, conf.table_row_xpath)
    lines.pop(0)
    lines.pop(-1)
    for i, line in enumerate(lines):
        table_datas = line.find_elements(By.TAG_NAME, 'td')
        try:
            sub = {
                'id': table_datas[0].text,
                'date': format_date(table_datas[1].text),
                'problem': table_datas[3].text,
                'url': table_datas[3].find_element(By.TAG_NAME, 'a').get_attribute('href'),
                'verdict': table_datas[5].text,
            }
            submissions.append(sub)
        except:
            print('exception parsing table row ' + str(i))

    return submissions


def format_date(text):
    text = text.split(' ')[0]
    date = datetime.strptime(text, '%b/%d/%Y')
    return date.strftime('%d/%m/%y')
