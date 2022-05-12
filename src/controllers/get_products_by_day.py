from typing import Dict

from src.controllers.interfaces.controllers import ControllersInterface
from src.data.get_products import GetProductsByDay

from .presenters.get_products_by_day_presenter import present_products_by_day


class GetProductsByDayController(ControllersInterface):
    def __init__(self, use_case: GetProductsByDay) -> None:
        self.__use_case = use_case

    def handle(self) -> Dict:
        products = self.__use_case.select_products_grouped_by_day()
        presented_products = present_products_by_day(products)
        return {"data": presented_products}
