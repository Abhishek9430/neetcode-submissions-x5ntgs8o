class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==1:
                return x
            small_pow=power(x,n-1)
            return small_pow*x
        
        def power_minus(x,n):
            if n==0:
                return 1
            small_pow=power_minus(x,n+1)
            return small_pow/x
            
        if n>0:
            val=power(x,n)
        else:
            val=power_minus(x,n)
        return val
        