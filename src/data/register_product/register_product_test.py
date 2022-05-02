from datetime import date

import pytest
from src.infra.test.product_spy import ProductRepositorySpy

from .register_product import RegisterProduct


def test_register_new_product(product):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    register_product_usecase.register_product(product=product)
    product_registered = product_repository.insert_product_by_day_params[date.today()][
        0
    ]

    assert product_registered.id
    assert product_registered.status.cover is False
    assert product_registered.status.core is False


def test_max_products_in_a_day_should_be_10(product):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    MAX_PRODUCTS_IN_A_DAY = 10
    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product_usecase.register_product(product)
    assert (
        len(product_repository.insert_product_by_day_params[date.today()])
        == MAX_PRODUCTS_IN_A_DAY
    )


def test_error_raises_when_max_products_in_a_day(product):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    MAX_PRODUCTS_IN_A_DAY = 10

    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product_usecase.register_product(product=product)

    with pytest.raises(Exception):
        register_product_usecase.register_product(product)
