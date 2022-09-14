from enum import Enum


class Links(Enum):
    database = 'https://fmalmnis.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'
    lessons = 'https://fmalmnis.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'


class Indexes(Enum):
    teachers = 0
    subjects = 1
    classrooms = 2
    classes = 3
    periods = 4

    uniperiod = 'uniperiod'
    starttime = 'starttime'
    endtime = 'endtime'

    subjectid = 'subjectid'
    teacherids = 'teacherids'
    classids = 'classids'
    classroomids = 'classroomids'

    id = 'id'
    data_rows = 'data_rows'
    short = 'short'
    name = 'name'
    period = 'period'
