from abc import ABC, abstractmethod
from datetime import date

from domain.entity import Product


class RegisterProductInterface(ABC):
    """Abstract method for domain use cases"""

    @abstractmethod
    def register(
        self,
        id: str,
        name: str,
        client: str,
        completed: bool,
        observations: str,
        day: date,
    ) -> Product:
        raise Exception("Should implement method register")
