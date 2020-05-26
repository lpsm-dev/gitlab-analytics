# -*- coding: utf-8 -*-

from typing import NoReturn, Callable
from clients.requests import RequestsImplementation

class Gitlab:
  def __init__(self, implementation: RequestsImplementation) -> NoReturn:
    self.implementation = implementation

  def call(self, route, params) -> Callable:
    return self.implementation.call(route, params)
