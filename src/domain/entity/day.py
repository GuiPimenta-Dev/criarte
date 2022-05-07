# pylint: disable=no-self-argument,no-self-use,no-name-in-module
from datetime import date

from pydantic import BaseModel, validator

CAPACITY = 10


class Day(BaseModel):
    date: date
    products: int

    @validator("products")
    def check_if_day_capacity_is_full(cls, value):
        # sourcery skip: raise-specific-error

        if value > CAPACITY:
            raise Exception("Day capacity is full")
