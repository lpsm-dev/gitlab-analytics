# -*- coding: utf-8 -*-

import requests
import urllib.parse
from typing import NoReturn

from settings.log import Log
from settings.config import Config
from settings.arguments import Arguments

from actions.gitlab import Gitlab

from clients.gitlab import GitLabClient

from tools.yml import YmlReader

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# ==============================================================================
# GLOBAL
# ==============================================================================

config, args = Config(), Arguments(description="GitLab Analytics").args

yml = YmlReader("/usr/src/code", "values.yml")

gitlab_url = config.get_env("GITLAB_URL") if config.get_env("GITLAB_URL") else (args["url"] if args["url"] else "https://git.stfcia.com.br")
gitlab_token = config.get_env("GITLAB_TOKEN") if config.get_env("GITLAB_TOKEN") else (args["token"] if args["token"] else None)

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else "/var/log/code"
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else "file.log"
log_level = config.get_env("LOG_LEVEL") if config.get_env("LOG_LEVEL") else "DEBUG"
logger_name = config.get_env("LOGGER_NAME") if config.get_env("LOGGER_NAME") else "Code"

logger = Log(log_path, log_file, log_level, logger_name).logger

gitlab_client = GitLabClient(gitlab_url, gitlab_token, retry=False, is_secure=True, session=None, logger=logger)
gitlab = Gitlab(gitlab_client)
gitlab_resources = gitlab.resources()

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format("GitLab", font="starwars"), "white", attrs=["dark"])

  logger.info("Running Script... Getting information")

  projects = gitlab.call(gitlab_resources["projects"]["route"], gitlab_resources["projects"]["params"])
  groups = gitlab.call(gitlab_resources["groups"]["route"], gitlab_resources["groups"]["params"])
  users = gitlab.call(gitlab_resources["users"]["route"], gitlab_resources["users"]["params"])

  logger.info("Getting Request Headers X-Total")

  total_projects = projects["headers"]["X-Total"]
  total_groups = groups["headers"]["X-Total"]
  total_users = users["headers"]["X-Total"]

  logger.info("Show information")

  print(f"\nTotal de Projetos: {total_projects}")
  print(f"Total de Grupos: {total_groups}")
  print(f"Total de Users: {total_users}\n")
