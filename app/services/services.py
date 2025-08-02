from app.crud.token import fetch_token_info


def get_token_info(contract_address: str):
    token = fetch_token_info(contract_address)
    return token
