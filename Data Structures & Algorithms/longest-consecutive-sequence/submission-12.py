class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maxs=0
        for n in nums:
            if n-1 not in seen:
                streak=1
                while n+streak in seen:
                    streak+=1
                maxs=max(maxs,streak)
        return maxs
        