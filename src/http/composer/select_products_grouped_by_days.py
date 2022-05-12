from src.data.get_products import GetProductsByDay
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository
from src.controllers import GetProductsByDayController


def compose_select_products_by_day() -> GetProductsByDayController:
    database = DBConnectionHandler("sqlite:///in_memory.db")
    repository = ProductRepository(database)
    use_case = GetProductsByDay(repository)

    return GetProductsByDayController(use_case)
