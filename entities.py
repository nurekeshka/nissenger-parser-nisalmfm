import inspect
from typing import List


class BaseEntity(object):
    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name

    def __str__(self):
        return self.name

    def getattributes(self) -> List[str]:
        return [attr for attr in dir(self) if not inspect.ismethod(
            attr) and not attr.startswith('_')]


class Teacher(BaseEntity):
    pass


class Subject(BaseEntity):
    pass


class Classroom(BaseEntity):
    pass


class Class(BaseEntity):
    def __init__(self, id: str, grade: int, letter: str):
        self.id: str = id
        self.grade: int = grade
        self.letter: str = letter

    def __str__(self):
        return f'{self.grade}{self.letter}'


class Period(BaseEntity):
    def __init__(self, id: str, number: int, starttime: str, endtime: str):
        self.id = id
        self.number: int = int(number)
        self.starttime: str = starttime
        self.endtime: str = endtime

    def __str__(self):
        return f'{self.starttime} - {self.endtime}'


class Day(BaseEntity):
    def __init__(self, number: int, name: str):
        self.number = int(number)
        self.name = name


class Group(BaseEntity):
    def __init__(self, name: str, classes: List[Class]):
        self.name = name
        self.classes = classes


class Lesson(BaseEntity):
    def __init__(self, subject: Subject, teacher: Teacher, classroom: Classroom, group: Group, period: Period, day: Day):
        self.subject = subject
        self.teacher = teacher
        self.classroom = classroom
        self.classes = group
        self.period = period
        self.day = day

    def __str__(self):
        return self.subject.__str__()
