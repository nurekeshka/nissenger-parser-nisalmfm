import utils
import requests
from constants import Links as links


class AbstractSender(object):
    url: str = None
    method: requests.get = requests.get

    def format(self) -> dict | str:
        self.data = self.response.json()

    def request(self, *args, **kwargs):
        self.response = self.method(url=self.url)
        self.format()
