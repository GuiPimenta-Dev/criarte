from typing import Dict, List, Optional

from fastapi import APIRouter, status
from pydantic import BaseModel
from src.data import ProductDTO, StatusDTO
from src.http.composer import (
    compose_delete_product,
    compose_register_product,
    compose_select_products_by_day,
    compose_select_products_in_especific_day,
    compose_update_product_status,
)
from src.http.composer.dev.delete_product import compose_dev_delete_product
from src.http.composer.dev.register_product_composer import compose_dev_register_product
from src.http.composer.dev.select_products_grouped_by_days import compose_dev_select_products_by_day
from src.http.composer.dev.select_products_in_especific_day import compose_dev_select_products_in_especific_day
from src.http.composer.dev.update_product_status import compose_dev_update_product_status
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


@product_routes.get("/api/v1/days/{day}")
async def get_products_in_especific_day(day: str):
    controller = compose_select_products_in_especific_day()
    try:
        return controller.handle(day)

    except Exception as error:
        handle_error(error)


@product_routes.put("/api/v1/products/{id}/status")
async def update_product_status(id: str, status: StatusDTO) -> None:
    controller = compose_update_product_status()

    try:
        controller.handle(id=id, status_dto=status)

    except Exception as error:
        handle_error(error)


@product_routes.delete("/api/v1/products/{id}")
async def delete_product(id: str) -> None:
    controller = compose_delete_product()

    try:
        controller.handle(id=id)

    except Exception as error:
        handle_error(error)


#### Dev #####


@product_routes.post("/api/dev/v1/products", status_code=status.HTTP_201_CREATED)
async def register_dev_product(product_dto: ProductDTO):
    controller = compose_dev_register_product()

    try:
        return controller.handle(product_dto)

    except Exception as error:
        handle_error(error)


@product_routes.get("/api/dev/v1/products")
async def get_dev_products_grouped_by_day():
    controller = compose_dev_select_products_by_day()
    try:
        return controller.handle()

    except Exception as error:
        handle_error(error)


@product_routes.get("/api/dev/v1/days/{day}")
async def get_dev_products_in_especific_day(day: str):
    controller = compose_dev_select_products_in_especific_day()
    try:
        return controller.handle(day)

    except Exception as error:
        handle_error(error)


@product_routes.put("/api/dev/v1/products/{id}/status")
async def update_dev_product_status(id: str, status: StatusDTO) -> None:
    controller = compose_dev_update_product_status()

    try:
        controller.handle(id=id, status_dto=status)

    except Exception as error:
        handle_error(error)


@product_routes.delete("/api/dev/v1/products/{id}")
async def delete_dev_product(id: str) -> None:
    controller = compose_dev_delete_product()

    try:
        controller.handle(id=id)

    except Exception as error:
        handle_error(error)
