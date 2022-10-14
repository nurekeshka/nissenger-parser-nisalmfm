from datetime import date
from typing import List

import requests

from apps.core import models
from apps.fmalmnis import constants as const
from apps.fmalmnis.constants import TimetableIndexes as indexes


def find_group_by_classes(classes: List[models.Class]) -> models.Group:
    return models.Group.objects.filter(classes__in=classes)


def load_teachers(teachers: list, timetable: models.Timetable):
    change = const.TEACHER_CHANGES
    changes = const.TEACHER_CHANGES.keys()

    for teacher in teachers:
        name = change[teacher['short']
                      ] if teacher['short'] in changes else teacher['short']
        models.Teacher.objects.create(
            name=name.lower().title(), timetable=timetable)


def load_subjects(subjects: list, timetable: models.Timetable):
    change = const.SUBJECT_CHANGES
    changes = const.SUBJECT_CHANGES.keys()

    for subject in subjects:
        name = change[subject['name']
                      ] if subject['name'] in changes else subject['name']
        models.Subject.objects.create(name=name, timetable=timetable)


def load_offices(classrooms: list, timetable: models.Timetable):
    change = const.CLASSROOM_CHANGES
    changes = const.CLASSROOM_CHANGES.keys()

    for classroom in classrooms:
        name = change[classroom['short']
                      ] if classroom['short'] in changes else classroom['short']
        models.Classroom.objects.create(name=name, timetable=timetable)


def load_periods(periods: list, timetable: models.Timetable):
    for period in periods:
        models.Period.objects.create(
            number=period['period'], starttime=period['starttime'], endtime=period['endtime'], timetable=timetable)


def load_classes(class_names: list, timetable: models.Timetable):
    for class_name in class_names:
        grade = int(class_name['short'][:-1])
        letter = class_name['short'][-1]

        entity = models.Class.objects.create(
            grade=grade, letter=letter, timetable=timetable)

        for number in range(1, 3):
            group = models.Group.objects.create(
                name=f'{number} - группа: {entity}', timetable=timetable)
            group.classes.add(entity)


def load_entities(tables: dict, timetable: models.Timetable) -> dict:
    load_teachers(get_data_rows(tables[indexes.teachers.value]), timetable)
    load_subjects(get_data_rows(tables[indexes.subjects.value]), timetable)
    load_offices(get_data_rows(tables[indexes.classrooms.value]), timetable)
    load_periods(get_data_rows(tables[indexes.periods.value]), timetable)
    load_classes(get_data_rows(tables[indexes.classes.value]), timetable)


def load_main_db(timetable: models.Timetable) -> requests.Response:
    data = request_timetable_database()
    tables = get_tables(data)
    load_entities(tables, timetable)


def get_tables(data: dict) -> List[dict]:
    return data['r']['tables']


def get_data_rows(data: dict) -> List[dict]:
    return data['data_rows']


def request_timetable_database():
    return requests.post(url=const.TIMETABLE_DATABASE_LINK, json=_timetable_database_data()).json()


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
