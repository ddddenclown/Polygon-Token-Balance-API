from fastapi import APIRouter, Query

from app.crud.token import get_token_balance
from app.schemas.token import TokenBalance
from app.config import TOKEN_ADDRESS

router = APIRouter()

@router.get("/balance", response_model=TokenBalance)
async def get_balance(
    address: str = Query(default=TOKEN_ADDRESS, description="The address of the token to get the balance of")
):
    balance = get_token_balance(address)
    return {"address": address, "balance": balance}