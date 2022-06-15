# 來源  https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
# 兩個類別訂單與實收明細
# 當訂單金額為100, 但實收明細為50, 50或30, 30, 40分多次的
# NSum可以幫助我們找出湊到100的組合
from decimal import Decimal

class ReceviedDetail:
    """
    實收明細
    """

    def __init__(self, pub_id, amount):
        self.pub_id = pub_id
        self.amount = amount

    def __str__(self):
        return self.pub_id


class Order:
    """
    訂單
    """

    def __init__(self, pub_id, amount):
        self.pub_id = pub_id
        self.amount = amount

    def __str__(self):
        return self.pub_id


class Solution:

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                # take advantages of sorted list
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                # recursively reduce N
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNsum(nums[i+1:], target-nums[i],
                                  N-1, result+[nums[i]], results)
        return

# target = 13
# nums = [1,2,3,3,5,6,11,12]

# nums.sort()
# results = []
# for i in range(2, 6):
#     Solution().findNsum(nums, target, i, [], results)
# print(results)


def find_mapping(order, recevied_detail_list):
    # 有小數後4位, 為了方便直接轉成整數
    d = Decimal('10') ** Decimal('4')
    target = int(o1.amount * d)
    nums = [int(r.amount*d) for r in recevied_detail_list]

    # 排序
    nums.sort()

    # results是二維陣列
    results = []

    # 開始找符合的組合
    for i in range(2, 6):
        Solution().findNsum(nums, target, i, [], results)

    if len(results) == 0:
        return []

    # 找出組合長度最少的
    min_length = 999
    min_length_result = None

    for result in results:
        if len(result) < min_length:
            min_length = len(result)
            min_length_result = result

    # 用[25000,30000] 找對應的ReceviedDetail.pub_id : [R4, R5]
    # [*R1*, R2, R3, R4, R5], [25000,30000]
    # [R1, *R2*, R3, R4, R5], [25000,30000]
    # [R1, R2, *R3*, R4, R5], [25000,30000]
    # [R1, R2, R3, *R4*, R5], [25000]
    # [R1, R2, R3, R4, *R5*], []
    ret = []
    for recevied_detail in recevied_detail_list:

        # 空則結束
        if len(min_length_result) == 0:
            break

        tmp_amount = int(recevied_detail.amount * d)

        del_index = -1
        for i in range(len(min_length_result)):
            amount = min_length_result[i]
            if amount == tmp_amount:
                # 當金額相同, 紀錄ReceviedDetail.pub_id, 並記錄需刪除的index
                ret.append(recevied_detail.pub_id)
                del_index = i
        # 刪除
        if del_index != -1:
            del min_length_result[del_index]

    return ret


o1 = Order(pub_id='O20200326', amount=Decimal('5.5000'))
recevied_detail_list = [
    ReceviedDetail(pub_id='R1', amount=Decimal('1.5000')),
    ReceviedDetail(pub_id='R2', amount=Decimal('1.0000')),
    ReceviedDetail(pub_id='R3', amount=Decimal('1.0000')),
    ReceviedDetail(pub_id='R4', amount=Decimal('3.0000')),
    ReceviedDetail(pub_id='R5', amount=Decimal('2.5000')),
]

recevied_detail_mapping = find_mapping(o1, recevied_detail_list)

for it in recevied_detail_mapping:
    print(it)
