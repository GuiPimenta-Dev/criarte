from uuid import uuid4

from src.domain.repository.product import ProductRepositoryInterface
from src.domain.use_cases import DeleteProductInterface


class DeleteProduct(DeleteProductInterface):
    """Delete product use case"""

    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    def delete_product(self, id: uuid4) -> None:
        self.repository.delete_product(id)
