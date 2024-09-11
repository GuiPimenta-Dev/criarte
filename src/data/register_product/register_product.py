from uuid import uuid4

from src.data import ProductDTO
from src.domain.entity.product import Product
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.use_cases import RegisterProductInterface
from src.errors import CustomError

MAX_DAY_CAPACITY = 10


class RegisterProduct(RegisterProductInterface):
    """Class to register product use case"""

    def __init__(self, repository: ProductRepositoryInterface) -> Product:
        self.__repository = repository

    def register_product(self, product: ProductDTO) -> None:
        """Register product concrete method"""

        products_in_day = self.__repository.products_in_a_day(day=product.day)

        if products_in_day >= MAX_DAY_CAPACITY:
            raise CustomError(status_code=400, message="The day's capacity is full")

        product = Product(
            id=uuid4(),
            day=product.day,
            type=product.type,
            printed_name=product.printed_name,
            theme=product.theme,
            price=product.price,
            observations=product.observations,
            sex=product.sex,
            payment=product.payment,
            client=product.client,
        )

        self.__repository.insert_product(product=product)
