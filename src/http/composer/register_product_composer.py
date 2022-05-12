from src.data.register_product import RegisterProduct
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository
from src.controllers import RegisterProductController


def compose_register_product():
    database = DBConnectionHandler("sqlite:///in_memory.db")
    repository = ProductRepository(database)
    use_case = RegisterProduct(repository)

    return RegisterProductController(use_case)
