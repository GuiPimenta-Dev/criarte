from typing import Dict

from src.controllers.interfaces.controllers import ControllersInterface
from src.data.get_products import GetProductsByDay


class GetProductsByDayController(ControllersInterface):
    def __init__(self, use_case: GetProductsByDay) -> None:
        self.__use_case = use_case

    def handle(self) -> Dict:
        return self.__use_case.select_products_grouped_by_day()
