from datetime import date

import pytest
from faker import Faker

from src.data.register_product.register_product_dto import ClientDTO, ProductDTO
from src.infra.test.product_spy import ProductRepositorySpy

from .get_products_by_day import GetProductsByDay

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


def test_get_products_in_specific_day(product):
    product_repository = ProductRepositorySpy()
    TODAY = date.today()
    product_repository.insert_product(product)

    get_products_usecase = GetProductsByDay(repository=product_repository)
    products = get_products_usecase.get_products_by_day(day=TODAY)

    assert products == product_repository.insert_product_params[TODAY]


def test_get_products_in_specific_day_with_empty_results():
    product_repository = ProductRepositorySpy()

    get_products_usecase = GetProductsByDay(repository=product_repository)
    products = get_products_usecase.get_products_by_day(day=date.today())

    assert products == []
