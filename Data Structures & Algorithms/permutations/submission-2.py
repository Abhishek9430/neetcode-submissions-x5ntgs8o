class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_perms(nums):
            if len(nums) == 0:
                return [[]]

            perms = get_perms(nums[1::])
            res = []
            for perm in perms:
                for i in range(len(perm)+1):
                    pcopy = perm.copy()
                    pcopy.insert(i,nums[0])
                    res.append(pcopy)
            return res
        return get_perms(nums)


        