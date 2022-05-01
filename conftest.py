from datetime import date

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
        sex="male",
        payment="pix",
        day=date.today(),
        client=ClientDTO(
            name=faker.name(), address=faker.sentence(), state=faker.name()
        ),
    )
