from datetime import date

import pytest
from faker import Faker

from src.data.register_product.register_product_dto import ClientDTO, ProductDTO
from src.infra.test.product_spy import ProductRepositorySpy

from .register_product import RegisterProduct

faker = Faker()


@pytest.fixture()
def product():
    return ProductDTO(
        type=faker.name(),
        printed_name=faker.name(),
        theme=faker.name(),
        price=faker.random_number(),
        sex="male",
        payment="pix",
        day=date.today(),
        client=ClientDTO(
            name=faker.name(), address=faker.sentence(), state=faker.name()
        ),
    )


def test_register_new_product(product):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    register_product_usecase.register_product(product=product)
    product_registered = product_repository.insert_product_params[date.today()][0]

    assert product_registered.id
    assert product_registered.cover is False
    assert product_registered.core is False


def test_max_products_in_a_day_should_be_10(product):
    product_repository = ProductRepositorySpy()
    register_product_usecase = RegisterProduct(repository=product_repository)

    MAX_PRODUCTS_IN_A_DAY = 10
    for _ in range(MAX_PRODUCTS_IN_A_DAY):
        register_product_usecase.register_product(product)
    assert (
        len(product_repository.insert_product_params[date.today()])
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
