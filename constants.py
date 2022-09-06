from enum import Enum


class EdupageLinks(Enum):
    main_db_link = 'https://fmalmnis.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'


class EdupageMainDbIDs(Enum):
    teachers = 0
    subjects = 1
    classrooms = 2
    classes = 3
    periods = 4
