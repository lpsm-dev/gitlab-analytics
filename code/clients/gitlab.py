# -*- coding: utf-8 -*-

import requests
import urllib.parse
from json import JSONDecodeError
from typing import Text, NoReturn, Dict
from exception import RequestGetException, RequestGetStatusException
from clients.requests import RequestsImplementation, RequestResponse

class GitLabClient(RequestsImplementation):

  def __init__(self, url: Text, token: Text, *args, **kwargs) -> NoReturn:
    self.token = token
    super().__init__(url, *args, **kwargs)

  def call_implementation(self, route: Text, params: Dict) -> Dict:
    try:
      response = self.session.get(
        urllib.parse.urljoin(self.url, route),
        params=params,
        headers=self._headers
      )
      headers = response.headers
      response = RequestResponse(response)
      if response.status == requests.codes.ok:
        self.logger.info(f"Success request - Status {response.status}")
        try:
          response = response.get_json()
          self.logger.info(f"Success get json data")
          return {
            "status": True,
            "headers": headers,
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
