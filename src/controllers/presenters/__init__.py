# pylint: disable=no-self-argument

from attr import s
from pydantic import BaseModel, validator
from src.infra.entity.products_entity import ProductEntity


class Client(BaseModel):
    name: str
    address: str
    state: str


class Status(BaseModel):
    cover: bool
    core: bool


class PresentedProduct(BaseModel):
    id: str
    type: str
    printed_name: str
    theme: str
    price: float
    sex: str
    payment: str
    client: Client
    status: Status

    @validator("sex")
    def parse_sex_string(cls, value):
        sex = {"male": "Homem", "female": "Mulher"}
        return sex[value]

    @validator("payment")
    def parse_payment_string(cls, value):
        payment = {
            "pix": "Pix",
            "credt_card": "Cartão de crédito",
            "bank_slip": "Boleto bancário",
        }
        return payment[value]


def present_product(product: ProductEntity) -> PresentedProduct:
    client = Client(
        name=product.client_name,
        address=product.client_address,
        state=product.client_state,
    )
    status = Status(cover=product.cover_status, core=product.core_status)
    return PresentedProduct(
        id=product.id,
        type=product.type,
        printed_name=product.printed_name,
        theme=product.theme,
        price=product.price,
        sex=product.sex,
        payment=product.payment,
        client=client,
        status=status,
    )
