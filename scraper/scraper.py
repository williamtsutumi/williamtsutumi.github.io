from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd
from github_scraper import scrape_github


def scrape_everything():
    try_wrapper('beecrowd', scrape_beecrowd())
    try_wrapper('github', scrape_github())
    try_wrapper('codeforces', scrape_codeforces())


def try_wrapper(website, func):
    try:
        func()
    except:
        print(website + ' scraper stopped working')
