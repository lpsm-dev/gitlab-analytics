# -*- coding: utf-8 -*-

import yaml
from tools.os import OS
from typing import NoReturn, Text, Dict

class YmlReader(OS):

  def __init__(self, yml_path: Text, yml_file: Text) -> NoReturn:
    self.yml_path = yml_path if yml_path else "/usr/src/code"
    if yml_file.endswith(".yaml") or yml_file.endswith(".yml"):
      self.yml_file = self.join_directory_with_file(self.yml_path, yml_file if yml_file else "values.yml")
    else:
      raise Exception("We need a YML File")
    self.check_if_path_and_file_exist(self.yml_path, self.yml_file, creation=False)

  def get_content(self) -> Dict:
    stream = open(self.yml_file, "r")
    return yaml.load(stream, Loader=yaml.FullLoader)
