from pydantic import BaseModel


class TokenBalance(BaseModel):
    address: str
    balance: float
