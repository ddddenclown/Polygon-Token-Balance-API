from web3 import Web3
from typing import List
import requests

from app.services.web3_provider import get_web3
from app.config import TOKEN_ADDRESS, ERC20_ABI, POLYGONSCAN_API_KEY, CHAIN, BASE_URL


def get_token_balance(address: str) -> float:
    w3 = get_web3()

    token_address = Web3.to_checksum_address(TOKEN_ADDRESS)
    user_address = Web3.to_checksum_address(address)

    contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    balance = contract.functions.balanceOf(user_address).call()
    decimals = contract.functions.decimals().call()
    return balance / (10 ** decimals)


def get_balance_batch(addresses: List[str]) -> List[float]:
    results = []
    w3 = get_web3()
    token_address = Web3.to_checksum_address(TOKEN_ADDRESS)
    contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    decimals = contract.functions.decimals().call()
    
    for address in addresses:
        user_address = Web3.to_checksum_address(address)
        balance = contract.functions.balanceOf(user_address).call()
        results.append(balance / (10 ** decimals))
    
    return results


def fetch_token_info(contract_address: str):
    params_tx = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": contract_address,
        "page": 1,
        "offset": 1,
        "sort": "asc",
        "apikey": POLYGONSCAN_API_KEY,
        "chainid": CHAIN,
    }
    resp_tx = requests.get(BASE_URL, params=params_tx)
    resp_tx.raise_for_status()
    data_tx = resp_tx.json()
    print("Response for token transactions:", data_tx)

    if data_tx.get("status") != "1" or not data_tx.get("result"):
        print("No token transactions found or error in response")
        return None

    first_tx = data_tx["result"][0]
    symbol = first_tx.get("tokenSymbol")
    name = first_tx.get("tokenName")
    print(f"Token symbol: {symbol}, Token name: {name}")

    params_supply = {
        "module": "stats",
        "action": "tokensupply",
        "contractaddress": contract_address,
        "apikey": POLYGONSCAN_API_KEY,
        "chainid": CHAIN,
    }
    resp_supply = requests.get(BASE_URL, params=params_supply)
    resp_supply.raise_for_status()
    data_supply = resp_supply.json()
    print("Response for token supply:", data_supply)

    total_supply = 0
    if data_supply.get("status") == "1":
        total_supply = int(data_supply.get("result", 0))
        print(f"Total supply: {total_supply}")
    else:
        print("Failed to get total supply or no data")

    return {
        "symbol": symbol,
        "name": name,
        "totalSupply": total_supply
    }
