class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        cost_price=prices[0]
        for i in range(1,len(prices)):
            curr_profit=prices[i]-cost_price
            maxprofit=max(curr_profit,maxprofit)
            if curr_profit<0:
                cost_price=prices[i]
        return maxprofit
        