from constants import Links as links
from payloads import database_json
from payloads import lessons_json
from utils import current_time
from requests import Response
from requests import post
from typing import List
from typing import Dict
import json


class Loader(object):
    def __init__(self, filepath=None, *args, **kwargs):
        if filepath is None:
            self.loading_datetime: str = current_time()
            self.lessons: Dict[str, list] = dict()
            self.load_timetable_data()
            self.load_classes_lessons()
        else:
            with open(filepath, 'r') as file:
                data = json.loads(file.read())
                
                self.lessons = data['lessons']
                self.tables = data['data']
 
    def load_timetable_data(self):
        response = self.request_database().json()
        self.tables: List[dict] = response['r']['tables']

    def load_classes_lessons(self):
        classes: Dict[str, dict] = next(
            x for x in self.tables if x['id'] == 'classes')['data_rows']

        for _class in classes:
            self.load_class_lessons(_class['id'])

    def load_class_lessons(self, id):
        response = self.request_lessons(id).json()['r']['ttitems']
        self.lessons[id] = response

    def request_database(self) -> Response:
        return post(url=links.database.value,
                    json=database_json())

    def request_lessons(self, class_id) -> Response:
        return post(url=links.lessons.value,
                    json=lessons_json(class_id))

    def export(self):
        data = {
            'data': self.tables,
            'lessons': self.lessons
        }

        with open('data.json', 'w') as file:
            file.write(json.dumps(data))