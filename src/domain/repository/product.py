from abc import ABC, abstractmethod
from datetime import date
from typing import List
from uuid import uuid4

from src.data import StatusDTO
from src.domain.entity.product import Product


class ProductRepositoryInterface(ABC):
    """Abstract method for domain product repository"""

    @abstractmethod
    def insert_product(self, product: Product) -> None:
        raise Exception("Should implement method insert_product")

    @abstractmethod
    def select_products_in_specific_day(self, day: str) -> List[Product]:
        raise Exception("Should implement method select_products_in_specific_day")

    @abstractmethod
    def is_day_limit_reached(self, day: date) -> bool:
        raise Exception("Should implement method is_day_limit_reached")

    @abstractmethod
    def update_product_status(self, id: uuid4, status: StatusDTO) -> bool:
        raise Exception("Should implement method update_product_status")
