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

from utils import first


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
        for teacher in self.loader.tables[indexes.teachers.value][indexes.data_rows.value]:
            self.teachers[teacher[indexes.id.value]] = Teacher(
                teacher[indexes.short.value])

        for period in self.loader.tables[indexes.periods.value][indexes.data_rows.value]:
            self.periods[period[indexes.id.value]] = Period(
                period[indexes.period.value], period[indexes.starttime.value], period['endtime'])

        for subject in self.loader.tables[indexes.subjects.value][indexes.data_rows.value]:
            self.subjects[subject[indexes.id.value]] = Subject(
                subject[indexes.name.value])

        for classroom in self.loader.tables[indexes.classrooms.value][indexes.data_rows.value]:
            self.classrooms[classroom[indexes.id.value]] = Classroom(
                classroom[indexes.short.value])

        for _class in self.loader.tables[indexes.classes.value][indexes.data_rows.value]:
            self.classes[_class[indexes.id.value]] = Class(
                _class[indexes.short.value])

    def parse_lesson(self, payload: Dict[str, dict]) -> Lesson:
        subject = self.subjects[payload[indexes.subjectid.value]]
        duration = payload.get(indexes.durationperiods.value) if payload.get(
            indexes.durationperiods.value) else 1

        teacher = self.teachers.get(first(payload[indexes.teacherids.value]))
        classroom = self.classrooms.get(
            first(payload[indexes.classroomids.value]))

        period = Period(payload[indexes.uniperiod.value],
                        payload[indexes.starttime.value], payload[indexes.endtime.value])

        classes = [self.classes[_class]
                   for _class in payload[indexes.classids.value]]

        return Lesson(
            subject=subject,
            teacher=teacher,
            period=period,
            classroom=classroom,
            classes=classes,
            duration=duration,
        )

    def load_lessons(self):
        for class_lessons in self.loader.lessons.values():
            for lesson in class_lessons:
                entity = self.parse_lesson(lesson)
                print(entity)
            return
