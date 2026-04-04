class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_price=prices[0]
        total_profit=0
        for i in range(1,len(prices)):
            price=prices[i]
            profit=price-cost_price
            total_profit=max(profit,total_profit)
            if profit<0:
                cost_price=price
                print(cost_price)
        return total_profit


        