from datetime import date
from random import choice

import pytest
from faker import Faker

from src.data import ClientDTO, ProductDTO

faker = Faker()


@pytest.fixture()
def product():

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
