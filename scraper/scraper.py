from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd
from github_scraper import scrape_github


def scrape_everything():
    scrape_beecrowd()
    scrape_github()
    scrape_codeforces()
