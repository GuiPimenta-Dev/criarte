from datetime import date
from uuid import uuid4

from domain.entity.product import Product
from domain.repository.product import ProductRepositoryInterface
from domain.usecases import RegisterProductInterface


class RegisterProduct(RegisterProductInterface):
    """Class to register product use case"""

    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def register(
        self,
        name: str,
        client: str,
        observations: str,
        day: date,
    ) -> None:
        if self.__repository.is_day_limit_reached(day=day):
            raise Exception("Day limit exceeded")

        product = Product(
            id=uuid4(), name=name, client=client, observations=observations, day=day
        )

        self.__repository.insert_product(
            id=product.id,
            name=product.name,
            client=product.client,
            completed=product.completed,
            observations=product.observations,
            day=product.day,
        )

        return product
