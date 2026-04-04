class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        res=[0]*len(temperatures)
        i=0
        while i < len(temperatures):
            while stack and stack[-1][0]<temperatures[i]:
                prev_temp,prev_day=stack.pop()
                res[prev_day]=i-prev_day

            stack.append([temperatures[i],i])
            i+=1
        return res
        