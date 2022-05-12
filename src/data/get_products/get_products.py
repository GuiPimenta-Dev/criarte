from datetime import date
from typing import Dict, List

from src.domain.entity.product import Product
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.use_cases.get_products import GetProductsByDayInterface


class GetProductsByDay(GetProductsByDayInterface):
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def select_products_grouped_by_day(self) -> List[Dict[str, Product]]:
        return self.__repository.select_products_grouped_by_day()

    def select_products_in_a_day(self, day: date) -> List[Product]:
        return self.__repository.select_products_in_specific_day(day=day)
