import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class RequestResponse:

  def __init__(self, response: Text) -> NoReturn:
    self.status = response.status_code
    self.reason = response.reason
    self.json = response.json()

  def get_json(self):
    return self.json

class GitLabClient:

  def __init__(self, url, token, is_secure=True, retry=False):
    self.url = url
    self.token = token
    if retry:
      self.session = self.requests_retry_session()
    else:
      self.session = requests.Session()

  @staticmethod
  def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None) -> requests.Session():
      session = session or requests.Session()
      retry = Retry(
          total=retries,
          read=retries,
          connect=retries,
          backoff_factor=backoff_factor,
          status_forcelist=status_forcelist,
      )
      adapter = HTTPAdapter(max_retries=retry)
      session.mount("http://", adapter)
      session.mount("https://", adapter)
      return session

  def call(self, route, params):
    try:
      pass
    except:
      pass

  @property
  def _headers(self):
    return {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.token}"
    }
