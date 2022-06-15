"""
Maximum Product Subarray
找出最大連續的乘積

Input: nums = [2,3,-2,4]
Output: 6

Input: nums = [-2,0,-1]
Output: 0

DP
    初始化dp[0] = nums[0], mx = nums[0], mn = nums[0]
    從i = 1遍歷, 宣告暫時的mx和mn, tmax/tmin
    因為需考慮到負號
    mx = max(nums[i] * tmax, nums[i] * tmin, nums[i])  # 目前最大值乘上當前值, 目前最小值乘上當前值, 當前值之間取最大
    mn = min(nums[i] * tmax, nums[i] * tmin, nums[i])  # 目前最大值乘上當前值, 目前最小值乘上當前值, 當前值之間取最小
    res = max(res, mx)
    return res
"""
