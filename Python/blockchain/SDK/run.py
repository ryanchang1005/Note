from factory import *


def test_testnet_btc():
    # get chain
    chain_client = ChainFactory().get_chain(CHAIN_BTC)
    chain_client.network_type = 'testnet'

    # get currency
    currency_client = CurrencyFactory().get_currency(CURRENCY_BTC_BTC)
    currency_client.network_type = 'testnet'

    # bind chain and currency
    currency_client.set_chain_client(chain_client)

    assert chain_client.is_address_valid(
        '1PANM2i1Vv6qxxYEktzfDWzmC9TBx9US2a') == False  # False

    assert chain_client.is_address_valid(
        'n17ZzDCSJkNvJufGNBqi7UDtzwRbuwU8My') == True  # True

    assert Decimal(currency_client.balance_of(
        'n17ZzDCSJkNvJufGNBqi7UDtzwRbuwU8My')) > 0  # True

    # # Transfer
    # tx_id = currency_client.transfer(
    #     from_pri_key='',
    #     to_address='',
    #     human_format_amount='0.00000005',
    # )
    # print(f'tx_id={tx_id}')

    print(currency_client.get_transaction(
        ''))

    print('ok, test_testnet_btc')


def test_mainnet_btc():
    # get chain
    chain_client = ChainFactory().get_chain(CHAIN_BTC)
    chain_client.network_type = 'mainnet'

    # get currency
    currency_client = CurrencyFactory().get_currency(CURRENCY_BTC_BTC)
    currency_client.network_type = 'mainnet'

    # bind chain and currency
    currency_client.set_chain_client(chain_client)

    assert chain_client.is_address_valid(
        '') == True  # True

    assert chain_client.is_address_valid(
        '') == False  # False

    print(currency_client.get_transaction(
        ''))

    print('ok, test_mainnet_btc')


if __name__ == "__main__":
    # test_testnet_btc()
    test_mainnet_btc()

    # # balance of
    # ret = currency_client.balance_of('')
    # print(ret)

    # # transfer
    # params = {
    #     'gas_price': 50,
    #     'gas_limit': 60000,
    # }
    # ret = currency_client.transfer(
    #     from_pri_key='xxx',
    #     to_address='xxx',
    #     human_format_amount='100',
    #     params=None
    # )
    # print(ret)
