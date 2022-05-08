from abc import ABC, abstractmethod
from datetime import date
from typing import List

from src.domain.entity import Product


class GetProductsByDayInterface(ABC):
    """Abstract method for get product by day use case"""

    @abstractmethod
    def get_products_by_day(
        self,
        day: date,
    ) -> List[Product]:
        raise Exception("Should implement method get_products_by_day")
