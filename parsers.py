import settings
import entities


class AbstractParser(object):
    fixes = None

    def format(data):
        return data


class DictionaryFixesParser(AbstractParser):
    fixes: dict = None
    id: str = None
    name: str = None

    entity: entities.BaseEntity = None

    @classmethod
    def format(self, data: dict) -> str:
        kwargs = self.fix(data)
        return self.to_object(**kwargs)

    @classmethod
    def fix(self, data: dict) -> dict:
        id = data[self.id]
        name = self.fixes[data[self.name]] if data[self.name] in self.fixes.keys(
        ) else data[self.name].lower().title()

        return {'id': id, 'name': name}

    @classmethod
    def to_object(self, id: str, name: str):
        return self.entity(id=id, name=name)


class TeachersParser(DictionaryFixesParser):
    fixes = settings.TEACHER_FIXES_DICTIONARY
    id = 'id'
    name = 'short'

    entity: entities.Teacher = entities.Teacher
