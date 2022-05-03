from uuid import uuid4

from src.data import StatusDTO
from src.domain.repository.product import ProductRepositoryInterface
from src.domain.usecase.update_product_status import UpdateProductStatusInterface


class UpdateProductStatus(UpdateProductStatusInterface):
    """Update product status use case"""

    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.__repository = repository

    def update_status(self, id: uuid4, status: StatusDTO) -> None:
        self.__repository.update_product_status(id=id, status=status)
