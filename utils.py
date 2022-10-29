from datetime import date, timedelta
from typing import Tuple


def get_week() -> Tuple[str]:
    today: date = date.today()
    weekday: int = today.weekday()

    firstday: date = today - timedelta(days=weekday)
    lastday: date = firstday + timedelta(days=6)

    return tuple(map(lambda day: day.strftime('%Y-%m-%d'), (firstday, lastday)))


def get_school_year() -> int:
    today = date.today()
    return today.year if today.month in range(9, 13) else today.year - 1
