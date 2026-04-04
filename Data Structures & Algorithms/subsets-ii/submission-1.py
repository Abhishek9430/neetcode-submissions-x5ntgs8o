class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subs=[]
        nums.sort()
        def dfs(i):
            if i==len(nums):
                res.append(subs.copy())
                return
            
            if i>len(nums):
                return

            subs.append(nums[i])
            dfs(i+1)
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            subs.pop()
            dfs(i+1)
        dfs(0)
        return res

        