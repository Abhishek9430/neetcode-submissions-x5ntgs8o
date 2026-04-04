class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_perms(nums):
            if len(nums)==0:
                return [[]]

            perms=get_perms(nums[1::])
            res=[]
            for p in perms:
                for i in range(len(p)+1):
                    p_copy=p.copy()
                    p_copy.insert(i,nums[0])
                    res.append(p_copy)
            return res

        return get_perms(nums)