class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lhm,rhm=0,0

        area=0
        while i<j:
            if height[i] < height[j]:
                lhm=max(lhm,height[i])
                area+=lhm-height[i]
                i+=1
            elif height[i]>=height[j]:
                rhm=max(rhm,height[j])
                area+=rhm-height[j]
                j-=1
        return area


        

        
        