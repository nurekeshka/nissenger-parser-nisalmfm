import datetime
from typing import List

import entities
import exceptions
import settings


class AbstractParser:
    fixes = None

    @classmethod
    def format(self, data: dict) -> object:
        kwargs = self.fix(data)
        return self.to_object(**kwargs)

    def fix(self, data: dict) -> dict:
        return data

    def to_object(self, **kwargs):
        return kwargs


class DictionaryFixesParser(AbstractParser):
    fixes: dict = None
    id: str = None
    name: str = None

    entity: entities.BaseEntity = None

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data[self.id]
        name = (
            self.fixes[data[self.name]]
            if data[self.name] in self.fixes.keys()
            else data[self.name].lower().title()
        )

        return {"id": id, "name": name}

    @classmethod
    def to_object(self, id: str, name: str) -> entity:
        return self.entity(id=id, name=name)


class TeachersParser(DictionaryFixesParser):
    fixes = settings.TEACHER_FIXES_DICTIONARY
    id = "id"
    name = "short"
    firstname = "firstname"
    lastname = "lastname"

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data[self.id]
        name = f"{data[self.lastname]} {data[self.firstname]}"

        name = self.fixes[name] if name in self.fixes.keys() else name.lower().title()

        return {"id": id, "name": name}

    entity: entities.Teacher = entities.Teacher


class SubjectsParser(DictionaryFixesParser):
    fixes = settings.SUBJECT_FIXES_DICTIONARY
    id = "id"
    name = "name"

    entity: entities.Subject = entities.Subject

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data[self.id]
        name = (
            self.fixes[data[self.name]]
            if data[self.name] in self.fixes.keys()
            else data[self.name].lower().title()
        )

        type = settings.SUBJECT_TYPES[data[self.name]]

        return {"id": id, "name": name, "type": type}

    @classmethod
    def to_object(self, id: str, name: str, type: str) -> entity:
        return self.entity(id=id, name=name, type=type)


class ClassroomsParser(DictionaryFixesParser):
    fixes = settings.CLASSROOM_FIXES_DICTIONARY
    id = "id"
    name = "short"

    entity: entities.Classroom = entities.Classroom


class ClassesParser(AbstractParser):
    id = "id"
    name = "short"

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data["id"]
        grade = int(data[self.name][:-1])
        letter = data[self.name][-1]

        return {"id": id, "grade": grade, "letter": letter}

    @classmethod
    def to_object(self, id: str, grade: int, letter: str) -> entities.Class:
        return entities.Class(id=id, grade=grade, letter=letter)


class PeriodParser(AbstractParser):
    id = "id"
    period = "period"
    starttime = "starttime"
    endtime = "endtime"

    @classmethod
    def fix(self, data: dict) -> dict:
        data[self.period] = int(data[self.period])
        return data

    @classmethod
    def to_object(
        self, id: str, period: int, starttime: str, endtime: str
    ) -> entities.Period:
        return entities.Period(
            id=id, number=period, starttime=starttime, endtime=endtime
        )


class DaysParser(AbstractParser):
    date_format = "%Y-%m-%d"

    @classmethod
    def fix(self, data: str) -> dict:
        day = datetime.datetime.strptime(data, self.date_format)
        number = day.isoweekday()
        name = settings.DAYS[number]

        return {"number": number, "name": name}

    @classmethod
    def to_object(self, number: int, name: str) -> entities.Day:
        return entities.Day(number=number, name=name)


class LessonsParser(AbstractParser):
    # Returns: { 'lessons': [{'subject': entities.Subject, 'teacher': entities.Teacher, ...}, {...}}, {...}] }
    @classmethod
    def format(self, data: dict) -> entities.Lesson:
        kwargs = data["lesson"]
        kwargs["database"] = data["database"]

        try:
            lessons = self.fix(**kwargs)

            if lessons is None:
                return

            return self.to_object(lessons)
        except Exception as e:
            print(e)
            raise exceptions.InformingException(**kwargs)

    @classmethod
    def fix(
        self,
        database,
        date: str,
        uniperiod: str,
        classroomids: List[str],
        starttime: str,
        endtime: str,
        groupnames: List[str],
        teacherids: List[str],
        subjectid: str,
        classids: List[str],
        name: str = None,
        eventid: str = None,
        studentids: List[str] = None,
        igroupid: str = None,
        type: str = None,
        durationperiods: int = 1,
        cellSlices: str = None,
        cellOrder: int = None,
    ):
        if type != "card":
            return

        lessons = list()

        subject: entities.Subject = database["subjects"][f"id={subjectid}"]

        try:
            teachers = [
                database["teachers"][f"id={teacherid}"] for teacherid in teacherids
            ]
        except exceptions.NothingFound:
            teachers = [entities.Teacher(id=teacherids[0], name=teacherids[0])]

        classrooms = [
            database["classrooms"][f"id={classroomid}"] for classroomid in classroomids
        ]

        day = DaysParser().format(date)

        classes: List[entities.Class] = [
            database["classes"][f"id={classid}"] for classid in classids
        ]

        # Doubled lessons for both groups
        if groupnames[0] == "" and len(classes) == 1:
            groups = [
                entities.Group(name=str(number), classes=classes) for number in (1, 2)
            ]
        # IELTS for several classes
        elif groupnames[0] == "" and len(classes) > 1:
            groups = [entities.Group(name=subject.name, classes=classes)]
        # Casual subjects and profile directed
        else:
            groups = [
                entities.Group(
                    name=self.try_extract_group_number(groupnames[0]), classes=classes
                )
            ]

        periods = [
            database["periods"][f"number={x}"]
            for x in range(int(uniperiod), int(uniperiod) + durationperiods)
        ]

        for period in periods:
            for group in groups:
                lesson = dict()

                lesson["subject"] = subject
                lesson["teacher"] = teachers[0]
                lesson["classroom"] = (
                    classrooms[0]
                    if len(classrooms) == 1
                    else entities.Classroom(id="-100", name="")
                )
                lesson["group"] = group
                lesson["period"] = period
                lesson["day"] = day

                lessons.append(lesson)

        return lessons

    @classmethod
    def to_object(self, lessons: List[dict]) -> List[entities.Lesson]:
        return [
            entities.Lesson(
                subject=lesson["subject"],
                teacher=lesson["teacher"],
                classroom=lesson["classroom"],
                group=lesson["group"],
                period=lesson["period"],
                day=lesson["day"],
            )
            for lesson in lessons
        ]

    @classmethod
    def try_extract_group_number(self, name: str) -> int:
        for ch in name.split():
            if ch.isdigit():
                return int(ch)

        return name
