from enum import Enum


class Link(Enum):
    database = 'https://fmalmnis.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'
    lessons = 'https://fmalmnis.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'


DAYS = (
    None,
    'monday',
    'tuesday',
    'weekday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
)
