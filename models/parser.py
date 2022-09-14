from constants import Indexes as indexes
from models.entities import Classroom
from models.entities import Teacher
from models.entities import Subject
from models.entities import Period
from models.entities import Lesson
from models.entities import Class
from models.loader import Loader
from typing import Tuple
from typing import Dict


class Parser(object):
    def __init__(self, loader: Loader, *args, **kwargs):
        self.loader: Loader = loader
        self.initialize_dictionaries()
        self.load_database()
        self.load_lessons()

    def initialize_dictionaries(self):
        self.classrooms: Dict[str, Classroom] = dict()
        self.teachers: Dict[str, Teacher] = dict()
        self.subjects: Dict[str, Subject] = dict()
        self.periods: Dict[str, Period] = dict()
        self.classes: Dict[str, Class] = dict()

    def load_database(self):
        for teacher in self.loader.tables[indexes.teachers.value]['data_rows']:
            self.teachers[teacher['id']] = Teacher(teacher['short'])

        for period in self.loader.tables[indexes.periods.value]['data_rows']:
            self.periods[period['id']] = Period(
                period['period'], period['starttime'], period['endtime'])

        for subject in self.loader.tables[indexes.subjects.value]['data_rows']:
            self.subjects[subject['id']] = Subject(subject['name'])

        for classroom in self.loader.tables[indexes.classrooms.value]['data_rows']:
            self.classrooms[classroom['id']] = Classroom(
                classroom['short'])

        for _class in self.loader.tables[indexes.classes.value]['data_rows']:
            self.classes[_class['id']] = Class(_class['short'])

    def parse_lesson(self, payload) -> Lesson:
        subject = self.subjects[payload['subjectid']]
        teacher = self.teachers[payload['teacherids'][0]]
        classroom = self.classrooms[payload['classroomids'][0]]
        period = Period(payload['uniperiod'],
                        payload['starttime'], payload['endtime'])
        classes = [self.classes[_class]
                   for _class in payload['classids']]

        return Lesson(
            subject=subject,
            teacher=teacher,
            period=period,
            classroom=classroom,
            classes=classes,
        )

    def load_lessons(self):
        for class_lessons in self.loader.lessons.values():
            for lesson in class_lessons:
                entity = self.parse_lesson(lesson)
                print(entity)
                return
