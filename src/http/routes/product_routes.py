from fastapi import APIRouter, Request, status
from src.data import ClientDTO, ProductDTO
from src.http.adapter import request_adapter
from src.http.composer import compose_register_product, compose_select_products_by_day
from src.http.errors.http_error import handle_error

product_routes = APIRouter()


@product_routes.post("/api/v1/products", status_code=status.HTTP_201_CREATED)
async def register_product(request: Request):
    req = await request_adapter(request=request)
    controller = compose_register_product()

    try:
        product_dto = ProductDTO(**req["body"], client=ClientDTO(**req["body"]))
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
