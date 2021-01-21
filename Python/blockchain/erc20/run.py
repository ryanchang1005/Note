from factory import *

if __name__ == "__main__":
    # get chain
    chain_factory = ChainFactory()
    chain_client = chain_factory.get_chain(CHAIN_TRON)

    # get currency
    currency_factory = CurrencyFactory()
    currency_client = currency_factory.get_currency(CURRENCY_TRON_TRX)

    # bind chain and currency
    currency_client.set_chain_client(chain_client)

    # # generate_address
    # ret = chain_client.generate_address()
    # print(ret)

    # # is_address_valid
    # ret = chain_client.is_address_valid('')
    # print(ret)

    # # pri_key_to_address
    # ret = chain_client.pri_key_to_address('')
    # print(ret)

    # # to_valid_address
    # ret = chain_client.to_valid_address('')
    # print(ret)

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
