class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        cp=prices[0]
        for i in range(1,len(prices)):
            sp=prices[i]
            if sp>cp:
                profit=max(sp-cp,profit)
            else:
                cp=prices[i]

        return profit
        