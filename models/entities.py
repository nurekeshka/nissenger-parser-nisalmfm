from constants import CLASSROOM_CHANGES
from constants import TEACHER_CHANGES
from constants import SUBJECT_CHANGES
from typing import List, Tuple


class BaseTimetableEntity(object):
    changes = dict()

    def __init__(self, name: str):
        self.name = name
        self._parse_name()

    def _parse_name(self):
        if self.name in self.changes:
            self.name = self.changes[self.name]

    def __str__(self):
        return self.name


class ParseTitleMixin(object):
    changes = dict()

    def _parse_name(self):
        if self.name in self.changes:
            self.name = self.changes[self.name]
        else:
            self.name = str(self.name).lower().title()


class Teacher(BaseTimetableEntity, ParseTitleMixin):
    changes = TEACHER_CHANGES


class Period(BaseTimetableEntity):
    def __init__(self, number: int, starttime: str, endtime: str):
        self.number = int(number)
        self.starttime = starttime
        self.endtime = endtime

    def __str__(self):
        return f'{self.starttime} | {self.endtime}'


class Subject(BaseTimetableEntity):
    changes = SUBJECT_CHANGES


class Classroom(BaseTimetableEntity):
    changes = CLASSROOM_CHANGES


class Class(BaseTimetableEntity):
    def __init__(self, name: str):
        self.grade = int(name[:-1])
        self.letter = name[-1]

    def __str__(self):
        return f'{self.grade}{self.letter}'


class Lesson(object):
    def __init__(self, subject: Subject, period: Period, teacher: Teacher, classroom: Classroom, classes: Tuple[Class], duration: int):
        self.subject: Subject = subject
        self.period: Period = period
        self.teacher: Teacher = teacher
        self.classroom: Classroom = classroom
        self.classes: List[Class] = classes
        self.duration: int = duration

    def __str__(self):
        return f'{self.subject} - {self.teacher}, {self.classroom}: {", ".join(map(str, self.classes))} :: {self.period} x{self.duration}'
