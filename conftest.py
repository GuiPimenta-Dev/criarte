import random
from datetime import date
from typing import Callable
from uuid import uuid4

import pytest
from faker import Faker

from src.data import ClientDTO, ProductDTO
from src.domain.entity.product import Product
from src.infra.config import DBConnectionHandler

faker = Faker()


@pytest.fixture()
def product_dto() -> ProductDTO:

    return ProductDTO(
        type=faker.name(),
        printed_name=faker.name(),
        theme=faker.name(),
        price=faker.random_number(),
        sex=random.choice(["male", "female"]),
        payment=random.choice(["pix", "credit_card", "bank_slip"]),
        observations=faker.name(),
        day=date.today(),
        client=ClientDTO(name=faker.name(), address=faker.sentence(), state=faker.name()),
    )


@pytest.fixture()
def product(product_dto: ProductDTO) -> Product:

    return Product(
        id=uuid4(),
        type=product_dto.type,
        printed_name=product_dto.printed_name,
        theme=product_dto.theme,
        price=product_dto.price,
        sex=product_dto.sex,
        payment=product_dto.payment,
        observations=product_dto.observations,
        day=product_dto.day,
        client=product_dto.client,
    )


@pytest.fixture()
def products(product_dto: ProductDTO) -> Callable:
    def get_product():
        return Product(
            id=uuid4(),
            type=faker.name(),
            printed_name=faker.name(),
            theme=faker.sentence(),
            price=faker.random_number(),
            sex=product_dto.sex,
            payment=product_dto.payment,
            observations=product_dto.observations,
            day=product_dto.day,
            client=product_dto.client,
        )

    return get_product


@pytest.fixture()
def engine():
    db_connection_handler = DBConnectionHandler("sqlite:///test.db")
    return db_connection_handler.get_engine()


@pytest.fixture(autouse=True)
def clean_up(engine):
    yield
    engine.execute("DELETE FROM products;")
