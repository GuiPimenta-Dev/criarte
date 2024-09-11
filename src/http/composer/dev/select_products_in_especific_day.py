from src.controllers import GetProductsInEspecificDayController
from src.data.get_days import GetDays
from src.data.get_products import GetProductsByDay
from src.infra.config import DBConnectionHandler
from src.infra.config.dev_db_base import DevDBConnectionHandler
from src.infra.repository import ProductRepository


def compose_dev_select_products_in_especific_day() -> GetProductsInEspecificDayController:
    database = DevDBConnectionHandler()
    repository = ProductRepository(database)
    use_case = GetProductsByDay(repository=repository, week_days=GetDays())

    return GetProductsInEspecificDayController(use_case)
