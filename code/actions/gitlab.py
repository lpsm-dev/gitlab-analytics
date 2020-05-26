# -*- coding: utf-8 -*-

from typing import NoReturn, Callable, Text, Dict
from clients.requests import RequestsImplementation

class Gitlab:

  def __init__(self, implementation: RequestsImplementation) -> NoReturn:
    self.implementation = implementation

  def call(self, route: Text, params: Dict) -> Callable:
    return self.implementation.call(route, params)
