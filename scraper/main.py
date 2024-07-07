from scraper import scrape_everything
import json
from datetime import datetime


def add_json_wrapper(output, filename, abbreviation, operation):
    with open('scraper/output/' + filename) as json_file:
        activities = json.load(json_file)
        for activity in activities:
            date = activity["date"]
            if not (date in output) or not (abbreviation in output[date]):
                output[date] = dict({abbreviation: 0})
            output[date][abbreviation] = operation(output[date][abbreviation], activity)


def save_githubpages_json():
    all_data = {}
    add_json_wrapper(all_data, 'github.json', 'gh', lambda output, activity: activity["count"])
    add_json_wrapper(all_data, 'beecrowd.json', 'bc', lambda output, activity: output + 1)
    add_json_wrapper(all_data, 'codeforces.json', 'cf', lambda output, activity: output + 1)
    add_json_wrapper(all_data, 'cses.json', 'cses', lambda output, activity: output + 1)

    with open('scraper/output/gh_pages.json', 'w') as data:
        json.dump(all_data, data)


def update_website_json():
    with open('script.js', 'r') as js:
        data = js.read().splitlines(True)
    with open('script.js', 'w') as js:
        with open('scraper/output/gh_pages.json') as output:
            json_data = output.readline()
            js.write('const json = ' + json_data +
                     '\nconst last_update = "' + datetime.today().strftime('%d/%m/%y') + '";\n')

        js.writelines(data[2:])


def set_next_update():
    with open('automation/update.sh', 'r+') as shell:
        data = shell.read().splitlines(True)
        month = datetime.now().month
        month_str = month + 1 if month < 12 else 1
        data[1] = 'month="' + str(month_str) + '"\n'
    with open('automation/update.sh', 'w') as shell:
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
