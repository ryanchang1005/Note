"""
Jump Game


bottom-up
    用變數m去存當前可以走到的最大index, m = max(m, i + A[i])
    如當前位置超過m, 則代表抵達不了, 例如[2, 1, 0, 4]
    在i=0時, m為2
    在i=1時, m為2
    在i=2時, m為2
    在i=3時, m為2 (不可能抵達m, 所以 i > m return false)

top-down
    用變數last_index = len(A) - 1存最後的index
    從倒數第二個index開始, 如 i + A[i] >= last_index OK, 將last_index換成i(OK代表i是可以走到last_index, 下一圈檢查前一個可不可以走道此i位置)
    最後判斷last_index == 0, 如不等於代表起點(index = 0)到不了last_index
"""


def bottom_up(A):
    m = 0

    for i in range(len(A)):
        if i > m:
            return False
        m = max(m, i + A[i])
    return True


def top_down(A):
    last_index = len(A) - 1
    for i in range(last_index - 1, -1, -1):
        if i + A[i] >= last_index:
            last_index = i
    return last_index == 0


if __name__ == '__main__':
    print(bottom_up([2, 3, 1, 1, 4]))  # True
    print(top_down([2, 3, 1, 1, 4]))  # True

    print(bottom_up([3, 2, 1, 0, 4]))   # False
    print(top_down([3, 2, 1, 0, 4]))    # False
