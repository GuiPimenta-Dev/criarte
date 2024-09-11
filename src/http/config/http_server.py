from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.http.routes import product_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes)
