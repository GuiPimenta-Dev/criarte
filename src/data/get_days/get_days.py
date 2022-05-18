import calendar
from datetime import datetime
from typing import Dict, List

from dateutil.relativedelta import relativedelta
from src.domain.entity.product import Product
from src.domain.use_cases.get_week_days import WeekDaysInterface

NUMBER_OF_PAST_MONTHS = 1
NUMBER_OF_NEXT_MONTHS = 13


class GetDays(WeekDaysInterface):
    def get_products_by_week_day(
        self, products_by_day: Dict[str, List[Product]]
    ) -> Dict[str, Dict[str, Dict[int, List[Product]]]]:
        year_week_days = self.__get_year_week_days()
        return self.__insert_product_into_week_day(
            year_week_days=year_week_days, products_by_day=products_by_day
        )

    def __get_year_week_days(self) -> Dict[str, Dict[str, List]]:
        results = {}
        for i in range(-NUMBER_OF_PAST_MONTHS, NUMBER_OF_NEXT_MONTHS):
            month_date = datetime.now() + relativedelta(months=i)
            year, month = month_date.year, month_date.month
            month_calendar = calendar.monthcalendar(year, month)
            week_days = self.__separate_into_week_days(month_calendar)
            results[f"{year}-{month}"] = week_days

        return results

    @staticmethod
    def __separate_into_week_days(month: List[List[int]]):
        week_days = {
            "monday": {},
            "tuesday": {},
            "wednesday": {},
            "thursday": {},
            "friday": {},
            "saturday": {},
            "sunday": {},
        }
        for week in month:
            for index, day in enumerate(week):
                match index:
                    case 0:
                        week_days["monday"][day] = []
                    case 1:
                        week_days["tuesday"][day] = []
                    case 2:
                        week_days["wednesday"][day] = []
                    case 3:
                        week_days["thursday"][day] = []
                    case 4:
                        week_days["friday"][day] = []
                    case 5:
                        week_days["saturday"][day] = []
                    case 6:
                        week_days["sunday"][day] = []
        return week_days

    @staticmethod
    def __insert_product_into_week_day(
        year_week_days: Dict[str, Dict[str, List]],
        products_by_day: Dict[str, List[Product]],
    ):

        for date, products in products_by_day.items():
            date = datetime.strptime(str(date), "%Y-%m-%d")
            year_month, day = f"{date.year}-{date.month}", date.day
            if year_month in year_week_days:
                for week_day in year_week_days[year_month].values():
                    if day in week_day:
                        week_day[day] = products
        return year_week_days
