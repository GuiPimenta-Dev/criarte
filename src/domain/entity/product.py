from typing import NamedTuple


class Product(NamedTuple):
    id: str
    name: str
    client: str
    completed: bool
    observations: str
