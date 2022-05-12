from uuid import uuid4

from src.controllers.interfaces.controllers import ControllersInterface
from src.data import StatusDTO
from src.data.update_product_status import UpdateProductStatus


class UpdateProductStatusController(ControllersInterface):
    def __init__(self, use_case: UpdateProductStatus) -> None:
        self.__use_case = use_case

    def handle(self, id: uuid4, status_dto: StatusDTO) -> None:
        self.__use_case.update_status(id=id, status=status_dto)
