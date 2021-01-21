from contract import ArchiveDocContractService

OWNER_ADDRESS = ''
OWNER_PRI_KEY = ''

STAFF_ADDRESS = ''
STAFF_PRI_KEY = ''

TEST_HASH = ''
TEST_HASH_LIST = ['',
                  '',
                  '']


def test_is_owner():
    is_owner = ArchiveDocContractService.is_owner(OWNER_ADDRESS)
    assert is_owner
    print(f'{OWNER_ADDRESS} is owner')

    is_owner = ArchiveDocContractService.is_owner(STAFF_ADDRESS)
    assert not is_owner
    print(f'{STAFF_ADDRESS} is not owner')


def test_add_staff():
    tx_id = ArchiveDocContractService.add_staff(OWNER_PRI_KEY,
                                                STAFF_ADDRESS)

    if tx_id is None:
        print('ArchiveDocContractService.add_staff fail')
        return
    else:
        print(f'ArchiveDocContractService.add_staff success, tx_id={tx_id}')

    # 1.wait transaction success
    # 2.execute ArchiveDocContractService.is_staff
    # is_staff = ArchiveDocContractService.is_staff(STAFF_ADDRESS)
    # assert is_staff


def test_remove_staff():
    tx_id = ArchiveDocContractService.remove_staff(OWNER_PRI_KEY,
                                                   STAFF_ADDRESS)

    if tx_id is None:
        print('ArchiveDocContractService.add_staff fail')
        return
    else:
        print(f'ArchiveDocContractService.add_staff success, tx_id={tx_id}')

    # 1.wait transaction success
    # 2.execute ArchiveDocContractService.is_staff
    # is_staff = ArchiveDocContractService.is_staff(STAFF_ADDRESS)
    # assert not is_staff


def test_is_staff():
    is_staff = ArchiveDocContractService.is_staff(OWNER_ADDRESS)
    print(f'{OWNER_ADDRESS} = {is_staff}')

    is_staff = ArchiveDocContractService.is_staff(STAFF_ADDRESS)
    print(f'{STAFF_ADDRESS} = {is_staff}')


def test_add_hash():
    tx_id = ArchiveDocContractService.add_hash(OWNER_PRI_KEY,
                                               TEST_HASH)
    if tx_id is None:
        print('ArchiveDocContractService.add_hash fail')
        return
    else:
        print(f'ArchiveDocContractService.add_hash success, tx_id={tx_id}')


def test_add_multiple_hash():
    tx_id = ArchiveDocContractService.add_multiple_hash(OWNER_PRI_KEY,
                                                        TEST_HASH_LIST)
    if tx_id is None:
        print('ArchiveDocContractService.add_multiple_hash fail')
        return
    else:
        print(f'ArchiveDocContractService.add_multiple_hash success, tx_id={tx_id}')


def test_is_exist():
    is_exist = ArchiveDocContractService.is_exist('')
    print(f'{TEST_HASH} : {is_exist}')


if __name__ == '__main__':
    test_add_multiple_hash()
