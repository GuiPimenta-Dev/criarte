from src.controllers.interfaces.controllers import ControllersInterface
from src.data import ProductDTO
from src.data.register_product.register_product import RegisterProduct


class RegisterProductController(ControllersInterface):
    def __init__(self, use_case: RegisterProduct) -> None:
        self.__use_case = use_case

    def handle(self, product_dto: ProductDTO) -> None:
        self.__use_case.register_product(product_dto)
