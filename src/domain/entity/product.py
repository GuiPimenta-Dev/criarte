from datetime import date
from typing import Literal

from pydantic import UUID4, BaseModel
from src.data import ClientDTO, StatusDTO


class Product(BaseModel):
    id: UUID4
    type: str
    printed_name: str
    theme: str
    price: float
    sex: Literal["male", "female"]
    payment: Literal["pix", "credit_card", "bank_slip"]
    day: date
    client: ClientDTO
    status: StatusDTO = StatusDTO(cover=False, core=False)
