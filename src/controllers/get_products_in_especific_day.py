from typing import Dict

from src.controllers.interfaces.controllers import ControllersInterface
from src.data import ProductDTO
from src.domain.use_cases.get_products import GetProductsByDayInterface


class GetProductsInEspecificDayController(ControllersInterface):
    def __init__(self, use_case: GetProductsByDayInterface) -> None:
        self.__use_case = use_case

    def handle(self, day: str) -> Dict:
        return self.__use_case.select_products_in_a_day(day)
