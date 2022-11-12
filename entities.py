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
            attr) and not attr.startswith('_') and not attr in ('getattributes', 'id')]

    def __json__(self) -> dict:
        return {attribute: getattr(self, attribute) for attribute in self.getattributes()}


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

    def __json__(self) -> dict:
        return {'name': self.name, 'classes': [_class.__json__() for _class in self.classes]}


class Lesson(BaseEntity):
    def __init__(self, subject: Subject, teacher: Teacher, classroom: Classroom, group: Group, period: Period, day: Day):
        self.subject = subject
        self.teacher = teacher
        self.classroom = classroom
        self.group = group
        self.period = period
        self.day = day

    def __str__(self):
        return self.subject.__str__()

    def __json__(self) -> dict:
        return {attribute: getattr(self, attribute).__json__() for attribute in self.getattributes()}


class Timetable(BaseEntity):
    def __init__(self):
        self.lessons = list()

    def add(self, lessons: List[Lesson]):
        self.lessons.extend(lessons)

    def export(self) -> dict:
        return [lesson.__json__() for lesson in self.lessons]
