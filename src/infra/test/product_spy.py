from datetime import date
from typing import List

from src.domain.entities.product import Product
from src.domain.repository.product import ProductRepositoryInterface


class ProductRepositorySpy(ProductRepositoryInterface):
    """Spy to Product Repository"""

    def __init__(self):
        self.insert_product_by_day_params = {}
        self.insert_product_by_id_params = {}

    def insert_product(self, product: Product) -> None:
        day = product.day
        if day not in self.insert_product_by_day_params:
            self.insert_product_by_day_params[day] = [product]
        else:
            self.insert_product_by_day_params[day].append(product)

        self.insert_product_by_id_params[product.id] = product

    def is_day_limit_reached(self, day: date) -> bool:
        if day in self.insert_product_by_day_params:
            return len(self.insert_product_by_day_params[day]) >= 10
        return False

    def select_products_in_specific_day(self, day: date) -> List[Product]:
        return self.insert_product_by_day_params.get(day, [])
