"""
Best Time to Buy and Sell Stock
買股票最大的利益

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0

最小買點 min_price = prices[0]
最大利益 max_profit = 0
遍歷prices, 從i=1開始, 取最小買點, 算出利益, 取利益最大值
"""


def run(prices):
    if len(prices) == 0:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)

    return max_profit


if __name__ == '__main__':
    print(run([7, 1, 5, 3, 6, 4]))  # 5
    print(run([7, 6, 4, 3, 1]))  # 0
    print(run([1, 4, 2, 10]))  # 9
