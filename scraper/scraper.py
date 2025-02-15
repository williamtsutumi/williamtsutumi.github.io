from codeforces_scraper import scrape_codeforces
from beecrowd_scraper import scrape_beecrowd
from github_scraper import scrape_github
from cses_scraper import scrape_cses

scrapers = [scrape_beecrowd, scrape_github, scrape_cses, scrape_codeforces]

def scrape_everything():
    for scraper in scrapers:
        try:
            scraper()
        except Exception as e:
            print(e)
