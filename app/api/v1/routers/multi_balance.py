from fastapi import APIRouter
from typing import List

from app.crud.token import get_balance_batch
from app.schemas.multi import BalanceBatchResponse, BatchRequests


router = APIRouter()


@router.post("/balances", response_model=List[BalanceBatchResponse])
async def batch_balances(request: BatchRequests):
    balances = get_balance_batch(request.addresses)
    return [
        {"address": addr, "balance": bal}
        for addr, bal in zip(request.addresses, balances)
    ]
