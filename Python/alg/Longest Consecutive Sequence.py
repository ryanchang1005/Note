"""
Longest Consecutive Sequence
找出最長連續序列

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4 [1, 2, 3, 4]

Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9 [0, 1, 2, 3, 4, 5, 6, 7, 8]

先將nums放到set中
開始遍歷nums:
    如num在set中, 開始往上往下找(while)並且刪除那些值的set, 並計算比較高度最大值(高值-低值)

"""


def run(A):
    longest_length = -1

    l = set()
    for it in A:
        l.add(it)

    for i in range(len(A)):
        num = A[i]
        if num in l:
            l.remove(num)
            left = num - 1
            right = num + 1
            while left in l:
                l.remove(left)
                left -= 1
            while right in l:
                l.remove(right)
                right += 1
            longest_length = max(longest_length, right - left - 1)  # 會高估需-1

    return longest_length


if __name__ == '__main__':
    print(run([100, 4, 200, 1, 3, 2]))  # 4
    print(run([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
