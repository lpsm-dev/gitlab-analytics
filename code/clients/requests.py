# -*- coding: utf-8 -*-

from __future__ import annotations

import requests
from validators.url import URL
from abc import ABC, abstractmethod
from requests.adapters import HTTPAdapter
from typing import Text, NoReturn, Callable, Dict
from requests.packages.urllib3.util.retry import Retry

class RequestResponse:

  def __init__(self, response: Text) -> NoReturn:
    self.status = response.status_code
    self.reason = response.reason
    self.json = response.json()

  def get_json(self) -> Dict:
    return self.json

class RequestsImplementation(ABC):

  def __init__(self, url: Text, *args, **kwargs) -> NoReturn:
    if not kwargs["is_secure"]:
      self.url = url.replace("https", "http")
    self.url = url
    self._logger = kwargs["logger"]
    if kwargs["retry"]:
      self.session = self.requests_retry_session(kwargs["session"])
    else:
      self.session = requests.Session()

  @staticmethod
  def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None) -> requests.Session():
    session = session or requests.Session()
    retry = Retry(total=retries, read=retries,
        connect=retries, backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

  @abstractmethod
  def call(self) -> NoReturn:
    pass

  @property
  def logger(self) -> Callable:
    return self._logger
