class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            small_pow=power(x*x,n//2)
            return small_pow*x if n%2!=0 else small_pow

        val=power(x,abs(n))
        return val if n>=0 else 1/val
        