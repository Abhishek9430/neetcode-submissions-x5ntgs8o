class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_time(rate):
            time = 0
            for pile in piles:
                time+=math.ceil(pile/rate)
            return time


        i = 1 # min rate
        j = max(piles) # max rate possible

        # choosing between rates
        min_rate = float("inf")
        while i <= j:
            rate = i + (j-i)//2
            time_taken = calc_time(rate)
            if time_taken <= h: # less than target still can do better i.e. we can further reduce the rate
                min_rate = min(rate,min_rate)
                j = rate - 1
            else:
                i = rate + 1 # crossing the time limit hence need to reduce rate
            
        return min_rate

