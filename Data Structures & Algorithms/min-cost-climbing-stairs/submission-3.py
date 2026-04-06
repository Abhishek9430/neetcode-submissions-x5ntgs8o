class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def climber(n):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 0
            
            cost_n_1 = climber(n-1)+cost[n-1]
            cost_n_2 = climber(n-2)+cost[n-2]
            memo[n] = min(cost_n_1,cost_n_2)
            return memo[n]
        
        n = len(cost)
        return climber(n)
        