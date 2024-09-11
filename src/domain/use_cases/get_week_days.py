from abc import ABC, abstractmethod
from typing import Dict


class WeekDaysInterface(ABC):
    """Abstract method for get days use case"""

    @abstractmethod
    def get_products_by_week_day(self, days) -> Dict[str, Dict[str, int]]:
        raise Exception("Should implement method get_products_by_week_day")
