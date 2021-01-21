import json

from eth_account import Account
from web3 import Web3, HTTPProvider


class AuditDocContractService:
    WEB3_URL = 'https://ropsten.infura.io/v3/'
    CONTRACT_ADDRESS = ''
    CONTRACT_ABI_PATH = '/Users/ryan/Desktop/python/AuditDocContract/AuditDoc_ABI.json'

    @staticmethod
    def get_web3_client():
        return Web3(HTTPProvider(AuditDocContractService.WEB3_URL))

    @staticmethod
    def get_contract(web3):
        with open(AuditDocContractService.CONTRACT_ABI_PATH) as f:
            abi = json.load(f)
        contract_address = web3.toChecksumAddress(
            AuditDocContractService.CONTRACT_ADDRESS)
        return web3.eth.contract(address=contract_address, abi=abi)

    @staticmethod
    def add_staff(owner_pri_key,
                  staff_address):
        try:
            web3 = AuditDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = AuditDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            staff_address = web3.toChecksumAddress(staff_address)

            transaction = contract.functions.addStaff(
                staff_address).buildTransaction(params)

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
            web3 = AuditDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = AuditDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            staff_address = web3.toChecksumAddress(staff_address)

            transaction = contract.functions.removeStaff(
                staff_address).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def is_staff(address):
        web3 = AuditDocContractService.get_web3_client()

        contract = AuditDocContractService.get_contract(web3)

        return contract.functions.isStaff(address).call()

    @staticmethod
    def is_owner(address):
        web3 = AuditDocContractService.get_web3_client()

        web3.eth.defaultAccount = web3.toChecksumAddress(address)

        contract = AuditDocContractService.get_contract(web3)

        return contract.functions.isOwner().call()

    @staticmethod
    def add_doc(pri_key, doc_id, auditor_address_list):
        """
        新增文件
        pri_key: str : 新增文件的人的私鑰
        doc_id: str : 文件id
        auditor_address_list: str list : 審核人地址陣列
        """
        try:
            web3 = AuditDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = AuditDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.addDoc(
                doc_id, auditor_address_list).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def is_doc_exist(doc_id):
        """
        文件是否存在
        doc_id: str : 文件id
        return: bool
        """
        web3 = AuditDocContractService.get_web3_client()

        contract = AuditDocContractService.get_contract(web3)

        return contract.functions.isDocExist(doc_id).call()

    @staticmethod
    def is_doc_finish(doc_id):
        """
        文件是否已審核完
        doc_id: str : 文件id
        return: bool
        """
        web3 = AuditDocContractService.get_web3_client()

        contract = AuditDocContractService.get_contract(web3)

        return contract.functions.isDocFinish(doc_id).call()

    @staticmethod
    def audit(pri_key, doc_id, hash):
        """
        審核
        pri_key: str : 新增文件的人的私鑰
        doc_id: str : 文件id
        hash: str : 審核內容的hash
        """
        try:
            web3 = AuditDocContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = AuditDocContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.audit(
                doc_id, hash).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def is_audit_hash_valid(doc_id, auditor_address, _hash):
        """
        審核內容是否有效
        doc_id: str : 文件id
        auditor_address: str : 審核人地址
        hash: str : 審核內容的hash
        return: bool
        """
        web3 = AuditDocContractService.get_web3_client()

        contract = AuditDocContractService.get_contract(web3)

        return contract.functions.isAuditHashValid(doc_id, auditor_address, _hash).call()
