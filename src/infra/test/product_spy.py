from datetime import date
from typing import List
from uuid import uuid4

from src.data import StatusDTO
from src.domain.entity.product import Product
from src.domain.repository.product import ProductRepositoryInterface


class ProductRepositorySpy(ProductRepositoryInterface):
    """Spy to Product Repository"""

    def __init__(self):
        self.product_by_day_params = {}
        self.product_by_id_params = {}

    def insert_product(self, product: Product) -> None:
        day = product.day
        if day not in self.product_by_day_params:
            self.product_by_day_params[day] = [product]
        else:
            self.product_by_day_params[day].append(product)

        self.product_by_id_params[product.id] = product

    def products_in_a_day(self, day: date) -> int:
        if day in self.product_by_day_params:
            return len(self.product_by_day_params[day])
        return 0

    def select_products_grouped_by_day(self):
        return self.product_by_day_params

    def select_products_in_specific_day(self, day: date) -> List[Product]:
        return self.product_by_day_params.get(day, [])

    def update_product_status(self, id: uuid4, status: StatusDTO) -> None:
        if id in self.product_by_id_params:
            self.product_by_id_params[id].status = status

    def delete_product(self, id: uuid4) -> None:
        del self.product_by_id_params[id]
