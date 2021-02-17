import json

from web3 import Web3, HTTPProvider
from web3.auto import w3
import time

from config import *


def handle_event(event):
    print(event)


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)
        print(int(time.time()))


def run():
    web3 = Web3(HTTPProvider(ETHER_NODE_URL))
    with open('TetherUSDABI.json') as f:
        my_abi = json.load(f)
    contract_address = web3.toChecksumAddress(
        '0xdac17f958d2ee523a2206206994597c13d831ec7')
    contract = web3.eth.contract(address=contract_address, abi=my_abi)
    event_filter = contract.events.Transfer.createFilter(fromBlock=11819639)
    log_loop(event_filter, 1)


if __name__ == '__main__':
    run()
"""
https://web3py.readthedocs.io/en/stable/filters.html#event-log-filters

AttributeDict(
{
'args': AttributeDict(
{
'from': '0x5169c08b2E2D43C52A09DDA0C934d87fdf1112d4', 
'to': '0x43b6268Fa0e7FeAe38a0B55855927047C490e2b2', 
'value': 1000000}), 'event': 'Transfer', 'logIndex': 0, 'transactionIndex': 1, 'transactionHash':
 HexBytes('0x481ebfd45c0d921d595c2c020601ccdfecaff825a587e2a9aeee9f7151c275b2'), 
 'address': '0x78183Ec667A3c6abbD107A2204B2acC2e72471d9', 
 'blockHash': HexBytes('0x39324b67dcf3668ea0388ac5bcb843dcebdbb16d51de7b6d8fe13eb5ac0db6c7'), 
 'blockNumber': 9627506
}
)
"""
