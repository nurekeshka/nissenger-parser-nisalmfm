

class BasicException(BaseException):
    details = 'Something went wrong'

    def __init__(self):
        super(BasicException, self).__init__(self.details)


class TableTypeError(BasicException):
    details = 'AbstractDatabase.load() argument of method must be dictionary that contains str: AbstractTable'


class BaseMethodistError(BasicException):
    details = 'Methodist fucked up... again...'


class MoreThanOneResult(BaseMethodistError):
    details = 'Holy shit... Maybe methodist created several teachers with the same name again?'


class NothingFound(BaseException):
    details = 'Database didn\'t find anything. Query input: {0}\nTable type: {1}'

    def __init__(self, query__input: str, table__type: object):
        super(NothingFound, self).__init__(
            self.details.format(query__input, type(table__type)))


class InformingException(BaseException):
    def __init__(self, **kwargs):
        details = '\n'
        details += '\n'.join(
            map(lambda pair: f'{pair[0]}={pair[1]}', kwargs.items()))
        super(InformingException, self).__init__(details)
