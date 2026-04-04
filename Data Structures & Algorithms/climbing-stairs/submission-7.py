class Solution:
    def climbStairs(self, n: int) -> int:
        # mem = {}
        # def cs(n):
        #     if n in mem:
        #         return mem[n]
        #     if n == 1 or n == 0:
        #         return 1
        #     if n == 2:
        #         return 2
            
        #     mem[n]=cs(n-1)+cs(n-2)
        #     return mem[n]
        # return cs(n)
        a=0
        b=1
        for _ in range(n):
            a,b=b,b+a
        return b



        
        