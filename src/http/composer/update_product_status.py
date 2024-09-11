from src.controllers import UpdateProductStatusController
from src.data.update_product_status import UpdateProductStatus
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository


def compose_update_product_status() -> UpdateProductStatusController:
    database = DBConnectionHandler()
    repository = ProductRepository(database)
    use_case = UpdateProductStatus(repository)

    return UpdateProductStatusController(use_case)
