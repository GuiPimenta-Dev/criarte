import os

from dotenv import load_dotenv
from src.controllers import DeleteProductController
from src.data.delete_product import DeleteProduct
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository

load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")


def compose_delete_product():
    database = DBConnectionHandler(f"postgresql://{USER}:{PASSWORD}@postgres_db:5432")
    repository = ProductRepository(database)
    use_case = DeleteProduct(repository)

    return DeleteProductController(use_case)
