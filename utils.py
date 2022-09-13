from datetime import timedelta
from datetime import datetime
from datetime import date
from typing import Tuple


def school_year() -> int:
    today = date.today()
    return today.year if today.month in range(9, 13) else today.year - 1


def current_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def current_week() -> Tuple[str]:
    today: date = date.today()
    weekday: int = today.weekday()

    firstday: date = today - timedelta(days=weekday)
    lastday: date = firstday + timedelta(days=6)

    return tuple( map( lambda day: day.strftime('%Y-%m-%d'), ( firstday, lastday ) ) )
