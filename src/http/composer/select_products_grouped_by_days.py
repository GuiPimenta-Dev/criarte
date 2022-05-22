import os

from dotenv import load_dotenv
from src.controllers import GetProductsByDayController
from src.data.get_days import GetDays
from src.data.get_products import GetProductsByDay
from src.infra.config import DBConnectionHandler
from src.infra.repository import ProductRepository

load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")


def compose_select_products_by_day() -> GetProductsByDayController:
    database = DBConnectionHandler(f"postgresql://{USER}:{PASSWORD}@postgres_db:5432")
    repository = ProductRepository(database)
    use_case = GetProductsByDay(repository=repository, week_days=GetDays())

    return GetProductsByDayController(use_case)
