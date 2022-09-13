from constants import EdupageMainDbIDs as indexes
from constants import FIELDS as fields
from datetime import datetime
from typing import Dict
from typing import List
import json


class Timetable(object):
    def __init__(self, data: List[list], *args, **kwargs):
        self.datetime: datetime = datetime.now()

        self.teachers: List[str] = list()
        self.subjects: List[str] = list()
        self.periods: List[dict] = list()
        self.offices: List[str] = list()
        self.classes: List[dict] = list()

        self.set_data(data)


    def __str__(self) -> str:
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S')


    def set_data(self, data: List[dict]):
        self.add_teachers(data[indexes.teachers.value])
        self.add_offices(data[indexes.classrooms.value])
        self.add_subjects(data[indexes.subjects.value])
        self.add_classes(data[indexes.classes.value])
        self.add_periods(data[indexes.periods.value])


    def add_teachers(self, teachers: List[str]):
        for teacher in teachers:
            self.teachers.append(teacher)


    def add_subjects(self, subjects: List[str]):
        for subject in subjects:
            self.subjects.append(subject)


    def add_offices(self, offices: List[str]):
        for office in offices:
            self.offices.append(office)
    

    def add_classes(self, classes: List[dict]):
        for _class in classes:
            self.classes.append(_class)

    
    def add_periods(self, periods: List[dict]):
        for period in periods:
            self.periods.append(period)


class Export(object):
    def __init__(self, timetable: Timetable, *args, **kwargs):
        self.timetable: Timetable = timetable

    
    def _create_empty_data(self) -> Dict[str, List]:
        data: Dict[str, List] = dict()

        for field in fields:
            data[field] = list()

        return data


    def as_json(self) -> str:
        data: Dict[str, List] = self._create_empty_data()

        for teacher in self.timetable.teachers:
            data['teachers'].append(teacher)

        for subject in self.timetable.subjects:
            data['subjects'].append(subject)
        
        for period in self.timetable.periods:
            data['periods'].append(period)
        
        for _class in self.timetable.classes:
            data['classes'].append(_class)
        
        for office in self.timetable.offices:
            data['offices'].append(office)

        # data = json.dumps(data)
        return data


if __name__ == '__main__':
    teachers = ['Nurbek' for _ in range(5)]

    timetable = Timetable()
    timetable.add_teachers(teachers)

    export = Export(timetable)
    result = export.as_json()
    print(result)
