class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        def costc(n):
            if n in mem:
                return mem[n]
            if n == 0 or n == 1:
                return 0
            
            cost_n_1 = costc(n-1) + cost[n-1]
            cost_n_2 = costc(n-2) + cost[n-2]
            mem[n] = min(cost_n_1,cost_n_2)
            return mem[n]
        return costc(len(cost))
        