class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        ml=0
        for num in nums:
            if not num-1 in seen:
                streak=1
                while num+streak in seen:
                    streak+=1
                ml=max(streak,ml)
        return ml
