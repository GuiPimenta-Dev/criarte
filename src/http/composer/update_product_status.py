import os

from dotenv import load_dotenv
from src.controllers import UpdateProductStatusController
from src.data.update_product_status import UpdateProductStatus
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository

load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")


def compose_update_product_status() -> UpdateProductStatusController:
    database = DBConnectionHandler(f"postgresql://{USER}:{PASSWORD}@postgres_db:5432")
    repository = ProductRepository(database)
    use_case = UpdateProductStatus(repository)

    return UpdateProductStatusController(use_case)
