# pylint: disable=no-self-argument,no-self-use,no-name-in-module
from datetime import date

from pydantic import BaseModel, validator
from src.errors.custom_error import CustomError

CAPACITY = 10


class Day(BaseModel):
    date: date
    products: int

    @validator("products")
    def check_if_day_capacity_is_full(cls, value):

        if value > CAPACITY:
            raise CustomError(status_code=400, message="The day's capacity is full")
