'''
from database import Database
from sender import FmalmNisEdupageSender as Sender
from models import Timetable
from parser import FmalmNisEdupageDatabaseParser as Parser


def main():
    payload = Sender.request_database()
    database = Database.load(payload=payload, parser=DatabaseParser)

    timetable = Timetable()
    parser = LessonsParser()

    for subject in database.subjects:
        data = Sender.request_lessons(type=By.SUBJECT, payload=subject.id)

        for lesson_json in data:
            lesson = parser.format(lesson_json)
            timetable.add(lesson)

    timetable.export()
'''

import senders
import constants
import databases
import parsers
import entities
import requests


def bootstrap():
    sender = senders.DatabaseSender()
    sender.request()


def main():
    sender = senders.DatabaseSender()
    sender.request()

    database = databases.TimetableDatabase()
    database.timetable_load(sender.data)

    timetable = entities.Timetable()

    for subject in database['subjects']:
        sender = senders.LessonsSender()
        sender.request(id=subject.id, by=constants.By.SUBJECT)

        for lesson__json in sender.data:
            parser = parsers.LessonsParser()
            lessons = parser.format(
                data={'lesson': lesson__json, 'database': database})
            timetable.add(lessons)

    data = timetable.export()

    sender = senders.TimetableSender()
    sender.request(timetable=data)


if __name__ == '__main__':
    main()
