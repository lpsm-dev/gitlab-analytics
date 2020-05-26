# -*- coding: utf-8 -*-

"""Documentation file log.py."""

import logging
import coloredlogs
from tools.os import OS
from typing import NoReturn, Text
from settings.handlers import BaseFileHandler, ContextHandler

class SingletonLogger(type):

  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(SingletonLogger, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

class Log(OS, metaclass=SingletonLogger):

  def __init__(self, log_path: Text, log_file: Text, log_level: Text, logger_name: Text) -> NoReturn:

    self._log_path = log_path if log_path else "./log/info"
    self._log_file = self.join_directory_with_file(self.log_path, log_file if log_file else "file.log")
    self._log_level = log_level if log_level in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"] else None
    self._logger_name = logger_name
    self.formatter = "%(levelname)s - %(asctime)s - %(message)s - %(pathname)s - %(funcName)s"
    self._check_if_log_path_and_log_file_exist()
    self._logger = logging.getLogger(self.logger_name)
    self._logger.setLevel(self.log_level)
    self._base_configuration_log_colored()
    self._logger.addHandler(ContextHandler(BaseFileHandler()).get_handler(log_file=self.log_file, log_level=self.log_level, formatter=self.formatter))

  def _check_if_log_path_and_log_file_exist(self) -> NoReturn:
    if self.check_if_is_dir(self.log_path):
      if not self.check_if_is_file(self.log_file):
        self.create_file(self.log_file)
    else:
      self.create_directory(self.log_path)
      self.create_file(self.log_file)

  def _base_configuration_log_colored(self) -> coloredlogs.install:
    coloredlogs.install(level=self._log_level,
                        logger=self.logger,
                        fmt=self.formatter,
                        milliseconds=True)

  @property
  def log_path(self) -> Text:
    return self._log_path

  @property
  def log_file(self) -> Text:
    return self._log_file

  @property
  def log_level(self) -> Text:
    return self._log_level

  @property
  def logger_name(self) -> Text:
    return self._logger_name

  @property
  def logger(self) -> Text:
    return self._logger
