from src.controllers import UpdateProductStatusController
from src.data.update_product_status import UpdateProductStatus
from src.infra.config import DBConnectionHandler
from src.infra.config.dev_db_base import DevDBConnectionHandler
from src.infra.repository import ProductRepository


def compose_dev_update_product_status() -> UpdateProductStatusController:
    database = DevDBConnectionHandler()
    repository = ProductRepository(database)
    use_case = UpdateProductStatus(repository)

    return UpdateProductStatusController(use_case)
