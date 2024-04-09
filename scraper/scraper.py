from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd


def scrape_everything():
    scrape_beecrowd()
    scrape_codeforces()
