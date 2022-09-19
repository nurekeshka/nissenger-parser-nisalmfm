from models.timetable import Timetable
from models.parser import Parser
from models.loader import Loader


def export_backup():
    loader = Loader()
    loader.export()


def main():
    loader = Loader('data.json')
    parser = Parser(loader)
    timetable = Timetable(parser)
    timetable.export_as_json()


if __name__ == '__main__':
    main()
