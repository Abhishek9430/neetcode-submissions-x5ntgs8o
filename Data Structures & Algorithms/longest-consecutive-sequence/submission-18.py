class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ml = 0
        seen = set(nums)
        for num in nums:
            if num+1 not in seen:
                l = 0
                while num-l in seen:
                    l+=1
                ml = max(ml,l)
            seen.add(num)
        return ml
