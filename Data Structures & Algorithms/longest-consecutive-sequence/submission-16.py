class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        lmax=0
        for num in nums:
            if num-1 not in seen:
                start=num
                while start in seen:
                    start+=1
                lmax=max(lmax,start-num)
        return lmax
                

             