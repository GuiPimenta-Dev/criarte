from datetime import date

import pytest
from src.infra.test.product_spy import ProductRepositorySpy

from .register_product import RegisterProduct


def test_register_new_product(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    register_product_usecase.register_product(product=product_dto)
    product_registered = product_repository.product_by_day_params[date.today()][0]

    assert product_registered.id
    assert product_registered.status.cover is False
    assert product_registered.status.core is False


def test_10_should_be_10(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    for _ in range(10):
        register_product_usecase.register_product(product_dto)
    assert len(product_repository.product_by_day_params[date.today()]) == 10


def test_error_raises_when_10(product_dto):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    for _ in range(10):
        register_product_usecase.register_product(product=product_dto)

    with pytest.raises(Exception):
        register_product_usecase.register_product(product_dto)
