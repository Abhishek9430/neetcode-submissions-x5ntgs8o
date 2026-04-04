class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            # change your choie
            subset.pop()
            dfs(i+1)

            # always next element since we dont want to indue duplicates

        dfs(0)
        return res

        