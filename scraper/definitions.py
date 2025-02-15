import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GH_PAGES_JSON = os.path.join(ROOT_DIR,'output', 'gh_pages.json')
GH_JSON = os.path.join(ROOT_DIR, 'output', 'github.json')
CF_JSON = os.path.join(ROOT_DIR, 'output', 'codeforces.json')
CSES_JSON = os.path.join(ROOT_DIR, 'output', 'cses.json')
BC_JSON = os.path.join(ROOT_DIR, 'output', 'beecrowd.json')
SCRIPT_PATH = os.path.join(os.path.dirname(ROOT_DIR), "script.js")
UPDATE_PATH = os.path.join(os.path.dirname(ROOT_DIR), "automation", "update.sh")

TMP_JSON = os.path.join(ROOT_DIR, "output", "tmp.json")