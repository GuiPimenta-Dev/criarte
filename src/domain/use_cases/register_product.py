from abc import ABC, abstractmethod

from src.data import ProductDTO
from src.domain.entity import Product


class RegisterProductInterface(ABC):
    """Abstract method for register product use case"""

    @abstractmethod
    def register_product(self, product: ProductDTO) -> Product:
        """Register product abstract method"""
        raise Exception("Should implement method register")
