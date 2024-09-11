# pylint: disable=no-name-in-module
from datetime import date

from pydantic import UUID4, BaseModel
from src.data import ClientDTO, StatusDTO


class Product(BaseModel):
    id: UUID4
    day: date
    type: str
    printed_name: str
    theme: str
    price: float
    observations: str
    sex: str
    payment: str
    client: ClientDTO
    status: StatusDTO = StatusDTO(cover=False, core=False)
