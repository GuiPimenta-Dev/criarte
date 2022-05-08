import contextlib

from fastapi import Request


async def request_adapter(request: Request):

    body = None

    with contextlib.suppress(Exception):
        body = await request.json()

    return {"query_params": request.query_params, "body": body}
