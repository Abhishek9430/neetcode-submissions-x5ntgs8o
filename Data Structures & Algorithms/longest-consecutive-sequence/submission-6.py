class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums)
        res=0
        for num in nums:
            if (num-1) not in lookup:
                streak=1
                while num+streak in lookup:
                    streak+=1
                res=max(res,streak)
        return res



        