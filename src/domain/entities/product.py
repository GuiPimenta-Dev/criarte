from datetime import date
from typing import Literal

from pydantic import UUID4, BaseModel


class Client(BaseModel):
    name: str
    address: str
    state: str


class Product(BaseModel):
    id: UUID4
    type: str
    printed_name: str
    theme: str
    price: float
    sex: Literal["male", "female"]
    payment: Literal["pix", "credit_card", "bank_slip"]
    day: date
    client: Client
    cover: bool = False
    core: bool = False
