from fastapi import APIRouter, status
from src.data import ProductDTO, StatusDTO
from src.http.composer import (
    compose_register_product,
    compose_select_products_by_day,
    compose_update_product_status,
)
from src.http.errors.http_error import handle_error

product_routes = APIRouter()


@product_routes.post("/api/v1/products", status_code=status.HTTP_201_CREATED)
async def register_product(product_dto: ProductDTO):
    controller = compose_register_product()

    try:
        return controller.handle(product_dto)

    except Exception as error:
        handle_error(error)


@product_routes.get("/api/v1/products")
async def get_products_grouped_by_day():
    controller = compose_select_products_by_day()
    try:
        return controller.handle()

    except Exception as error:
        handle_error(error)


@product_routes.put("/api/v1/products/{id}/status")
async def update_product_status(id: str, status: StatusDTO) -> None:
    controller = compose_update_product_status()

    try:
        controller.handle(id=id, status_dto=status)

    except Exception as error:
        handle_error(error)
