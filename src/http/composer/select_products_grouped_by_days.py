from src.controllers import GetProductsByDayController
from src.data.get_days import GetDays
from src.data.get_products import GetProductsByDay
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository


def compose_select_products_by_day() -> GetProductsByDayController:
    database = DBConnectionHandler()
    repository = ProductRepository(database)
    use_case = GetProductsByDay(repository=repository, week_days=GetDays())

    return GetProductsByDayController(use_case)
