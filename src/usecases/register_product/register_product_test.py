from datetime import date

import pytest
from faker import Faker

from infra.test.product_spy import ProductRepositorySpy

from .register_product import RegisterProduct

faker = Faker()


def test_register_new_product():
    product_repository = ProductRepositorySpy()
    register_product = RegisterProduct(repository=product_repository)

    TODAY = date.today()
    register_product.register(
        name=faker.name(),
        client=faker.name(),
        observations=faker.sentence(),
        day=TODAY,
    )

    assert "id" in product_repository.insert_product_params[TODAY][0]
    assert "name" in product_repository.insert_product_params[TODAY][0]
    assert "client" in product_repository.insert_product_params[TODAY][0]
    assert "observations" in product_repository.insert_product_params[TODAY][0]
    assert "day" in product_repository.insert_product_params[TODAY][0]
    assert product_repository.insert_product_params[TODAY][0]["completed"] is False


def test_max_products_in_a_day_should_be_10():
    product_repository = ProductRepositorySpy()
    register_product = RegisterProduct(repository=product_repository)

    TODAY = date.today()
    MAX_PRODUCTS_IN_A_DAY = 10
    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product.register(
            name=faker.name(),
            client=faker.name(),
            observations=faker.sentence(),
            day=TODAY,
        )
    assert len(product_repository.insert_product_params[TODAY]) == MAX_PRODUCTS_IN_A_DAY


def test_error_raises_when_max_products_in_a_day():
    product_repository = ProductRepositorySpy()
    register_product = RegisterProduct(repository=product_repository)

    TODAY = date.today()
    MAX_PRODUCTS_IN_A_DAY = 10

    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product.register(
            name=faker.name(),
            client=faker.name(),
            observations=faker.sentence(),
            day=TODAY,
        )
    with pytest.raises(Exception):
        register_product.register(
            name=faker.name(),
            client=faker.name(),
            observations=faker.sentence(),
            day=TODAY,
        )
