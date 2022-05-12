from abc import ABC, abstractmethod
from datetime import date
from typing import List

from src.domain.entity import Product


class GetProductsByDayInterface(ABC):
    """Abstract method for get product by day use case"""

    @abstractmethod
    def select_products_grouped_by_day(self) -> List[Product]:
        raise Exception("Should implement method select_products_grouped_by_day")

    @abstractmethod
    def select_products_in_a_day(
        self,
        day: date,
    ) -> List[Product]:
        raise Exception("Should implement method select_products_in_a_day")
