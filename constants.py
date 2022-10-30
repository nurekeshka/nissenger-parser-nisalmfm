from enum import Enum


class Links(Enum):
    database = 'https://fmalmnis.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'
    lessons = 'https://fmalmnis.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'


class By(object):
    SUBJECT = 'subjects'
    CLASS = 'classes'
    TEACHER = 'teachers'
    CLASSROOM = 'classrooms'
