import calendar
from datetime import datetime
from typing import Dict, List

from dateutil.relativedelta import relativedelta
from src.domain.entity.product import Product
from src.domain.use_cases.get_week_days import WeekDaysInterface

NUMBER_OF_PAST_MONTHS = 1
NUMBER_OF_NEXT_MONTHS = 4


class GetDays(WeekDaysInterface):
    def get_products_by_week_day(
        self, products_by_day: Dict[str, List[Product]]
    ) -> dict[str, dict[str, list]]:
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
            "monday": {"products" : [], "total":0},
            "tuesday": {"products" : [], "total":0},
            "wednesday": {"products" : [], "total":0},
            "thursday": {"products" : [], "total":0},
            "friday": {"products" : [], "total":0},
            "saturday": {"products" : [], "total":0},
            "sunday": {"products" : [], "total":0},
        }
        for week in month:
            for index, day in enumerate(week):
                match index:
                    case 0:
                        week_days["monday"]["products"].append({day: []})
                    case 1:
                        week_days["tuesday"]["products"].append({day: []})
                    case 2:
                        week_days["wednesday"]["products"].append({day: []})
                    case 3:
                        week_days["thursday"]["products"].append({day: []})
                    case 4:
                        week_days["friday"]["products"].append({day: []})
                    case 5:
                        week_days["saturday"]["products"].append({day: []})
                    case 6:
                        week_days["sunday"]["products"].append({day: []})
        return week_days

    @staticmethod
    def __insert_product_into_week_day(
        year_week_days,
        products_by_day: Dict[str, List[Product]],
    ):

        for date, products in products_by_day.items():
            date = datetime.strptime(str(date), "%Y-%m-%d")
            year_month, day = f"{date.year}-{date.month}", date.day
            if year_month in year_week_days:
                for week_day in year_week_days[year_month].values():
                    for i in week_day["products"]:
                        if day in i:
                            total = 0
                            for product in products:
                                total += product.price
                            i[day] = products
                            week_day["total"] = total

        return year_week_days
