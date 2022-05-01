from datetime import date

from pydantic import BaseModel


class ClientDTO(BaseModel):
    name: str
    address: str
    state: str


class ProductDTO(BaseModel):
    type: str
    printed_name: str
    theme: str
    price: float
    sex: str
    payment: str
    day: date
    client: ClientDTO
