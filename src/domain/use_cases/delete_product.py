from abc import ABC, abstractmethod
from uuid import uuid4


class DeleteProductInterface(ABC):
    """Abstract method for register product use case"""

    @abstractmethod
    def delete_product(self, id: uuid4) -> None:
        """Delete product abstract method"""
        raise Exception("Should implement method delete_product")
