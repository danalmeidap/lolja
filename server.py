from fastapi import FastAPI
from src.infra.sqlalchemy.config.database import create_db
from fastapi.middleware.cors import CORSMiddleware
from src.routers import auth, products, orders


app = FastAPI()

app.include_router(products.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(orders.router)

create_db()


origins = [
    "http://localhost:5500",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
