class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def cs(n):
            if n in mem:
                return mem[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            mem[n-1]=cs(n-1)
            mem[n-2]=cs(n-2)
            return mem[n-1]+mem[n-2]
        return cs(n)

        
        