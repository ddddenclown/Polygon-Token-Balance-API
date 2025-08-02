from web3 import Web3
from app.services.web3_provider import get_web3
from app.config import TOKEN_ADDRESS, ERC20_ABI


def get_token_balance(address: str) -> float:
    w3 = get_web3()

    token_address = Web3.to_checksum_address(TOKEN_ADDRESS)
    user_address = Web3.to_checksum_address(address)

    contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    balance = contract.functions.balanceOf(user_address).call()
    decimals = contract.functions.decimals().call()
    return balance / (10 ** decimals)