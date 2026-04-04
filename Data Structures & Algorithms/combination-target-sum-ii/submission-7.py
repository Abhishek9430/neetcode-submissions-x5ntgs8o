class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        combs=[]
        candidates.sort()
        def dfs(i,total):
            if total>target:
                return
            if total==target:
                res.append(combs.copy())
                return
            if i>=len(candidates):
                return


            combs.append(candidates[i])
            dfs(i+1,total+candidates[i])

            # remove duplicates
            combs.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            dfs(i+1,total)
        dfs(0,0)
        return res
        