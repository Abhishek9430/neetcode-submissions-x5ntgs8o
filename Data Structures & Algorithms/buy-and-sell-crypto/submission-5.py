class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - cp
            if profit < 0:
                cp = price
            max_profit = max(profit,max_profit)
        return max_profit