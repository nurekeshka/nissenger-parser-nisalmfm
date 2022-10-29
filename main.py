'''
from database import Database
from sender import FmalmNisEdupageSender as Sender
from models import Timetable
from parser import FmalmNisEdupageDatabaseParser as Parser
'''


def main():
    '''
    payload = Sender.request_database()
    database = Database.load(payload=payload, parser=DatabaseParser)

    timetable = Timetable()
    parser = LessonsParser()

    for subject in database.subjects:
        data = Sender.request_lessons(type=By.SUBJECT, payload=subject.id)

        for lesson_json in data:
            lesson = parser.json_to_object(lesson_json)
            timetable.add(lesson)

    timetable.export()
    '''


if __name__ == '__main__':
    main()
