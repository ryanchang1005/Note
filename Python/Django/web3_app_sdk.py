import json
import secrets

from web3 import HTTPProvider, Web3
from eth_account import Account


def get_file_name(path):
    if '/' in path:
        return path.split('/')[-1]
    else:
        return path


def read_file_content(path):
    result = ''
    with open(path, 'r') as f:
        for line in f.readlines():
            result += line
    return result


class CommonService:
    URL = 'http://127.0.0.1:8545'

    @staticmethod
    def get_web3_client():
        return Web3(HTTPProvider(CommonService.URL))

    @staticmethod
    def generate_address():
        account = Account.create(secrets.token_hex(16))
        return {
            'address': account.address,
            'private_key': account.key.hex()
        }

    @staticmethod
    def get_transaction(tx_id):
        w3 = CommonService.get_web3_client()
        ret = w3.eth.getTransactionReceipt(tx_id)
        return {
            'confirmation': w3.eth.blockNumber - ret['blockNumber'],
            'is_success': ret['status'] == 1,
            'contract_address': ret.contractAddress,
        }

    @staticmethod
    def deploy():
        w3 = CommonService.get_web3_client()
        sol_file_path = 'xxx.sol'
        pri_key = 'xxx'
        gas_price = '0'

        from solc import compile_standard
        file_name = get_file_name(sol_file_path)
        clz_name = file_name.replace('.sol', '')
        sol_content = read_file_content(sol_file_path)

        # 編譯
        compiled_sol = compile_standard({
            'language': 'Solidity',
            'sources': {
                file_name: {
                    'content': sol_content
                }
            },
            'settings': {
                'outputSelection': {
                    "*": {
                        "*": [
                            "metadata", "evm.bytecode"
                            , "evm.bytecode.sourceMap"
                        ]
                    }
                }
            }
        })

        bytecode = compiled_sol['contracts'][file_name][clz_name]['evm']['bytecode']['object']

        abi = json.loads(compiled_sol['contracts'][file_name][clz_name]['metadata'])['output']['abi']

        pre_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

        # deploy account
        account = w3.eth.account.privateKeyToAccount(pri_key)

        # constructor
        transaction = pre_contract.constructor().buildTransaction(
            {
                'gasPrice': w3.toWei(str(gas_price), 'gwei'),
                'from': account.address,
                'nonce': w3.eth.getTransactionCount(account.address)
            }
        )

        signed_txn = w3.eth.account.signTransaction(transaction, private_key=pri_key)
        ret = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f'tx_id:{ret.hex()}')
        print(f'contract_address:{w3.eth.waitForTransactionReceipt(ret).contractAddress}')

    @staticmethod
    def get_address(pri_key):
        account = Account.privateKeyToAccount(pri_key)
        return account.address


class USDtService:
    DECIMAL = 6
    CONTRACT_ABI_PATH = 'xxx.json'
    CONTRACT_ADDRESS = '0xxxx'

    @staticmethod
    def to_raw_amount(readable_amount):
        return str(int(float(readable_amount) * (10 ** USDtService.DECIMAL)))

    @staticmethod
    def to_readable_amount(raw_amount):
        return str(int(raw_amount) / (10 ** USDtService.DECIMAL))

    @staticmethod
    def get_contract():
        w3 = CommonService.get_web3_client()
        with open(USDtService.CONTRACT_ABI_PATH) as f:
            abi = json.load(f)
            return w3.eth.contract(address=w3.toChecksumAddress(USDtService.CONTRACT_ADDRESS), abi=abi)

    @staticmethod
    def get_balance(address):
        w3 = CommonService.get_web3_client()
        contract = USDtService.get_contract()
        address = w3.toChecksumAddress(address)
        raw_amount = contract.functions.balanceOf(address).call()
        return USDtService.to_readable_amount(raw_amount)

    @staticmethod
    def transfer(from_pri_key, to_address, amount, gas_price):
        w3 = CommonService.get_web3_client()

        from_address = CommonService.get_address(from_pri_key)
        to_address = w3.toChecksumAddress(to_address)

        params = {
            'from': from_address,
            'nonce': w3.eth.getTransactionCount(from_address),
            'gasPrice': w3.toWei(str(gas_price), 'gwei'),
        }

        params['gas'] = w3.eth.estimateGas(params)

        w3.eth.defaultAccount = from_address

        contract = USDtService.get_contract()

        transaction = contract.functions.transfer(to_address, int(USDtService.to_raw_amount(amount))) \
            .buildTransaction(params)

        signed_txn = w3.eth.account.signTransaction(transaction, private_key=from_pri_key)

        ret = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return ret.hex()


class EthService:
    DECIMAL = 18

    @staticmethod
    def to_raw_amount(readable_amount):
        return str(int(float(readable_amount) * (10 ** EthService.DECIMAL)))

    @staticmethod
    def to_readable_amount(raw_amount):
        return str(int(raw_amount) / (10 ** EthService.DECIMAL))

    @staticmethod
    def get_balance(address):
        w3 = CommonService.get_web3_client()
        address = w3.toChecksumAddress(address)
        raw_amount = w3.eth.getBalance(address)
        return EthService.to_readable_amount(raw_amount)

    @staticmethod
    def transfer(from_pri_key, to_address, amount, gas_price):
        w3 = CommonService.get_web3_client()

        from_address = CommonService.get_address(from_pri_key)
        to_address = w3.toChecksumAddress(to_address)

        params = {
            'nonce': w3.eth.getTransactionCount(from_address),
            'gasPrice': w3.toWei(str(gas_price), 'gwei'),
            'to': to_address,
            'value': int(EthService.to_raw_amount(amount)),
            'gas': 21000
        }

        signed_txn = w3.eth.account.signTransaction(params, from_pri_key)

        ret = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return ret.hex()
