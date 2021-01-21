import json
from web3 import (
    HTTPProvider,
    Web3,
)


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


def deploy():
    url = 'https://ropsten.infura.io/v3/'
    sol_path = '/Users/ryan/Desktop/python/AuditDocContract/AuditDoc.sol'
    pri_key = ''

    web3 = Web3(HTTPProvider(url))

    from solc import compile_standard
    file_name = get_file_name(sol_path)
    clz_name = file_name.replace('.sol', '')
    sol_content = read_file_content(sol_path)

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
                        "metadata", "evm.bytecode", "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
    })

    bytecode = compiled_sol['contracts'][file_name][clz_name]['evm']['bytecode']['object']

    abi = json.loads(compiled_sol['contracts'][file_name][clz_name]['metadata'])[
        'output']['abi']

    pre_contract = web3.eth.contract(abi=abi, bytecode=bytecode)

    # 設定部署的帳號
    account = web3.eth.account.privateKeyToAccount(pri_key)

    # 傳遞建構式參數(1e)
    # transaction = pre_contract.constructor(1000000000000, 'fusdt3', 'fusdt3', 6).buildTransaction(
    #     {
    #         'gasPrice': web3.toWei('30', 'gwei'),
    #         'from': account.address,
    #         'nonce': web3.eth.getTransactionCount(account.address)
    #     }
    # )
    transaction = pre_contract.constructor().buildTransaction(
        {
            'gasPrice': web3.toWei('30', 'gwei'),
            'from': account.address,
            'nonce': web3.eth.getTransactionCount(account.address)
        }
    )

    signed_txn = web3.eth.account.signTransaction(
        transaction, private_key=pri_key)
    data = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    print(f'Create contract tx_id={data.hex()}')


if __name__ == "__main__":
    deploy()
