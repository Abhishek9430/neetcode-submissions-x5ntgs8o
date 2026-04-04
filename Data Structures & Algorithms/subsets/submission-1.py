class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return

            # include ith number
            subset.append(nums[i])
            dfs(i+1)

            # change the decision and take decision not to include ith
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res