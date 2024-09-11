from src.controllers.delete_product import DeleteProductController
from src.data.delete_product.delete_product import DeleteProduct
from src.infra.config.dev_db_base import DevDBConnectionHandler
from src.infra.repository.product_repository import ProductRepository


def compose_dev_delete_product():
    database = DevDBConnectionHandler()
    repository = ProductRepository(database)
    use_case = DeleteProduct(repository)

    return DeleteProductController(use_case)
