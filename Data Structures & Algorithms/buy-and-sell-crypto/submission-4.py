class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_price = float("inf")
        profit = 0
        for cp in prices:
            small_profit=cp-cost_price
            profit=max(small_profit,profit)
            if small_profit < 0:
                cost_price = cp
        return profit

        