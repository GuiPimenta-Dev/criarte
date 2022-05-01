from abc import ABC, abstractmethod

from src.data.register_product.register_product_dto import ProductDTO
from src.domain.entity import Product


class RegisterProductInterface(ABC):
    """Abstract method for domain use cases"""

    @abstractmethod
    def register_product(product: ProductDTO) -> Product:
        raise Exception("Should implement method register")
