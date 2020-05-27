# -*- coding: utf-8 -*-

from typing import Text
from exception import InvalidURL, URLException, URLTypeException

try:
  from urllib.parse import urlparse
except ImportError:
  from urlparse import urlparse

class URL:

  @classmethod
  def url_validator(cls, url: Text) -> bool:
    if isinstance(url, str):
      if url.startswith ("http://") or url.startswith ("https://"):
        try:
          result = urlparse(url)
          return all([result.scheme, result.netloc])
        except ValueError:
          raise InvalidURL(f"Invalid URL - {url}")
      else:
        raise URLException("We need a url with https:// or http://...")
    else:
      raise URLTypeException(f"We speec a {type(str)} not a {type(url)}")
