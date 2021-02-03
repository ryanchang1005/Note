import json
import secrets
import requests

from datetime import datetime
from decimal import Decimal

from web3 import Web3, HTTPProvider
from eth_account import Account

from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from tronpy.keys import PrivateKey

from bit import wif_to_key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from cryptoaddress import BitcoinAddress

from config import *

"""
         EtherChain
        / 
Chain -- BTCChain
        \
         TronChain


             EtherCurrency - EtherEthCurrency
            /              - EtherUSDTCurrency
Currency -- 
            \
             TronCurrency - TronTrxCurrency
           |             - TronUSDTCurrency
            \
             BTCCurrency
"""

###############################################################


class Chain:

    def get_lib_client(self):
        """
        Return client of chain object
        return: Ether, Tron
        ex: Ether > from web3 import Web3
            Tron > from tronpy import Tron
        """
        raise NotImplementedError

    def deploy(self):
        raise NotImplementedError

    def pri_key_to_address(self, pri_key):
        """
        Return address by pri_key and client of chain 
        return: address(str)
        """
        raise NotImplementedError

    def generate_address(self):
        """
        Generate new address and private key pair
        return: dict
        {
            'address': '0x1234567890...',
            'pri_key': '1234567890',
        }
        """
        raise NotImplementedError

    def is_address_valid(self, address):
        """
        Check address format valid
        return: bool
        """
        raise NotImplementedError

    def to_valid_address(self, address):
        """
        Convert address(random upper/lower) to valid address
        return: address(str)
        """
        raise NotImplementedError


class EtherChain(Chain):

    def get_lib_client(self):
        return Web3(HTTPProvider(ETHER_NODE_URL))

    def generate_address(self):
        account = Account.create(secrets.token_hex(100))
        return {
            'address': account.address,
            'pri_key': account.key.hex(),
        }

    def pri_key_to_address(self, pri_key):
        account = Account.privateKeyToAccount(pri_key)
        return account.address

    def is_address_valid(self, address):
        return self.get_lib_client().isChecksumAddress(address)

    def to_valid_address(self, address):
        return self.get_lib_client().toChecksumAddress(address)


class TronChain(Chain):

    def get_lib_client(self):
        return Tron(network=TRON_NETWORK)

    def generate_address(self):
        tron = self.get_lib_client()
        ret = tron.generate_address()
        return {
            'address': ret['base58check_address'],
            'pri_key': ret['private_key'],
        }

    def pri_key_to_address(self,
                           pri_key):
        tron = self.get_lib_client()
        ret = tron.generate_address(PrivateKey.fromhex(pri_key))
        return ret['base58check_address']

    def is_address_valid(self,
                         address):
        try:
            return self.get_lib_client().is_address(address)
        except Exception as e:
            return False


class BTCChain(Chain):

    def __init__(self, network_type='mainnet'):
        if network_type:
            network_type = network_type.lower()
            if network_type not in ['mainnet', 'testnet']:
                raise NotImplementedError(
                    f'Invalid network_type, network_type={network_type}')

            self.network_type = network_type

    def is_mainnet(self):
        return self.network_type == 'mainnet'

    def get_lib_client(self):
        raise NotImplementedError

    def deploy(self):
        raise NotImplementedError

    def pri_key_to_address(self, pri_key):
        key = wif_to_key(pri_key)
        return key.address

    def generate_address(self):
        key = Key()
        return {
            'address': key.address,
            'pri_key': key.to_wif(),
        }

    def is_address_valid(self, address):
        try:
            BitcoinAddress(address, network_type='mainnet')
        except Exception as e:
            return False
        return True

    def to_valid_address(self, address):
        raise NotImplementedError


class ChainFactory:
    def get_chain(self, chain_name):
        if chain_name == CHAIN_ETHER:
            return EtherChain()
        elif chain_name == CHAIN_TRON:
            return TronChain()
        elif chain_name == CHAIN_BTC:
            return BTCChain()
        else:
            raise NotImplementedError
###############################################################


class Currency:

    def set_chain_client(self, chain_client):
        """
        Set chain client
        """
        self.chain_client = chain_client

    def decimals(self):
        """
        Return decimals of currency
        return: decimals(int)
        """
        raise NotImplementedError

    def to_human_format_amount(self, currency_format_amount):
        """
        Convert amount decimals
        params: currency_format_amount(str)
        return: human_format_amount(str)
        """
        return str(Decimal(currency_format_amount) / (10 ** self.decimals()))

    def to_currency_format_amount(self, human_format_amount):
        """
        Convert amount decimals
        params: human_format_amount(str)
        return: currency_format_amount(str)
        """
        return str(Decimal(human_format_amount) * (10 ** self.decimals()))

    def balance_of(self, address):
        """
        Return balance of address with human_format_amount
        params: address(str)
        return: balance(str)
        """
        raise NotImplementedError

    def transfer(self, from_pri_key, to_address, human_format_amount, params):
        """
        Make a transfer
        params: from_pri_key(str): Private key of sender
        params: to_address(str): Address of receiver
        params: human_format_amount(str): Transfer amount
        params: params(dict): Chain only data(Ether:gwei, gas limit)
            {
                'gas_price': 50,
                'gas_limit': 21000
            }
        return: tx_id(str): Transfer hash
        """
        raise NotImplementedError

    def get_transaction(self, tx_id):
        """
        Get transaction detail
        return: dict
        {
            'tx_id': '0x123456789',
            'block': 123,
            'from_address': '0x1234567890',
            'to_address': '0x0987654321',
            'is_status_success': True,
            'extra': {
                'gas_used': '21000'
            },
        }
        """
        raise NotImplementedError

    def get_transaction_list(self, address, start_value, params):
        """
        Get transaction list
        """
        raise NotImplementedError


class EtherCurrency(Currency):

    def get_transaction(self, tx_id):
        web3 = self.chain_client.get_lib_client()
        ret = web3.eth.getTransactionReceipt(tx_id)
        return {
            'tx_id': tx_id,
            'block_number': ret['blockNumber'],
            'from': ret['from'],
            'confirmation': web3.eth.blockNumber - ret['blockNumber'],
            'is_status_success': ret['status'] == 1,
            'extra': {
                'gas_used': ret['gasUsed'],
            }
        }


class EtherEthCurrency(EtherCurrency):

    def decimals(self):
        return 18

    def balance_of(self, address):
        web3 = self.chain_client.get_lib_client()
        balance = web3.eth.getBalance(address)
        return self.to_human_format_amount(balance)

    def transfer(self, from_pri_key, to_address, human_format_amount, params):
        if 'gas_price' not in params:
            raise Exception('gas_price not in params')

        from_address = self.chain_client.pri_key_to_address(from_pri_key)
        web3 = self.chain_client.get_lib_client()
        currency_format_amount = self.to_currency_format_amount(
            human_format_amount)
        currency_format_amount = int(float(currency_format_amount))
        transfer_params = {
            'nonce': web3.eth.getTransactionCount(from_address),
            'gasPrice': web3.toWei(str(params['gas_price']), 'gwei'),
            'to': to_address,
            'value': currency_format_amount
        }

        # 計算gas
        transfer_params['gas'] = web3.eth.estimateGas(transfer_params)

        signed_txn = web3.eth.account.signTransaction(
            transfer_params, from_pri_key)

        tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return tx_id.hex()


class EtherUSDTCurrency(EtherCurrency):

    def get_contract(self):
        web3 = self.chain_client.get_lib_client()
        with open(ETHER_USDT_ABI_PATH) as f:
            abi = json.load(f)
        return web3.eth.contract(address=ETHER_USDT_ADDRESS, abi=abi)

    def decimals(self):
        return 6

    def balance_of(self, address):
        contract = self.get_contract()
        balance = contract.functions.balanceOf(address).call()
        return self.to_human_format_amount(balance)

    def transfer(self, from_pri_key, to_address, human_format_amount, params):
        if 'gas_price' not in params:
            raise Exception('gas_price not in params')

        if 'gas_limit' not in params:
            raise Exception('gas_limit not in params')

        from_address = self.chain_client.pri_key_to_address(from_pri_key)
        web3 = self.chain_client.get_lib_client()

        # 設定發送端地址
        web3.eth.defaultAccount = from_address

        # 取得錢包合約物件
        contract = self.get_contract()

        # 檢查地址
        from_address = web3.toChecksumAddress(from_address)
        to_address = web3.toChecksumAddress(to_address)

        # 參數
        transfer_params = {
            'from': from_address,
            'nonce': web3.eth.getTransactionCount(from_address),
            'gasPrice': web3.toWei(str(params['gas_price']), 'gwei'),
            'gas': int(params['gas_limit'])
        }

        # 執行交易
        currency_format_amount = self.to_currency_format_amount(
            human_format_amount)
        currency_format_amount = int(float(currency_format_amount))
        transaction = contract.functions.transfer(to_address, currency_format_amount) \
            .buildTransaction(transfer_params)

        signed_txn = web3.eth.account.signTransaction(
            transaction, private_key=from_pri_key)

        tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return tx_id.hex()


class TronTrxCurrency(Currency):

    def balance_of(self, address):
        try:
            tron = self.chain_client.get_lib_client()
            return str(tron.get_account_balance(address))
        except AddressNotFound:
            # address is new, no transfer record
            return '0'

    def transfer(self, from_pri_key, to_address, human_format_amount, params):
        decimals = 6
        from_address = self.chain_client.pri_key_to_address(from_pri_key)
        priv_key = PrivateKey(bytes.fromhex(from_pri_key))

        tron = self.chain_client.get_lib_client()
        currency_format_amount = int(
            float(human_format_amount) * 10 ** decimals)
        txn = (
            tron.trx.transfer(from_address, to_address, currency_format_amount)
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
        )
        ret = txn.wait()
        return ret['id']


class TronUSDTCurrency(Currency):
    def get_contract(self):
        tron = self.chain_client.get_lib_client()
        return tron.get_contract(TRON_USDT_ADDRESS)

    def decimals(self):
        return 6

    def balance_of(self, address):
        contract = self.get_contract()
        balance = contract.functions.balanceOf(address)
        return self.to_human_format_amount(balance)

    def transfer(self, from_pri_key, to_address, human_format_amount, params):
        from_address = self.chain_client.pri_key_to_address(from_pri_key)
        priv_key = PrivateKey(bytes.fromhex(from_pri_key))
        currency_format_amount = self.to_currency_format_amount(
            human_format_amount)
        currency_format_amount = int(float(currency_format_amount))
        txn = (
            self.get_contract().functions.transfer(to_address, currency_format_amount)
            .with_owner(from_address)
            .build()
            .sign(priv_key)
        )

        ret = txn.broadcast()

        return ret['txid']


class BTCCurrency(Currency):

    def __init__(self, network_type='mainnet'):
        """
        :param network_type: str: 'mainnet' | 'testnet'
        """
        self.network_type = network_type

    def decimals(self):
        return 8

    def to_human_format_amount(
            self, currency_amount
    ):
        currency_amount = Decimal(currency_amount)
        return str(currency_amount / 10 ** self.decimals())

    def to_currency_format_amount(
            self, human_amount
    ):
        return str(float(human_amount) * 10 ** self.decimals())

    def balance_of(self, address):

        if self.network_type == 'mainnet':
            key = PrivateKey()
        elif self.network_type == 'testnet':
            key = PrivateKeyTestnet()
        else:
            raise Exception(
                f'network_type not in [mainnet, testnet], value={self.network_type}')

        key._address = address
        return self.to_human_format_amount(key.get_balance())


class CurrencyFactory:
    def get_currency(self, currency_name):
        if currency_name == CURRENCY_ETHER_ETH:
            return EtherEthCurrency()
        elif currency_name == CURRENCY_ETHER_USDT:
            return EtherUSDTCurrency()
        elif currency_name == CURRENCY_TRON_TRX:
            return TronTrxCurrency()
        elif currency_name == CURRENCY_TRON_USDT:
            return TronUSDTCurrency()
        elif currency_name == CURRENCY_BTC_BTC:
            return BTCCurrency()
        else:
            raise NotImplementedError
