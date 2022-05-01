from datetime import date
from typing import List

from src.domain.entities.product import Product
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.usecases.get_products_by_day import GetProductsByDayInterface


class GetProductsByDay(GetProductsByDayInterface):
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def get_products_by_day(self, day: date) -> List[Product]:
        return self.__repository.select_products_in_specific_day(day=day)
