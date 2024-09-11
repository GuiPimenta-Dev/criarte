# pylint: disable=too-few-public-methods,no-name-in-module
from datetime import date
from typing import Optional

from pydantic import BaseModel


class ClientDTO(BaseModel):
    name: str
    address: str
    state: str


class StatusDTO(BaseModel):
    cover: bool
    core: bool


class ProductDTO(BaseModel):
    type: str
    printed_name: str
    theme: str
    price: float
    sex: str
    payment: str
    day: date
    client: ClientDTO
    observations: str = ""
