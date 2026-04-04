class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time=[]
        for s,p in zip(speed,position):
            time=(target-p)/s
            pos_time.append([p,time])

        pos_time.sort(key=lambda x:x[0],reverse=True)
        stack=[pos_time[0][1]]
        for val in pos_time:
            if val[1]>stack[-1]:
                stack.append(val[1])
        return len(stack)
            
        