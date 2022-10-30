

class BaseEntity(object):
    def __init__(self, id: str, name: str):
        self.id: str = id
        self.name: str = name

    def __str__(self):
        return self.name


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
    def __init__(self, number: int, starttime: str, endtime: str):
        self.number: int = int(number)
        self.starttime: str = starttime
        self.endtime: str = endtime

    def __str__(self):
        return f'{self.starttime} - {self.endtime}'


class Day(BaseEntity):
    def __init__(self, number: int, name: str):
        self.number = int(number)
        self.name = name
