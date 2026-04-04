class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # mem = {}
        # def costc(n):
        #     if n in mem:
        #         return mem[n]
        #     if n == 0 or n == 1:
        #         return 0
            
        #     cost_n_1 = costc(n-1) + cost[n-1]
        #     cost_n_2 = costc(n-2) + cost[n-2]
        #     mem[n] = min(cost_n_1,cost_n_2)
        #     return mem[n]
        # return costc(len(cost))
        n = len(cost)
        dp = [0]*(n+1)

        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        
        return dp[n]
        