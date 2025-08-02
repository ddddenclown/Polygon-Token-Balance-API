from fastapi import APIRouter
from app.api.v1.routers import token_balance


api_router = APIRouter()
api_router.include_router(token_balance.router)