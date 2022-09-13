from utils import school_year
from utils import current_week


def database_json() -> dict:
    return {
        "__args": [
            None,
            school_year(),
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


def lessons_json(id: str) -> dict:
    firstday, lastday = current_week()

    return {
        "__args":[
            None,
            {
                "year": school_year(),
                "datefrom": firstday,
                "dateto": lastday,
                "table":"classes",
                "id": id,
                }
            ],
        "__gsh":"00000000"
    }    
