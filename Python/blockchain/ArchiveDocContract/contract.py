import json

from eth_account import Account
from web3 import Web3, HTTPProvider


class ArchiveDocContractService:
    WEB3_URL = 'https://ropsten.infura.io/v3/'
    CONTRACT_ADDRESS = ''
    CONTRACT_ABI_PATH = '/Users/ryan/Desktop/python/ArchiveDoc/ArchiveDoc_ABI.json'

    @staticmethod
    def get_web3_client():
        return Web3(HTTPProvider(ArchiveDocContractService.WEB3_URL))

    @staticmethod
    def get_contract(web3):
        with open(ArchiveDocContractService.CONTRACT_ABI_PATH) as f:
            abi = json.load(f)
        contract_address = web3.toChecksumAddress(ArchiveDocContractService.CONTRACT_ADDRESS)
        return web3.eth.contract(address=contract_address, abi=abi)

    @staticmethod
    def add_staff(owner_pri_key,
                  staff_address):
        try:
            web3 = ArchiveDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = ArchiveDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            staff_address = web3.toChecksumAddress(staff_address)

            transaction = contract.functions.addStaff(staff_address).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def remove_staff(owner_pri_key,
                     staff_address):
        try:
            web3 = ArchiveDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = ArchiveDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            staff_address = web3.toChecksumAddress(staff_address)

            transaction = contract.functions.removeStaff(staff_address).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def is_staff(address):
        web3 = ArchiveDocContractService.get_web3_client()

        contract = ArchiveDocContractService.get_contract(web3)

        return contract.functions.isStaff(address).call()

    @staticmethod
    def is_owner(address):
        web3 = ArchiveDocContractService.get_web3_client()

        web3.eth.defaultAccount = web3.toChecksumAddress(address)

        contract = ArchiveDocContractService.get_contract(web3)

        return contract.functions.isOwner().call()

    @staticmethod
    def add_hash(pri_key, doc_hash):
        try:
            web3 = ArchiveDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = ArchiveDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.addHash(doc_hash).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def add_multiple_hash(pri_key, doc_hash_list):
        try:
            web3 = ArchiveDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = ArchiveDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.addMultipleHash(doc_hash_list).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def is_exist(doc_hash):
        web3 = ArchiveDocContractService.get_web3_client()

        contract = ArchiveDocContractService.get_contract(web3)

        return contract.functions.isExist(doc_hash).call()
