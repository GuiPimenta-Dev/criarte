import calendar
import datetime
from typing import Dict, List

from dateutil.relativedelta import relativedelta
from src.domain.use_cases.get_days import GetDaysInterface

NOW = datetime.datetime.now()
NUMBER_OF_PAST_MONTHS = 2
NUMBER_OF_NEXT_MONTHS = 13


class GetDays(GetDaysInterface):
    def get_days(self) -> Dict[str, Dict[str, int]]:

        results = {}
        for i in range(-NUMBER_OF_PAST_MONTHS, NUMBER_OF_NEXT_MONTHS):
            month_date = NOW + relativedelta(months=i)
            year, month = month_date.year, month_date.month
            month_calendar = calendar.monthcalendar(year, month)
            week_days = self.separate_into_week_days(month_calendar)
            results[f"{year}-{month}"] = week_days

        return results

    @staticmethod
    def separate_into_week_days(month: List[List[int]]):
        week_days = {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": [],
        }
        for week in month:
            for index, day in enumerate(week):
                match index:
                    case 0:
                        week_days["monday"].append(day)
                    case 1:
                        week_days["tuesday"].append(day)
                    case 2:
                        week_days["wednesday"].append(day)
                    case 3:
                        week_days["thursday"].append(day)
                    case 4:
                        week_days["friday"].append(day)
                    case 5:
                        week_days["saturday"].append(day)
                    case 6:
                        week_days["sunday"].append(day)
        return week_days
