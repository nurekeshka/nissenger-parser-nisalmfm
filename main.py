import senders
import constants
import databases
import parsers
import entities
import time


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
    print(sender.response.status_code)
    print(sender.response.json())


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
