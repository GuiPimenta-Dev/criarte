from datetime import date
from typing import Dict, List

from src.domain.entity.product import Product
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.use_cases.get_products import GetProductsByDayInterface
from src.domain.use_cases.get_week_days import WeekDaysInterface


class GetProductsByDay(GetProductsByDayInterface):
    def __init__(
        self,
        repository: ProductRepositoryInterface,
        week_days: WeekDaysInterface,
    ) -> None:
        self.__repository = repository
        self.week_days = week_days

    def select_products_grouped_by_day(self) -> List[Dict[str, Product]]:
        products_grouped_by_day = self.__repository.select_products_grouped_by_day()
        return self.week_days.get_products_by_week_day(products_grouped_by_day)

    def select_products_in_a_day(self, day: date) -> List[Product]:
        return self.__repository.select_products_in_specific_day(day=day)
