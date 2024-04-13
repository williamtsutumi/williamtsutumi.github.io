import time
import json
from configs import GithubConfigs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from time import strptime


def scrape_github():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    conf = GithubConfigs()
    driver.get(conf.gh_url)
    time.sleep(5)

    year_list = driver.find_elements(By.TAG_NAME, 'ul')[-4]
    iters = len(year_list.find_elements(By.TAG_NAME, 'li'))

    output = []
    for i in range(iters):
        year_list = driver.find_elements(By.TAG_NAME, 'ul')[-4]
        curr_year = year_list.find_elements(By.TAG_NAME, 'li')[i]
        year_str = curr_year.find_element(By.TAG_NAME, 'a').text
        curr_year.click()
        time.sleep(5)

        tooltips = driver.find_elements(By.TAG_NAME, 'tool-tip')[conf.first_tooltip:]
        for tooltip in tooltips:
            if conf.no_contribution_text in tooltip.text:
                continue
            output.append(parse_text(tooltip.text, year_str))

    with open("scraper/output/github.json", "w") as outfile:
        json.dump(output, outfile)

    driver.quit()


def parse_text(txt, year):
    splited = txt.split(' ')
    contributions = int(splited[0])
    month = splited[-2][:3]

    month_number = str(strptime(month, '%b').tm_mon)
    if len(month_number) == 1:
        month_number = '0' + month_number
    day = splited[-1][:2]
    if not day.isdigit():
        day = day.replace(day[1], "")
        day = '0' + day
    date = day + '/' + month_number + '/' + year[2:]
    return {'count': contributions, 'date': date}


def format_date(text):
    text = text.split(' ')[0]
    date = datetime.strptime(text, '%b/%d/%Y')
    return date.strftime('%d/%m/%y')
