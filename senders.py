import utils
import requests
from constants import Links as links


class AbstractSender(object):
    url: str = None
    method: requests.get = requests.get

    def __init__(self):
        pass

    @classmethod
    def format(self) -> dict | str:
        return self.response.json()

    @classmethod
    def request(self, *args, **kwargs):
        self.response: requests.Response = self.method(url=self.url)
        self.data: dict | str = self.format()


class JsonSender(AbstractSender):
    @classmethod
    def json(self, *args, **kwargs):
        return {}

    @classmethod
    def request(self, *args, **kwargs):
        self.response: requests.Response = self.method(
            url=self.url,
            json=self.json(*args, **kwargs)
        )

        self.data: dict | str = self.format()


class DatabaseSender(JsonSender):
    url = links.database.value
    method = requests.post

    @classmethod
    def format(self) -> dict:
        data = self.response.json()
        return [table['data_rows'] for table in data['r']['tables']]

    @classmethod
    def json(self) -> dict:
        return {
            "__args": [
                None,
                utils.get_school_year(),
                {},
                {
                    "op": "fetch",
                    "needed_part": {
                        "teachers": [
                            "short"
                        ],
                        "classes": [
                            "short"
                        ],
                        "classrooms": [
                            "short"
                        ],
                        "subjects": [
                            "name"
                        ],
                        "periods": [
                            "period",
                            "starttime",
                            "endtime"
                        ]
                    },
                    "needed_combos": {}
                }
            ],
            "__gsh": "00000000"
        }


class LessonsSender(JsonSender):
    url = links.lessons.value
    method = requests.post

    @classmethod
    def format(self) -> dict:
        data = self.response.json()
        self.data = data['r']['ttitems']

    @classmethod
    def json(self, *args, **kwargs) -> dict:
        print(args)
        print(kwargs)
        return {
            "__args": [
                None,
                {
                    "year": utils.get_school_year(),
                    "datefrom": "2022-10-03",
                    "dateto": "2022-10-09",
                    "table": "classes",
                    "id": "-30"
                }
            ],
            "__gsh": "00000000"
        }
