from datetime import date, timedelta
from typing import Dict, List, Tuple

import requests

from apps.core import models
from apps.fmalmnis import constants as const
from apps.fmalmnis.constants import TimetableIndexes as indexes


def find_group_by_classes(classes: List[models.Class]) -> models.Group:
    return models.Group.objects.filter(classes__in=classes)


def load_teachers(teachers: list, timetable: models.Timetable):
    change = const.TEACHER_CHANGES
    changes = const.TEACHER_CHANGES.keys()

    table = dict()

    for teacher in teachers:
        name = change[teacher['short']
                      ] if teacher['short'] in changes else teacher['short']
        table[teacher['id']] = models.Teacher.objects.create(
            name=name.lower().title(), timetable=timetable)

    return table


def load_subjects(subjects: list, timetable: models.Timetable):
    change = const.SUBJECT_CHANGES
    changes = const.SUBJECT_CHANGES.keys()

    table = dict()

    for subject in subjects:
        name = change[subject['name']
                      ] if subject['name'] in changes else subject['name']
        table[subject['id']] = models.Subject.objects.get_or_create(
            name=name, timetable=timetable)[0]

    return table


def load_classrooms(classrooms: list, timetable: models.Timetable):
    change = const.CLASSROOM_CHANGES
    changes = const.CLASSROOM_CHANGES.keys()

    table = dict()

    for classroom in classrooms:
        name = change[classroom['short']
                      ] if classroom['short'] in changes else classroom['short']
        table[classroom['id']] = models.Classroom.objects.create(
            name=name, timetable=timetable)

    return table


def load_periods(periods: list, timetable: models.Timetable):
    table = dict()

    for period in periods:
        table[int(period['period'])] = models.Period.objects.create(
            number=period['period'], starttime=period['starttime'], endtime=period['endtime'], timetable=timetable)

    return table


def load_classes(classes: list, timetable: models.Timetable):
    table = dict()

    for _class in classes:
        grade = int(_class['short'][:-1])
        letter = _class['short'][-1]

        entity = models.Class.objects.create(
            grade=grade, letter=letter, timetable=timetable)

        table[_class['id']] = entity

        for number in (1, 2):
            group = models.Group.objects.create(
                name=number, timetable=timetable)
            group.classes.add(entity)

    return table


def load_entities(tables: dict, timetable: models.Timetable) -> dict:
    teachers = load_teachers(get_data_rows(
        tables[indexes.teachers.value]), timetable)
    subjects = load_subjects(get_data_rows(
        tables[indexes.subjects.value]), timetable)
    classrooms = load_classrooms(get_data_rows(
        tables[indexes.classrooms.value]), timetable)
    periods = load_periods(get_data_rows(
        tables[indexes.periods.value]), timetable)
    classes = load_classes(get_data_rows(
        tables[indexes.classes.value]), timetable)

    load_lessons(teachers, subjects, classrooms, periods, classes, timetable)


def load_main_db(timetable: models.Timetable):
    response = request_timetable_database()
    tables = get_tables(response)
    load_entities(tables, timetable)


def load_lessons(teachers: Dict[str, models.Teacher],
                 subjects: Dict[str, models.Subject],
                 classrooms: Dict[str, models.Classroom],
                 periods: Dict[int, models.Period],
                 classes: Dict[str, models.Class],
                 timetable: models.Timetable,
                 ):
    data: Dict[str, dict] = {'teachers': teachers, 'classrooms': classrooms,
                             'periods': periods, 'classes': classes}

    for subject_id in subjects.keys():
        subject = models.Subject.objects.get(
            name=subjects[subject_id], timetable=timetable)

        response = request_lessons(subject_id)
        lessons = get_lessons(response)

        for lesson in lessons:
            parse_lesson_by_subjects(lesson, subject, data, timetable)


def request_lessons(subject_id: str) -> dict:
    return requests.post(url=const.TIMETABLE_LESSONS_LINK, json=__timetable_lessons_by_subject(subject_id)).json()


def get_tables(data: dict) -> List[dict]:
    return data['r']['tables']


def get_lessons(data: dict) -> List[dict]:
    return data['r']['ttitems']


def get_data_rows(data: dict) -> List[dict]:
    return data['data_rows']


def parse_lesson_by_subjects(lesson: dict, subject: models.Subject, data: Dict[str, dict], timetable: models.Timetable):
    lesson_classes = list()

    for _class_name in lesson['classids']:
        lesson_classes.append(data['classes'][_class_name])

    if lesson['groupnames'][0] == '':
        groups = models.Group.objects.filter(
            classes__in=lesson_classes, timetable=timetable)

    elif lesson['groupnames'][0] in ('1 Подгруппа', '2 Подгруппа'):
        groups = models.Group.objects.get(
            classes__in=lesson_classes, timetable=timetable, name=int(lesson['groupnames'][0][0]))

    else:
        groups = models.Group.objects.get_or_create(
            name=lesson['groupnames'], timetable=timetable, classes__in=lesson_classes)

    classroom = None
    teacher = None
    period = None
    group = None
    day = None

    # models.Lesson.objects.create(
    #     subject=subject,
    #     classroom=classroom,
    #     teacher=teacher,
    #     period=period,
    #     group=group,
    #     day=day,
    #     timetable=timetable,
    # )


def request_timetable_database() -> dict:
    return requests.post(url=const.TIMETABLE_DATABASE_LINK, json=__timetable_database_data()).json()


def __timetable_lessons_by_subject(subject_id: str):
    firstday, lastday = get_current_week()

    return {
        "__args": [
            None,
            {
                "year": school_year(),
                "datefrom": firstday,
                "dateto": lastday,
                "table": "subjects",
                "id": subject_id,
            }
        ],
        "__gsh": "00000000"
    }


def __timetable_database_data():
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


def get_current_week() -> Tuple[str]:
    today: date = date.today()
    weekday: int = today.weekday()

    firstday: date = today - timedelta(days=weekday)
    lastday: date = firstday + timedelta(days=6)

    return tuple(map(lambda day: day.strftime('%Y-%m-%d'), (firstday, lastday)))
