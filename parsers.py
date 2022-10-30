import settings
import entities
import datetime


class AbstractParser(object):
    fixes = None

    @classmethod
    def format(self, data: dict) -> str:
        kwargs = self.fix(data)
        return self.to_object(**kwargs)

    def fix(self, data: dict) -> dict:
        return data

    def to_object(self, **kwargs):
        return kwargs


class DictionaryFixesParser(AbstractParser):
    fixes: dict = None
    id: str = None
    name: str = None

    entity: entities.BaseEntity = None

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data[self.id]
        name = self.fixes[data[self.name]] if data[self.name] in self.fixes.keys(
        ) else data[self.name].lower().title()

        return {'id': id, 'name': name}

    @classmethod
    def to_object(self, id: str, name: str):
        return self.entity(id=id, name=name)


class TeachersParser(DictionaryFixesParser):
    fixes = settings.TEACHER_FIXES_DICTIONARY
    id = 'id'
    name = 'short'

    entity: entities.Teacher = entities.Teacher


class SubjectsParser(DictionaryFixesParser):
    fixes = settings.SUBJECT_FIXES_DICTIONARY
    id = 'id'
    name = 'name'

    entity: entities.Subject = entities.Subject


class ClassroomsParser(DictionaryFixesParser):
    fixes = settings.CLASSROOM_FIXES_DICTIONARY
    id = 'id'
    name = 'short'

    entity: entities.Classroom = entities.Classroom


class ClassesParser(AbstractParser):
    id = 'id'
    name = 'short'

    @classmethod
    def fix(self, data: dict):
        id = data['id']
        grade = int(data[self.name][:-1])
        letter = data[self.name][-1]

        return {'id': id, 'grade': grade, 'letter': letter}

    @classmethod
    def to_object(self, id: str, grade: int, letter: str):
        return entities.Class(id=id, grade=grade, letter=letter)


class PeriodParser(AbstractParser):
    id = 'id'
    period = 'period'
    starttime = 'starttime'
    endtime = 'endtime'

    @classmethod
    def fix(self, data: dict):
        data[self.period] = int(data[self.period])
        return data

    @classmethod
    def to_object(self, id: str, period: int, starttime: str, endtime: str):
        return entities.Period(id=id, number=period,
                               starttime=starttime, endtime=endtime)


class DaysParser(AbstractParser):
    date_format = '%Y-%m-%d'

    @classmethod
    def fix(self, data: str):
        day = datetime.datetime.strptime(data, self.date_format)
        number = day.isoweekday()
        name = settings.DAYS[number]

        return {'number': number, 'name': name}

    @classmethod
    def to_object(self, number: int, name: str):
        return entities.Day(number=number, name=name)
