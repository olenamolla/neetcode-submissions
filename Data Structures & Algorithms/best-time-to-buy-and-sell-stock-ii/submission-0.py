class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            sum_profit = prices[i+1] - prices[i]
            if sum_profit > 0:
                profit += sum_profit

        return profit