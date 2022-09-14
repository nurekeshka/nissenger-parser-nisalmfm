from typing import Tuple


class Teacher(object):
    changes = {
        '?міртай Э. Т.': 'Әміртай Э. Т.',
        'К': 'Куратор',
        'С?лтан Р. М.': 'Сұлтан Р. М.',
        'У': 'Учитель',
        'У?лихан А.': 'Уәлихан А.',
    }

    def __init__(self, name: str):
        self.name = name
        self._parse_name()

    def _parse_name(self):
        if self.name in self.changes:
            self.name = self.changes[self.name]
        else:
            self.name = str(self.name).lower().title()

    def __str__(self):
        return self.name


class Period(object):
    def __init__(self, number: int, starttime: str, endtime: str):
        self.number = int(number)
        self.starttime = starttime
        self.endtime = endtime

    def __str__(self):
        return f'{self.starttime} | {self.endtime}'


class Subject(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Classroom(object):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Class(object):
    def __init__(self, name: str):
        self.grade = int(name[:-1])
        self.letter = name[-1]

    def __str__(self):
        return f'{self.grade}{self.letter}'


class Lesson(object):
    def __init__(self, subject: Subject, period: Period, teacher: Teacher, classroom: Classroom, classes: Tuple[Class], duration: int):
        self.subject = subject
        self.period = period
        self.teacher = teacher
        self.classroom = classroom
        self.classes = classes
        self.duration = duration

    def __str__(self):
        return '\n'.join([
            f'{self.subject}',
            f'{self.period}',
            f'{self.classroom}',
            f'{self.teacher}',
            f'{", ".join(map(str, self.classes))}',
        ])
