from fastapi import HTTPException, status
from pydantic import ValidationError
from src.errors import CustomError


def handle_error(error: Exception) -> None:
    print(error)
    if isinstance(error, ValidationError):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if isinstance(error, CustomError):
        raise HTTPException(status_code=error.status_code, detail=error.message)

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
