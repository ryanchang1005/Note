"""
Top K Frequent Elements
找出前K常出現的元素

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

先put進map, 並加總, mapping結果為 "值":"出現次數"
{
    1: 3,  # 1出現3次
    2: 2,
    3: 1
}
再將map轉成array形式, 初始化所有array值為0, array的index為"出現的次數", 值為"出現的值", [0, 3, 5] >> 出現1次的有3, 出現2次的有5
最後從尾段找array不為None的前K個值, 並輸出
"""


def run(nums, K):
    freq_map = {}
    freq_list = [None for _ in range(len(nums) + 1)]
    for n in nums:
        if n not in freq_map:
            freq_map[n] = 0
        freq_map[n] += 1
    for k, v in freq_map.items():
        if v not in freq_list:
            freq_list[v] = []
        freq_list[v].append(k)

    ret = []
    for i in range(len(freq_list) - 1, -1, -1):
        it = freq_list[i]
        if it:
            ret += it
            if len(ret) >= K:
                break
    return ret


if __name__ == '__main__':
    print(run([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(run([1, 1, 1, 1, 2, 2, 3, 4, 4, 4], 3))  # [1, 4, 2]
    print(run([1], 1))  # [1]
