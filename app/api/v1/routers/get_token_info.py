from fastapi import APIRouter, HTTPException
from app.services.services import get_token_info

router = APIRouter()


@router.get("/token-info/{contract_address}")
async def token_info(contract_address: str):
    token = get_token_info(contract_address)
    if not token:
        raise HTTPException(status_code=404, detail="Token info not found")
    return token
