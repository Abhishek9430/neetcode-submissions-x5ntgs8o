class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        combs=[]
        def dfs(i):
            if i>=len(nums) or sum(combs)>target:
                return
            if sum(combs)==target:
                res.append(combs.copy())
                return

            combs.append(nums[i])
            dfs(i)

            combs.pop()
            dfs(i+1)

        
        dfs(0)
        return res

        