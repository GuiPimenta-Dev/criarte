from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.data import ClientDTO, ProductDTO
from src.error.custom_error import CustomError
from src.http.adapter import request_adapter
from src.http.composer.register_product_composer import compose_register_product
from src.presenters.errors import HttpErrors

product_routes = APIRouter()


@product_routes.post("/api/v1/product")
async def register_product(request: Request):
    req = await request_adapter(request=request)
    controller = compose_register_product()

    try:
        product_dto = ProductDTO(**req["body"], client=ClientDTO(**req["body"]))
        response = controller.handle(product_dto)

    except ValidationError:
        response = HttpErrors.error_422()

    except CustomError as error:
        response = HttpErrors.error(status_code=error.status_code, error=error.message)

    return JSONResponse(status_code=response["status_code"], content=response["data"])
