class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTime(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            return time

        i=1
        j=max(piles)
        res=float("inf")
        while i<=j:
            rate=i+(j-i)//2
            time_taken=calcTime(rate)
            if time_taken<=h:
                res=min(res,rate)
                j=rate-1
            elif time_taken>h:
                i=rate+1
        return res





        