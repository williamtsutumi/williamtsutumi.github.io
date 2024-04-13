from scraper import scrape_everything
import json

empty_index = {"cf": 0, "gh": 0}


def add_cf_json(output):
    with open('scraper/output/codeforces.json') as json_file:
        activities = json.load(json_file)
        for activity in activities:
            date = activity["date"]
            if not (date in output):
                output[date] = dict(empty_index)
            output[date]["cf"] += 1


def add_gh_json(output):
    with open('scraper/output/github.json') as json_file:
        activities = json.load(json_file)
        for activity in activities:
            date = activity["date"]
            if not (date in output):
                output[date] = dict(empty_index)
            output[date]["gh"] = activity["count"]


def save_githubpages_json():
    all_data = {}
    add_cf_json(all_data)
    add_gh_json(all_data)

    with open('scraper/output/gh_pages.json', 'w') as data:
        json.dump(all_data, data)


def main():
    # scrape_everything()
    save_githubpages_json()


if __name__ == '__main__':
    main()
