class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        combs=[]
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(combs.copy())
                return
            if i>=len(candidates) or total>target:
                return


            combs.append(candidates[i])
            dfs(i+1,total+candidates[i])

            # remove duplicates
            combs.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1

            dfs(i+1,total)
        dfs(0,0)
        return res
        