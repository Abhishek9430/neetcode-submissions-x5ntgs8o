class Solution:
    def trap(self, height: List[int]) -> int:
        # min(lh,rh)-height[i]

        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1],height[i-1])

        for j in range(len(height)-2,-1,-1):
            rightmax[j] = max(rightmax[j+1],height[j+1]) 

        amax = 0
        for k in range(len(height)):
            a = min(leftmax[k],rightmax[k])-height[k]
            if a > 0:
                amax+=a
        
        return amax
