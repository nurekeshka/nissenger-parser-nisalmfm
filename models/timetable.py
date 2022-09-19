from models.parser import Parser
from utils import current_time
import pandas as pd


class Timetable(object):
    def __init__(self, parser: Parser, *args, **kwargs):
        self.parser = parser

        # self.initialize_table()

    def initialize_table(self):
        self.table = pd.DataFrame()

    def test(self):
        for lesson in self.parser.lessons:
            print(lesson)
            return

    def export_as_json(self):
        pass
