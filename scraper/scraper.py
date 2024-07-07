from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd
from github_scraper import scrape_github
from cses_scraper import scrape_cses


def scrape_everything():
    scrape_beecrowd()
    scrape_github()
    scrape_codeforces()
    scrape_cses()
