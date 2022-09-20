from enum import Enum


class Links(Enum):
    database = 'https://fmalmnis.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'
    lessons = 'https://fmalmnis.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'


class Indexes(Enum):
    teachers = 0
    subjects = 1
    classrooms = 2
    classes = 3
    periods = 4

    uniperiod = 'uniperiod'
    starttime = 'starttime'
    endtime = 'endtime'

    subjectid = 'subjectid'
    teacherids = 'teacherids'
    classids = 'classids'
    classroomids = 'classroomids'
    durationperiods = 'durationperiods'

    id = 'id'
    data_rows = 'data_rows'
    short = 'short'
    name = 'name'
    period = 'period'


class TableHeaders(Enum):
    teachers = 'TEACHERS'
    classes = 'CLASSES'
    classrooms = 'CLASSROOMS'
    subjects = 'SUBJECTS'
    periods = 'PERIODS'


TEACHER_CHANGES = {
    '?міртай Э. Т.': 'Әміртай Э. Т.',
    'К': 'Куратор',
    'С?лтан Р. М.': 'Сұлтан Р. М.',
    'У': 'Учитель',
    'У?лихан А.': 'Уәлихан А.',
    'Н?рма?амбет Д.': 'Нұрмағамбет Д.',
    'АА': 'Химик',
    'ББ': 'Куратор',
    'В': 'Физик',
    'А': 'Асель',
    'ДТ': 'Биолог',
}


CLASSROOM_CHANGES = {
    'МСЗ': 'Малый Спорт Зал',
    'СЗ': 'Спорт Зал',
}

SUBJECT_CHANGES = {
    'SAT Eng': 'SAT English',
    'Человек. Общество. Право (Основы права)': 'Основы права',
    'Начальная военная и технологическая подготовка': 'НВП',
    "Русский язык и литература": "Русский",
    "Русская литература": "Русская литература",
    "Русский язык": "Русский",
    "Казахский язык": "Казахский",
    "Казахская литература": "Казахская литература",
    "Казахский язык и литература": "Казахский",
    "Английский язык": "Английский",
    "Мат PISA": "Математика PISA",
    "Каз PISA": "Казахский PISA",
    "Рус PISA": "Русский PISA",
    "Физика ВСО/PISA": "Физика ВСО",
    "Казахский язык ВСО": "Казахский ВСО",
    "Информатика ВСО/PISA": "Информатика ВСО",
    "Химия ВСО/PISA": "Химия ВСО",
    "Биология ВСО/PISA": "Биология ВСО",
    "Русский язык ВСО": "Русский ВСО",
    "Химия(Углубленная)": "Химия",
    "Биология(Углубленная)": "Биология",
    "Информатика(Углубленная)": "Информатика",
    "Физика(Углубленная)": "Физика",
    "География(Стандартная)": "География",
    "Экономика(Стандартная)": "Экономика",
    "Графика и проектирование(Стандартная)": "ГИП",
    "Математика(7)": "Математика",
    "Математика(10)": "Математика (10)",
    "Програм.": "Программирование",
    "История Казахстана (Казахстан в современном мире)": "КСМ",
    "Физика Доп.": "Физика Доп",
    "Физическая культура": "Физ-ра",
    "Глобальные перспективы и проектные работы": "GPPW",
    "Начальная военная и технологическая подготовка": "НВП",
    "Человек. Общество. Право (Основы права)": "Основы Права",
}


DAYS = (
    'monday',
    'tuesday',
    'weekday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
)
