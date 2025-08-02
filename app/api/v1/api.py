from fastapi import APIRouter
from app.api.v1.routers import token_balance, multi_balance, get_token_info

api_router = APIRouter()
api_router.include_router(token_balance.router, prefix="/balance")
api_router.include_router(multi_balance.router, prefix="/batch")
api_router.include_router(get_token_info.router, prefix="/info")
