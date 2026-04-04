class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTime(rate):
            time_taken=0
            for pile in piles:
                time_taken+=math.ceil(pile/rate)
            return time_taken


        i=1
        j=max(piles)
        final_rate=float("inf")
        while i<=j:
            rate=i+(j-i)//2
            time_taken=calcTime(rate)
            if time_taken<=h:
                final_rate=min(rate,final_rate)
                j=rate-1
            elif time_taken>h:
                i=rate+1
        return final_rate




        