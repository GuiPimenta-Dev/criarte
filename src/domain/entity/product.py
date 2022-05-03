# pylint: disable=no-self-argument,no-self-use,no-name-in-module
from datetime import date
from typing import Literal

from pydantic import UUID4, BaseModel, validator
from src.data import ClientDTO, StatusDTO

CAPACITY = 10


class WorkDay(BaseModel):
    date: date
    products: int

    @validator("products")
    def check_if_day_capacity_is_full(cls, value):

        if value > CAPACITY:
            raise Exception("Day capacity is full")


class Product(BaseModel):
    id: UUID4
    day: WorkDay
    type: str
    printed_name: str
    theme: str
    price: float
    sex: Literal["male", "female"]
    payment: Literal["pix", "credit_card", "bank_slip"]
    client: ClientDTO
    status: StatusDTO = StatusDTO(cover=False, core=False)
