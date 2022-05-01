from datetime import date
from typing import List

from src.domain.entities.product import Product
from src.domain.repository.product import ProductRepositoryInterface


class ProductRepositorySpy(ProductRepositoryInterface):
    """Spy to Product Repository"""

    def __init__(self):
        self.insert_product_params = {}

    def insert_product(self, product: Product) -> None:
        day = product.day
        if day not in self.insert_product_params:
            self.insert_product_params[day] = [product]
        else:
            self.insert_product_params[day].append(product)

    def is_day_limit_reached(self, day: date) -> bool:
        if day in self.insert_product_params:
            return len(self.insert_product_params[day]) >= 10
        return False

    def select_products_in_specific_day(self, day: date) -> List[Product]:
        return self.insert_product_params.get(day, [])
