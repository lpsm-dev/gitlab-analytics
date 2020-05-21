# -*- coding: utf-8 -*-

"""Documentation file exception.py"""

from typing import NoReturn, Text

class ExceptionDefault(object):

  @staticmethod
  def raise_exception(exception: Text) -> NoReturn:
    raise exception

class SettingsException(Exception):
  pass

class CreateParserException(SettingsException):
  pass
