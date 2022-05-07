from typing import Literal

from pydantic import UUID4, BaseModel
from src.data import ClientDTO, StatusDTO
from src.domain.entity.day import Day


class Product(BaseModel):
    id: UUID4
    day: Day
    type: str
    printed_name: str
    theme: str
    price: float
    sex: Literal["male", "female"]
    payment: Literal["pix", "credit_card", "bank_slip"]
    client: ClientDTO
    status: StatusDTO = StatusDTO(cover=False, core=False)
