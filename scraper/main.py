from scraper import scrape_everything
import json


def save_githubpages_json():
    all_data = {}
    with open('codeforces.json') as json_file:
        subs = json.load(json_file)
        for s in subs:
            date = s['date']
            if date in all_data:
                all_data[date] += 1
            else:
                all_data[date] = 1

    with open('gh_pages.json', 'w') as data:
        json.dump(all_data, data)


def main():
    # scrape_everything()
    save_githubpages_json()


if __name__ == '__main__':
    main()
