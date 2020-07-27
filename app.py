import os, sys
import requests
import platform

# TODO: support Linux w/ XFCE
if platform.system() == 'Darwin':
    OS = 'Mac'

from dotenv import load_dotenv

load_dotenv() # unlike in R, this must always be called
os.getenv('GITHUB_USERNAME')
base_url = "https://api.github.com/"
auth_header = {'Authorization' : f"token {os.getenv('AUTH_TOKEN')}"}

# TODO: use Popen over os.sytem, also figure out why
def osx_dialog(title, message):
    os.system(f"osascript -e 'display dialog \"{message}\" with title \"{title}\"'")

def osx_notify(title, message):
    # TODO: have button that spawns dialog, may require JS
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")

def get_list_from_endpoint(endpoint):
    r = requests.get(endpoint, headers = auth_header).json()
    return r['items']

pr_reviews_url = f"{base_url}search/issues?q=is:open+is:pr+review-requested:{os.getenv('GITHUB_USERNAME')}"
reviews = get_list_from_endpoint(pr_reviews_url)

repos = set()
_ = [repos.add(i['html_url']) for i in reviews]

title = f"You have {len(reviews)} open PR review requests"
message = "\n".join(list(repos))

#osx_notify(title = title, message = message) # this returns a button status but it's async

# TODO: add a gatekeeper to this firing because it's annoying
osx_dialog(title = title, message = message)

# terminate before unfinished calls
sys.exit()

# stdout
# print(f"You have {len(reviews)} open PR review requests.")
# print(*repos, sep='\n')

# TODO: report assigned issues
assigned_url = f"{base_url}search/issues?q=is:open+assignee:{os.getenv('GITHUB_USERNAME')}"
assignments = get_list_from_endpoint(assigned_url)

# TODO: report mentions not in assignments/reviews
mentions_url = f"{base_url}search/issues?q=is:open+mentions:{os.getenv('GITHUB_USERNAME')}"
mentions = get_list_from_endpoint(mentions_url)
