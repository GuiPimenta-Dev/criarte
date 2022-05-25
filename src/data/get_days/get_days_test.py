import calendar
from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from src.data.get_days import GetDays

FIRST_MONTH = 1
LAST_MONTH = 3


def test_calendar_days_with_products(product):
    today = date.today()
    today_weekday = calendar.day_name[today.weekday()].lower()
    today_string = datetime.now().strftime("%Y-%m-%d")
    today_year_month = f"{today.year}-{today.month}"

    first_date = datetime.now() + relativedelta(months=-FIRST_MONTH)
    first_date_year_month = f"{first_date.year}-{first_date.month}"

    last_date = datetime.now() + relativedelta(months=LAST_MONTH)
    last_date_year_month = f"{last_date.year}-{last_date.month}"

    week_days = GetDays().get_products_by_week_day({today_string: [product]})

    assert week_days[first_date_year_month]
    assert week_days[today_year_month][today_weekday] != []
    assert week_days[last_date_year_month]
