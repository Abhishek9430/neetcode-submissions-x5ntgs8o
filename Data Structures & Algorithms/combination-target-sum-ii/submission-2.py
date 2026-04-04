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

            # chose to take the element since this element does not
            # need to be consider again thus move ahead after choosing

            combs.append(candidates[i])
            dfs(i+1,total+candidates[i])

            # change the decision to choose this element and move ahead
            combs.pop()
            while i+1<len(candidates) and candidates[i] ==  candidates[i+1]:
                i+=1

            dfs(i+1,total)

        dfs(0,0)
        return res
        