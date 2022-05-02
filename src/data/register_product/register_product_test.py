from datetime import date

import pytest
from src.infra.test.product_spy import ProductRepositorySpy

from .register_product import RegisterProduct

MAX_PRODUCTS_IN_A_DAY = 10


def test_register_new_product(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    register_product_usecase.register_product(product=product_dto)
    product_registered = product_repository.product_by_day_params[date.today()][0]

    assert product_registered.id
    assert product_registered.status.cover is False
    assert product_registered.status.core is False


def test_max_products_in_a_day_should_be_10(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product_usecase.register_product(product_dto)
    assert (
        len(product_repository.product_by_day_params[date.today()])
        == MAX_PRODUCTS_IN_A_DAY
    )


def test_error_raises_when_max_products_in_a_day(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product_usecase.register_product(product=product_dto)

    with pytest.raises(Exception):
        register_product_usecase.register_product(product_dto)
