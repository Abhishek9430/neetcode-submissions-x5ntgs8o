class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        days=[0]*len(temperatures)

        i=0
        while i<len(temperatures):
            while stack and stack[-1][1]<temperatures[i]:
                prev_day,prev_temp=stack.pop()
                days[prev_day]=i-prev_day


            stack.append([i,temperatures[i]])
            i+=1

        return days
        