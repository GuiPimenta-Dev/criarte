from src.controllers import DeleteProductController
from src.data.delete_product import DeleteProduct
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository


def compose_delete_product():
    database = DBConnectionHandler()
    repository = ProductRepository(database)
    use_case = DeleteProduct(repository)

    return DeleteProductController(use_case)
