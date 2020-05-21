# -*- coding: utf-8 -*-

"""Documentation file main.py."""

import requests
import urllib.parse
from pprint import pprint

from settings.config import Config
from settings.arguments import Arguments

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format("GitLab", font="starwars"), "white", attrs=["dark"])

config, args = Config(), Arguments(description="GitLab Analytics").args

gitlab_url = config.get_env("GITLAB_URL") if config.get_env("GITLAB_URL") else (args["url"] if args["url"] else "https://git.stfcia.com.br")
gitlab_token = config.get_env("GITLAB_TOKEN") if config.get_env("GITLAB_TOKEN") else (args["token"] if args["token"] else None)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {gitlab_token}"
}

params = {
  "sort": "asc"
}

projects = requests.get(urllib.parse.urljoin(gitlab_url, "/api/v4/projects"), params=params, headers=headers)
groups = requests.get(urllib.parse.urljoin(gitlab_url, "/api/v4/groups"), params=params, headers=headers)
users = requests.get(urllib.parse.urljoin(gitlab_url, "/api/v4/users"), params=params, headers=headers)

pprint(projects.headers["X-Total"])
pprint(groups.headers["X-Total"])
pprint(users.headers["X-Total"])
