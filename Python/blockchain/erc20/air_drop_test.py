import json

from web3 import Web3, HTTPProvider

URL = 'https://ropsten.infura.io/v3/'
sol_path = 'contract/Airdropper.sol'
abi_path = 'contract/AirdropperABI.json'

airdrop_address = ''

address = ''
pri_key = ''
fusdt_address = ''


def get_client():
    return Web3(HTTPProvider(URL))


def get_contract():
    web3 = get_client()
    with open(abi_path) as f:
        my_abi = json.load(f)
    return web3.eth.contract(address=web3.toChecksumAddress(airdrop_address), abi=my_abi)


def run():
    web3 = get_client()
    contract = get_contract()

    web3.eth.defaultAccount = address
    to_address_list = [
        '',
        '',
        '',
        '',
        '',
        '',
    ]
    amount = 1000000

    params = {
        'from': address,
        'nonce': web3.eth.getTransactionCount(address),
        'gasPrice': web3.toWei(str(50), 'gwei'),
        'gas': int(500000)
    }

    # 執行交易
    transaction = contract.functions \
        .AirTransfer(to_address_list, amount, fusdt_address) \
        .buildTransaction(params)

    signed_txn = web3.eth.account.signTransaction(
        transaction, private_key=pri_key)

    tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(tx_id.hex())


if __name__ == "__main__":
    run()
