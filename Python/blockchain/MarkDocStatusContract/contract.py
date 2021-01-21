import json

from eth_account import Account
from web3 import Web3, HTTPProvider


class MarkDocStatusContractService:
    WEB3_URL = 'https://ropsten.infura.io/v3/'
    CONTRACT_ADDRESS = ''
    CONTRACT_ABI_PATH = '/Users/ryan/Desktop/python/MarkDocStatusContract/MarkDocStatus_ABI.json'

    DOC_STATUS_NONE = '0'   # 預設狀態
    DOC_STATUS_VERIFY = '1'  # 核可
    DOC_STATUS_REFUSE = '2'  # 拒絕
    DOC_STATUS_REVOKE = '3'  # 撤回

    @staticmethod
    def get_web3_client():
        return Web3(HTTPProvider(MarkDocStatusContractService.WEB3_URL))

    @staticmethod
    def get_contract(web3):
        with open(MarkDocStatusContractService.CONTRACT_ABI_PATH) as f:
            abi = json.load(f)
        contract_address = web3.toChecksumAddress(
            MarkDocStatusContractService.CONTRACT_ADDRESS)
        return web3.eth.contract(address=contract_address, abi=abi)

    @staticmethod
    def add_staff(owner_pri_key,
                  staff_address):
        try:
            web3 = MarkDocStatusContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = MarkDocStatusContractService.get_contract(web3)

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
            web3 = MarkDocStatusContractService.get_web3_client()

            account = Account.privateKeyToAccount(owner_pri_key)

            web3.eth.defaultAccount = account.address

            contract = MarkDocStatusContractService.get_contract(web3)

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
        web3 = MarkDocStatusContractService.get_web3_client()

        contract = MarkDocStatusContractService.get_contract(web3)

        return contract.functions.isStaff(address).call()

    @staticmethod
    def is_owner(address):
        web3 = MarkDocStatusContractService.get_web3_client()

        web3.eth.defaultAccount = web3.toChecksumAddress(address)

        contract = MarkDocStatusContractService.get_contract(web3)

        return contract.functions.isOwner().call()

    @staticmethod
    def add_doc(pri_key, doc_id):
        """
        新增文件
        pri_key: str : 新增文件的人的私鑰
        doc_id: str : 文件id
        """
        try:
            web3 = MarkDocStatusContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = MarkDocStatusContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.addDoc(doc_id).buildTransaction(params)

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
        web3 = MarkDocStatusContractService.get_web3_client()
        contract = MarkDocStatusContractService.get_contract(web3)
        return contract.functions.isDocExist(doc_id).call()

    @staticmethod
    def set_doc_status(pri_key, doc_id, status):
        """
        設定文件狀態
        doc_id: str : 文件id
        status: str : 狀態(MarkDocStatusContractService.DOC_STATUS)
        """
        try:
            web3 = MarkDocStatusContractService.get_web3_client()

            account = Account.privateKeyToAccount(pri_key)

            web3.eth.defaultAccount = account.address

            contract = MarkDocStatusContractService.get_contract(web3)

            params = {
                'from': account.address,
                'nonce': web3.eth.getTransactionCount(account.address),
                'gasPrice': web3.toWei('50', 'gwei')
            }

            transaction = contract.functions.setDocStatus(doc_id, status).buildTransaction(params)

            signed_txn = web3.eth.account.signTransaction(
                transaction, private_key=account.privateKey)
            tx_id = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return tx_id.hex()
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def get_doc_status(doc_id):
        """
        取得文件狀態
        doc_id: str : 文件id
        return: str : 狀態(MarkDocStatusContractService.DOC_STATUS)
        """
        web3 = MarkDocStatusContractService.get_web3_client()
        contract = MarkDocStatusContractService.get_contract(web3)
        return contract.functions.getDocStatus(doc_id).call()
