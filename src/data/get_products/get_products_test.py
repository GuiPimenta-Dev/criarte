from datetime import date

from src.domain.use_cases.get_week_days import WeekDaysInterface
from src.infra.test.product_spy import ProductRepositorySpy

from .get_products import GetProductsByDay


class GetDaysSpy(WeekDaysInterface):
    def get_products_by_week_day(self, products_by_day):
        return products_by_day


def test_get_products_grouped_by_day(product):
    product_repository = ProductRepositorySpy()
    product_repository.insert_product(product=product)
    product_repository.insert_product(product=product)
    product_repository.insert_product(product=product)

    get_products_usecase = GetProductsByDay(repository=product_repository, week_days=GetDaysSpy())

    products = get_products_usecase.select_products_grouped_by_day()
    assert products == product_repository.product_by_day_params


def test_get_products_in_specific_day(product):
    product_repository = ProductRepositorySpy()
    product_repository.insert_product(product=product)

    get_products_usecase = GetProductsByDay(repository=product_repository, week_days=GetDaysSpy())

    TODAY = date.today()
    products = get_products_usecase.select_products_in_a_day(day=TODAY)

    assert products == product_repository.product_by_day_params[TODAY]


def test_get_products_in_specific_day_with_empty_results():
    product_repository = ProductRepositorySpy()

    get_products_usecase = GetProductsByDay(repository=product_repository, week_days=GetDaysSpy())
    products = get_products_usecase.select_products_in_a_day(day=date.today())

    assert products == []
