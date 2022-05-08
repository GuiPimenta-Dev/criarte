from typing import Dict

from src.data import ProductDTO
from src.data.register_product.register_product import RegisterProduct
from src.presenters.interfaces.controllers import ControllersInterface


class RegisterProductController(ControllersInterface):
    def __init__(self, use_case: RegisterProduct) -> None:
        self.__use_case = use_case

    def handle(self, product_dto: ProductDTO) -> Dict:
        self.__use_case.register_product(product_dto)
        return {"status_code": 200, "data": None}
