class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_time=[(p,int(target-p)/s) for p,s in zip(position,speed)]
        pos_time.sort(reverse=True)
        stack=[pos_time[0][1]]
        for pt in pos_time:
            if pt[1]>stack[-1]:
                stack.append(pt[1])
            
        return len(stack)

        