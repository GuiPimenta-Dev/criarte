from abc import ABC, abstractmethod
from uuid import uuid4


class UpdateProductStatus(ABC):
    """Abstract method for update product status use case" """

    @abstractmethod
    def update_status(
        self,
        id: uuid4,
        cover: bool,
        core: bool,
    ) -> None:
        raise Exception("Should implement method update_status")
