class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_time(rate):
            time_taken=0
            for pile in piles:
                time_taken+=math.ceil(pile/rate)
            return time_taken

        
        i=1
        j=max(piles)
        final_rate = float("inf")
        while i<=j:
            rate = i + (j-i)//2
            time_taken = calc_time(rate)
            
            if time_taken <= h:
                final_rate = min(final_rate,rate)
                j = rate - 1
            else:
                i = rate + 1
        return final_rate


        