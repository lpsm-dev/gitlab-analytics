# -*- coding: utf-8 -*-

from typing import NoReturn, Callable, Text, Dict
from clients.requests import RequestsImplementation

class Gitlab:

  def __init__(self, client: RequestsImplementation) -> NoReturn:
    self.client = client

  def call(self, route: Text, params: Dict) -> Callable:
    return self.client.get(route, params)

  @staticmethod
  def resources():
    return {
      "users": {
          "route": "/api/v4/users",
          "params": {
              "page": 1,
              "per_page": 1,
              "sort": "asc"
          }
      },
      "projects": {
          "route": "/api/v4/projects",
          "params": {
              "page": 1,
              "per_page": 1,
              "sort": "asc"
          }
      },
      "groups": {
          "route": "/api/v4/groups",
          "params": {
              "page": 1,
              "per_page": 1,
              "sort": "asc"
          }
      }
    }

