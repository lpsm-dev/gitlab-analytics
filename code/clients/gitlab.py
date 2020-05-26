# -*- coding: utf-8 -*-

import requests
import urllib.parse
from json import JSONDecodeError
from cachetools import cached, TTLCache
from typing import Text, NoReturn
from exception import RequestGetException, RequestGetStatusException
from clients.requests import RequestsImplementation, RequestResponse

class GitLabClient(RequestsImplementation):

  def __init__(self, url: Text, token: Text, *args, **kwargs) -> NoReturn:
    self.token = token
    super().__init__(url, *args, **kwargs)

  @cached(cache=TTLCache(maxsize=1024, ttl=3600))
  def call(self, route, params):
    try:
      url = urllib.parse.urljoin(self.url, route)
      print(url)
      response = self.session.get(
        url,
        params=params,
        headers=self._headers
      )
      response = RequestResponse(response)
      if response.status == requests.codes.ok:
        self.logger.info(f"Success request - Status {response.status}")
        try:
          response = response.get_json()
          self.logger.info(f"Success get json data")
          return {
            "status": True,
            "data": response
          }
        except JSONDecodeError:
          response = response.reason
          self.logger.error(f"Error get json data")
          return {
            "status": False,
            "data": "response"
          }
      else:
        raise RequestGetStatusException(f"Invalid request - Status {response.status}")
        return {
          "status": False,
          "data": ""
        }
    except RequestGetException:
      self.logger.error("Error Resquest Get")
      return {
        "status": False,
        "data": ""
      }

  @property
  def _headers(self):
    return {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.token}"
    }
