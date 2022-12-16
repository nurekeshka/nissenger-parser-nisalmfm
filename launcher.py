import senders
import constants
import databases
import parsers
import entities
import os


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
    with open('timetable.txt', 'w', encoding='utf-8') as file:
        print(data, file=file)

    try:
        current_version = open('data.txt', 'r', encoding='utf-8')
        resent_version = open('timetable.txt', 'r', encoding='utf-8')

        timetable_is_the_same = current_version.read() == resent_version.read()

        current_version.close()
        resent_version.close()

        if timetable_is_the_same:
            os.remove('./timetable.txt')
            return
        else:
            os.remove('./data.txt')
            os.rename('./timetable.txt', './data.txt')
    except FileNotFoundError:
        os.rename('./timetable.txt', './data.txt')

    sender = senders.TimetableSender()
    sender.request(timetable=data)

    return sender.response


if __name__ == '__main__':
    main()
