class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_time=[]
        for pos,spd in zip(position,speed):
            pos_time.append([pos,(target-pos)/spd])

        pos_time.sort(key=lambda x: x[0],reverse=True)

        stack=[pos_time[0][1]]
        for pt in pos_time:
            if pt[1]>stack[-1]:
                stack.append(pt[1])

        return len(stack)
            
        