from pydantic import BaseModel
from typing import List, Optional


class BalanceBatchResponse(BaseModel):
    address: str
    balance: Optional[float]


class BatchRequests(BaseModel):
    addresses: List[str]
