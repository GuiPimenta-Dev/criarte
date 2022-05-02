from datetime import date

from src.infra.test.product_spy import ProductRepositorySpy

from .get_products_by_day import GetProductsByDay


def test_get_products_in_specific_day(product):
    product_repository = ProductRepositorySpy()
    product_repository.insert_product(product=product)

    get_products_usecase = GetProductsByDay(repository=product_repository)

    TODAY = date.today()
    products = get_products_usecase.get_products_by_day(day=TODAY)

    assert products == product_repository.product_by_day_params[TODAY]


def test_get_products_in_specific_day_with_empty_results():
    product_repository = ProductRepositorySpy()

    get_products_usecase = GetProductsByDay(repository=product_repository)
    products = get_products_usecase.get_products_by_day(day=date.today())

    assert products == []
