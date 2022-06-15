import requests

from decimal import Decimal


class BlockchairService:
    MAIN_URL = 'https://api.blockchair.com/bitcoin'
    TEST_URL = 'https://api.blockchair.com/bitcoin/testnet'

    @classmethod
    def get_transaction(cls, tx_id):
        url = cls.MAIN_URL + f'/raw/transaction/{tx_id}'
        rsp = requests.get(url)

        if rsp.status_code != 200:
            return False, f'rsp.status_code={rsp.status_code}'

        data = rsp.json()
        print(data)
        raw_tx = data['data'][tx_id]['decoded_raw_transaction']
        vout0 = raw_tx['vout'][0]
        vout1 = raw_tx['vout'][1]

        from_address = vout1['scriptPubKey']['addresses'][0]
        to_address = vout0['scriptPubKey']['addresses'][0]
        amount = '%.08f' % round(Decimal(vout0['value']), 8)

        return True, {
            'tx_id': tx_id,
            'from_address': from_address,
            'to_address': to_address,
            'amount': amount,
        }

    @classmethod
    def get_transaction_test(cls, tx_id):
        url = cls.TEST_URL + f'/raw/transaction/{tx_id}'
        rsp = requests.get(url)

        if rsp.status_code != 200:
            return False, f'rsp.status_code={rsp.status_code}'

        data = rsp.json()
        raw_tx = data['data'][tx_id]['decoded_raw_transaction']
        vout0 = raw_tx['vout'][0]
        vout1 = raw_tx['vout'][1]

        from_address = vout1['scriptPubKey']['addresses'][0]
        to_address = vout0['scriptPubKey']['addresses'][0]
        amount = '%.08f' % round(Decimal(vout0['value']), 8)

        return True, {
            'tx_id': tx_id,
            'from_address': from_address,
            'to_address': to_address,
            'amount': amount,
        }


class BTCApiService:
    GET_TX_FUNC = [
        BlockchairService.get_transaction
    ]

    GET_TX_TEST_FUNC = [
        BlockchairService.get_transaction_test
    ]

    @classmethod
    def get_transaction(cls, tx_id):
        for func in cls.GET_TX_FUNC:
            try:
                return func(tx_id)
            except Exception as e:
                print(str(e))
                continue
        return False, 'all error'

    @classmethod
    def get_transaction_test(cls, tx_id):
        for func in cls.GET_TX_TEST_FUNC:
            try:
                return func(tx_id)
            except Exception as e:
                continue
        return False, 'all error'
