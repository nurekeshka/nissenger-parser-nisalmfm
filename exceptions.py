

class TableTypeError(TypeError):
    def __init__(self):
        super(TableTypeError, self).__init__(
            'AbstractDatabase.load() argument of method must be dictionary that contains str: AbstractTable')


class BaseMethodistError(Exception):
    details = 'Methodist fucked up... again...'

    def __init__(self):
        super(BaseMethodistError, self).__init__(self.details)


class MoreThanOneResult(BaseMethodistError):
    details = 'Holy shit... Maybe he created several teachers with the same name?'
