from datetime import date
from typing import NamedTuple
from uuid import uuid4


class Product(NamedTuple):
    id: uuid4
    name: str
    client: str
    observations: str
    day: date
    completed: bool = False
