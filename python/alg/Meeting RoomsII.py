"""
Meeting RoomsII
找出最少需要幾個會議室

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1


三種解法
1.用兩個陣列起始和結束 + 兩個指標
2.將intervals先存入map中(自帶或事後排序)開始+1結束-1, 依序遍歷map, 加總值並在途中取最大值
3.用最小堆
"""


def solve2(intervals):
    m = {}

    # 放到map中
    for it in intervals:
        if it[0] not in m:
            m[it[0]] = 0
        m[it[0]] += 1

        if it[1] not in m:
            m[it[1]] = 0
        m[it[1]] -= 1

    tmp = 0
    res = 0
    for k in sorted(m.keys()):
        tmp += m[k]
        res = max(res, tmp)
    return res


if __name__ == '__main__':
    print(solve2([[0, 30], [5, 10], [15, 20]]))  # 2
    print(solve2([[7, 10], [2, 4]]))  # 1
    print(solve2([[1, 3], [2, 4], [5, 8], [6, 9], [7, 10]]))  # 3
