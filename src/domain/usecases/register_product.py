from abc import ABC, abstractmethod

from src.data import ProductDTO
from src.domain.entities import Product


class RegisterProductInterface(ABC):
    """Abstract method for domain use cases"""

    @abstractmethod
    def register_product(product: ProductDTO) -> Product:
        raise Exception("Should implement method register")
