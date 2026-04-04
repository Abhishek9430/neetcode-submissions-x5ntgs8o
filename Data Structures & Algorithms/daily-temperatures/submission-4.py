class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for day,temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                d,t=stack.pop()
                res[d]=day-d
            stack.append([day,temp])
        return res
        