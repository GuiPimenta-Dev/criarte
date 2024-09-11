from abc import ABC, abstractmethod
from uuid import uuid4

from src.data import StatusDTO


class UpdateProductStatusInterface(ABC):
    """Abstract method for update product status use case" """

    @abstractmethod
    def update_status(self, id: uuid4, status: StatusDTO) -> None:
        raise Exception("Should implement method update_status")
