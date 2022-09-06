from datetime import date
from config import YEAR


def get_current_year() -> int:
    return YEAR if YEAR is not None else date.today().year
