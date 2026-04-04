class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        i=0
        j=i+1
        while j<len(prices):
            if prices[j]<=prices[i]:
                 i=j
                 j+=1
            while j<len(prices) and prices[j]>prices[i]:
                mp=max(mp,prices[j]-prices[i])
                j+=1
        return mp
        