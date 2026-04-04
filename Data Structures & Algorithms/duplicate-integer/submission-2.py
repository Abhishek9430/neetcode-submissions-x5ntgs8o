class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for val in nums:
            if val in d:
                return True
            else:
                d[val]='test'
        return False