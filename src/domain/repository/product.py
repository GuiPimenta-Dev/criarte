from abc import ABC, abstractmethod
from datetime import date
from typing import List

from domain.entity.product import Product


class ProductRepositoryInterface(ABC):
    """Abstract method for domain product repository"""

    @abstractmethod
    def insert_product(
        self,
        id: str,
        name: str,
        client: str,
        completed: bool,
        observations: str,
        day: date,
    ) -> None:
        raise Exception("Should implement method insert_product")

    @abstractmethod
    def select_product(self, id: str) -> Product:
        raise Exception("Should implement method select_product")

    @abstractmethod
    def select_products_in_specific_day(self, day: str) -> List[Product]:
        raise Exception("Should implement method select_products_in_specific_day")

    @abstractmethod
    def is_day_limit_reached(self, day: date) -> bool:
        raise Exception("Should implement method is_day_limit_reached")
