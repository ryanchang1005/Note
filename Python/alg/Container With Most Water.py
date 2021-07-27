"""
Container With Most Water
以左右支柱為一個範圍, 計算如何裝多水(寬 x 支柱短的)

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

用雙指標內, 如左邊小下一圈則將左往右反之
"""


def run(A):
    l = 0
    r = len(A) - 1
    ret = 0
    while l < r:
        width = r - l
        if A[l] < A[r]:
            val = width * A[l]
            ret = max(ret, val)
            l += 1
        else:
            val = width * A[r]
            ret = max(ret, val)
            r -= 1

    return ret


if __name__ == '__main__':
    print(run([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(run([1, 1]))  # 1
    print(run([4, 3, 2, 1, 4]))  # 16
