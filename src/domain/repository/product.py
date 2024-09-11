from abc import ABC, abstractmethod
from datetime import date
from typing import Dict, List
from uuid import uuid4

from src.data import StatusDTO
from src.domain.entity.product import Product


class ProductRepositoryInterface(ABC):
    """Abstract method for domain product repository"""

    @abstractmethod
    def insert_product(self, product: Product) -> None:
        raise Exception("Should implement method insert_product")

    @abstractmethod
    def select_products_grouped_by_day(self) -> List[Dict[str, Product]]:
        raise Exception("Should implement method select_products_grouped_by_day")

    @abstractmethod
    def select_products_in_specific_day(self, day: str) -> List[Product]:
        raise Exception("Should implement method select_products_in_specific_day")

    @abstractmethod
    def products_in_a_day(self, day: date) -> int:
        raise Exception("Should implement method products_in_a_day")

    @abstractmethod
    def update_product_status(self, id: uuid4, status: StatusDTO) -> None:
        raise Exception("Should implement method update_product_status")

    @abstractmethod
    def delete_product(self, id: uuid4) -> None:
        raise Exception("Should implement method delete_product")
