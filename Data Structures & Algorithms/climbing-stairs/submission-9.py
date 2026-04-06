class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climber(n):
            if n in memo:
                return memo[n]
            elif n == 0 or n == 1:
                return 1
            elif n == 2:
                return 2
            
            memo[n] = climber(n-1)+climber(n-2)
            return memo[n]
        
        return climber(n)
        