from .constants import TIMETABLE_DATABASE_LINK
from .constants import TIMETABLE_LESSONS_LINK
from datetime import date
from typing import List
import requests


def load_main_db() -> requests.Response:
    data = request_timetable_database()
    tables = get_tables(data)


def get_tables(data: dict) -> List[dict]:
    return data['r']['tables']


def get_data_rows(data: dict) -> List[dict]:
    return data['data_rows']


def request_timetable_database():
    return requests.post(url=TIMETABLE_DATABASE_LINK, json=_timetable_database_data()).json()


def _timetable_database_data():
    return {
        "__args":
        [
            None,
            school_year(),
            {},
            {
                "op": "fetch",
                "needed_part":
                {
                    "teachers":
                    [
                        "short"
                    ],
                    "classes":
                    [
                        "short"
                    ],
                    "classrooms":
                    [
                        "short"
                    ],
                    "subjects":
                    [
                        "name"
                    ],
                    "periods":
                    [
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


def school_year() -> int:
    today = date.today()
    return today.year if today.month in range(9, 13) else today.year - 1
