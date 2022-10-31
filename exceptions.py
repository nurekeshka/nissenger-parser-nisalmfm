

class TableTypeError(TypeError):
    def __init__(self):
        super(TableTypeError, self).__init__(
            'AbstractDatabase.load() argument of method must be dictionary that contains str: AbstractTable')
