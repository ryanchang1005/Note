"""
Maximum Subarray
最大子數列問題

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

DP(不要去算已經算過的值)
    [-2, 1,-3, 4]
    -2 : dp=[0,0,0,0]
    1 : "1 vs -1(-2+1) >> 1 win", dp=[0,1,0,0]
    -3 : "-3 vs -2(1(previous computed)+(-3)) >> -2 win", dp=[0,1,-2,0]
    4 : "4 vs 2(-2+4) >> 4 win", dp[0,1,0,4]
    return max(dp)
    dp[i] = max(A[i], dp[i-1]+A[i])

"""


def run(A):
    dp = [0 for _ in A]
    dp[0] = A[0]

    for i in range(1, len(A)):
        dp[i] = max(A[i], dp[i-1] + A[i])

    return max(dp)


if __name__ == '__main__':
    print(run([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(run([-3, -2, 4, -1, 5, -1, -7]))  # 8
