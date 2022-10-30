import parsers


class AbstractTable(object):
    def __init__(self, data: dict | list, parser: parsers.AbstractParser):
        self.data = data
        self.parser: parsers.AbstractParser = parser

    def format(self):
        for i in range(len(self.data)):
            self.data[i] = self.parser.format(self.data[i])

    def __getitem__(self, key: str):
        return self.data[key]

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


if __name__ == '__main__':
    pass
