# -*- coding: utf-8 -*-

"""Documentation file main.py."""

import requests
import urllib.parse
from pprint import pprint

from settings.log import Log
from settings.config import Config
from settings.arguments import Arguments

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
  cprint(figlet_format("GitLab", font="starwars"), "white", attrs=["dark"])

  config, args = Config(), Arguments(description="GitLab Analytics").args

  gitlab_url = config.get_env("GITLAB_URL") if config.get_env("GITLAB_URL") else (args["url"] if args["url"] else "https://git.stfcia.com.br")
  gitlab_token = config.get_env("GITLAB_TOKEN") if config.get_env("GITLAB_TOKEN") else (args["token"] if args["token"] else None)

  log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else "/var/log/code"
  log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else "file.log"
  log_level = config.get_env("LOG_LEVEL") if config.get_env("LOG_LEVEL") else "DEBUG"
  logger_name = config.get_env("LOGGER_NAME") if config.get_env("LOGGER_NAME") else "Code"

  log = Log(log_path, log_file, log_level, logger_name).logger

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

  total_projects = projects.headers["X-Total"]
  total_groups = groups.headers["X-Total"]
  total_users = users.headers["X-Total"]

  log.info("Show Details")

  print(f"\nTotal de Projetos: {total_projects}")
  print(f"Total de Grupos: {total_groups}")
  print(f"Total de Users: {total_users}")
