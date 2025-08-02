from re import L
from web3 import Web3
from app.config import POLYGON_RPC_URL

def get_web3():
    return Web3(Web3.HTTPProvider(POLYGON_RPC_URL))