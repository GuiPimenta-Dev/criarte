from typing import NamedTuple


class Item(NamedTuple):
    id: str
    product: str
    client: str
    completed: bool
    observations: str
