# -*- coding: utf-8 -*-

from typing import Text
from exception import URLTypeException, URLException, InvalidURL

try:
  from urllib.parse import urlparse
except ImportError:
  from urlparse import urlparse

class URL:

  @staticmethod
  def url_validator(url: Text) -> bool:
    if url.startswith ("http://") or url.startswith ("https://"):
      if isinstance(url, str):
        try:
          result = urlparse(url)
          return all([result.scheme, result.netloc, result.path])
        except:
          raise InvalidURL(f"This URL {url} is invalid...")
      else:
        raise URLTypeException(f"We speec a {type(str)} not a {type(url)}")
    else:
        raise URLException("We need a url with https:// or http://...")
