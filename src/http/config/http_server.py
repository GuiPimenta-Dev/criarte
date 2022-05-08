from fastapi import FastAPI
from src.http.routes import product_routes

app = FastAPI()

app.include_router(product_routes)
