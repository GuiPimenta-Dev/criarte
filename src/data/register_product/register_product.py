from uuid import uuid4

from src.data import ProductDTO
from src.domain.entity.product import Product
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.usecases import RegisterProductInterface


class RegisterProduct(RegisterProductInterface):
    """Class to register product use case"""

    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def register_product(self, product: ProductDTO) -> None:
        if self.__repository.is_day_limit_reached(day=product.day):
            raise Exception("Day limit exceeded")

        product = Product(
            id=uuid4(),
            type=product.type,
            printed_name=product.printed_name,
            theme=product.theme,
            price=product.price,
            sex=product.sex,
            payment=product.payment,
            day=product.day,
            client=product.client,
        )

        self.__repository.insert_product(product=product)

        return product
