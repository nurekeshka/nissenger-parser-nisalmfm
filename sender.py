from constants import EdupageLinks
from utils import get_current_year
from utils import get_current_week
from requests import Response
from requests import Request
from requests import post


def request_main_db() -> Response:
    return post(
        url=EdupageLinks.main_db_link.value,
        json=create_main_db_request_json()
    )


def create_main_db_request_json() -> dict:
    return {
        "__args": [
            None,
            get_current_year(),
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


def create_current_js_request_json(class_id: str) -> dict:
    firstday, lastday = get_current_week()

    return {
        "__args":[
            None,
            {
                "year": get_current_year(),
                "datefrom": firstday,
                "dateto": lastday,
                "table":"classes",
                "id": class_id,
                }
            ],
        "__gsh":"00000000"
    }    
