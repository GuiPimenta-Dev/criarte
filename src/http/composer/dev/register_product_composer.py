from src.controllers import RegisterProductController
from src.data.register_product import RegisterProduct
from src.infra.config.dev_db_base import DevDBConnectionHandler
from src.infra.repository import ProductRepository


def compose_dev_register_product():
    database = DevDBConnectionHandler()
    repository = ProductRepository(database)
    use_case = RegisterProduct(repository)

    return RegisterProductController(use_case)
