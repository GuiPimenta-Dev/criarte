from typing import Dict
from uuid import uuid4

from src.controllers.interfaces.controllers import ControllersInterface
from src.data.delete_product import DeleteProduct


class DeleteProductController(ControllersInterface):
    def __init__(self, use_case: DeleteProduct) -> None:
        self.__use_case = use_case

    def handle(self, id: uuid4) -> Dict:
        self.__use_case.delete_product(id)
