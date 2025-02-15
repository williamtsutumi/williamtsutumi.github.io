from scraper import scrape_everything
import json
import os
from datetime import datetime

from definitions import GH_PAGES_JSON, GH_JSON, BC_JSON, CF_JSON, CSES_JSON, SCRIPT_PATH, UPDATE_PATH


def add_json_wrapper(output, filepath, abbreviation, operation):
    with open(filepath) as json_file:
        activities = json.load(json_file)
        for activity in activities:
            date = activity["date"]
            if not (date in output) or not (abbreviation in output[date]):
                output[date] = dict({abbreviation: 0})
            output[date][abbreviation] = operation(output[date][abbreviation], activity)


def save_githubpages_json():
    all_data = {}
    add_json_wrapper(all_data, GH_JSON, 'gh', lambda output, activity: activity["count"])
    add_json_wrapper(all_data, BC_JSON, 'bc', lambda output, activity: output + 1)
    add_json_wrapper(all_data, CF_JSON, 'cf', lambda output, activity: output + 1)
    add_json_wrapper(all_data, CSES_JSON, 'cses', lambda output, activity: output + 1)

    with open(GH_PAGES_JSON, 'w') as data:
        json.dump(all_data, data)


def update_website_json():
    with open(SCRIPT_PATH, 'r') as js:
        data = js.read().splitlines(True)
    with open(SCRIPT_PATH, 'w') as js:
        with open(GH_PAGES_JSON) as output:
            json_data = output.readline()
            js.write('const json = ' + json_data +
                     '\nconst last_update = "' + datetime.today().strftime('%d/%m/%y') + '";\n')

        js.writelines(data[2:])


def set_next_update():
    with open(UPDATE_PATH, 'r+') as shell:
        data = shell.read().splitlines(True)
        month = datetime.now().month
        month_str = month + 1 if month < 12 else 1
        data[1] = 'month="' + str(month_str) + '"\n'
    with open(UPDATE_PATH, 'w') as shell:
        shell.writelines(data)


def main():
    print('starting scraping')
    scrape_everything()
    save_githubpages_json()
    update_website_json()
    set_next_update()
    print('updated successfully')


if __name__ == '__main__':
    while True:
        ans = input("update github pages now? (Y/N) ")
        if ans.upper() == "Y":
            main()
            break
        elif ans.upper() == "N":
            break
        else:
            continue
