from abc import ABC, abstractmethod

from domain.entity.product import Product


class RegisterProduct(ABC):
    """Abstract method for register"""

    @abstractmethod
    def register(
        self, id: str, name: str, client: str, completed: bool, observations: str
    ) -> Product:
        raise Exception("Should implement method register")
