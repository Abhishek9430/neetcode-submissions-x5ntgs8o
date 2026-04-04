class Solution:
    def trap(self, heights: List[int]) -> int:
        leftmax=[0]*len(heights)
        rightmax=[0]*len(heights)

        leftmax[0]=heights[0]
        rightmax[-1]=heights[-1]

        for i in range(1,len(heights)):
            leftmax[i]=max(leftmax[i-1],heights[i])
        
        for i in range(len(heights)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],heights[i])
        
        amax=0
        for i in range(len(heights)):
            area=min(leftmax[i],rightmax[i])-heights[i]
            if area>0:
                amax+=area
        return amax

