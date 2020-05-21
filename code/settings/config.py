# -*- coding: utf-8 -*-

"""Documentation file config.py."""

from os import environ
from typing import Text

class Config:

  @staticmethod
  def get_env(env: Text) -> Text:
    """Method to return env value."""
    try:
      return environ.get(env)
    except Exception as error:
      print(f"Key Error: {error}")
