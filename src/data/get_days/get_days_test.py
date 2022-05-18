from datetime import datetime

from src.data.get_days import GetDays

YEAR = datetime.now().year
MONTH = datetime.now().month

get_days_use_case = GetDays()


def test_get_calendar_days_this_year():

    result = get_days_use_case.get_days()
    print(result)
