from datetime import timedelta
from datetime import date
from typing import Tuple
from config import YEAR


def get_current_year() -> int:
    return YEAR if YEAR is not None else date.today().year


def get_current_week() -> Tuple[str]:
    today: date = date.today()
    weekday: int = today.weekday()

    firstday: date = today - timedelta(days=weekday)
    lastday: date = firstday + timedelta(days=6)

    return tuple( map( lambda day: day.strftime('%Y-%m-%d'), ( firstday, lastday ) ) )
