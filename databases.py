import entities
import parsers
from typing import Dict, List
import exceptions


class AbstractTable(object):
    def __init__(self, data: dict | list, parser: parsers.AbstractParser = None):
        self.data: List[entities.BaseEntity] = data
        self.parser: parsers.AbstractParser = parser

        if self.parser:
            self.format()

    def format(self):
        for i in range(len(self.data)):
            self.data[i] = self.parser.format(self.data[i])

    def __getitem__(self, key: str):
        try:
            attribute, value = key.split('=')

            for i in range(len(self.data)):
                if value == str(getattr(self.data[i], attribute)):
                    return self.data[i]
        except TypeError:
            pass

        return self.data[i]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            index = self.index
            self.index += 1
            return self.data[index]
        else:
            raise StopIteration

    def __str__(self):
        return str(self.data)


class TeachersTable(AbstractTable):
    def __init__(self, data: dict | list):
        super(TeachersTable, self).__init__(
            data=data, parser=parsers.TeachersParser)


class SubjectsTable(AbstractTable):
    def __init__(self, data: dict | list):
        super(SubjectsTable, self).__init__(
            data=data, parser=parsers.SubjectsParser)


class ClassroomsTable(AbstractTable):
    def __init__(self, data: dict | list):
        super(ClassroomsTable, self).__init__(
            data=data, parser=parsers.ClassroomsParser)


class ClassesTable(AbstractTable):
    def __init__(self, data: dict | list):
        super(ClassesTable, self).__init__(
            data=data, parser=parsers.ClassesParser)


class PeriodsTable(AbstractTable):
    def __init__(self, data: dict | list):
        super(PeriodsTable, self).__init__(
            data=data, parser=parsers.PeriodParser)


class AbstractDatabase(object):
    def __init__(self):
        self.database: dict = dict()

    def load(self, data: Dict[str, AbstractTable]):
        if type(data) is dict:
            for key, table in data.items():
                if isinstance(table, AbstractTable):
                    self.database[key] = table
                else:
                    raise exceptions.TableTypeError()
        else:
            raise exceptions.TableTypeError()

    def __getitem__(self, key: int):
        return self.database[key]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.database):
            index = self.index
            self.index += 1
            return self.database[index]
        else:
            raise StopIteration

    def __str__(self):
        return '\n'.join(map(lambda table: f'{table[0]}: {table[1]}', self.database.items()))


class TimetableDatabase(AbstractDatabase):
    tables: Dict[str, AbstractTable] = {
        'teachers': TeachersTable,
        'subjects': SubjectsTable,
        'classrooms': ClassroomsTable,
        'classes': ClassesTable,
        'periods': PeriodsTable,
    }

    def timetable_load(self, data: Dict[str, dict]):
        self.load({name: table(data[name])
                  for name, table in self.tables.items()})
