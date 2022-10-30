import entities
import parsers
from typing import List


class AbstractTable(object):
    def __init__(self, data: dict | list, parser: parsers.AbstractParser):
        self.data: List[entities.BaseEntity] = data
        self.parser: parsers.AbstractParser = parser

    def format(self):
        for i in range(len(self.data)):
            self.data[i] = self.parser.format(self.data[i])

    def __getitem__(self, key: str):
        if key.startswith('id='):
            for i in range(len(self.data)):
                if key.split('=')[1] == self.data[i].id:
                    return self.data[i]

        return None

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


if __name__ == '__main__':
    pass
