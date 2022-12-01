

class BasicException(BaseException):
    details = 'Something went wrong'

    def __init__(self):
        super(BasicException, self).__init__(self.details)


class TableTypeError(BaseException):
    details = 'AbstractDatabase.load() argument of method must be dictionary that contains str: AbstractTable'


class BaseMethodistError(BaseException):
    details = 'Methodist fucked up... again...'


class MoreThanOneResult(BaseMethodistError):
    details = 'Holy shit... Maybe methodist created several teachers with the same name again?'


class NothingFound(BaseException):
    details = 'Database didn\'t find anything'
