class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        lmax = 0
        for i in range(len(nums)):
            if nums[i]+1 not in numset:
                l = 0          
                while nums[i]-l in numset:
                    l+=1
                lmax=max(lmax,l)
        return lmax




             