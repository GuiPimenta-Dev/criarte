from datetime import date
from random import choice
from uuid import uuid4

import pytest
from faker import Faker

from src.data import ClientDTO, ProductDTO
from src.domain.entities.product import Product

faker = Faker()


@pytest.fixture()
def product_dto() -> ProductDTO:

    return ProductDTO(
        type=faker.name(),
        printed_name=faker.name(),
        theme=faker.name(),
        price=faker.random_number(),
        sex=choice(["male", "female"]),
        payment=choice(["pix", "credit_card", "bank_slip"]),
        day=date.today(),
        client=ClientDTO(
            name=faker.name(), address=faker.sentence(), state=faker.name()
        ),
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
        day=product_dto.day,
        client=product_dto.client,
    )
