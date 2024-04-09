from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd


def scrape_everything():
    scrape_beecrowd()
    scrape_codeforces()
