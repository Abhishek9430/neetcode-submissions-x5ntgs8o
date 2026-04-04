class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lm,rm=0,0
        area=0
        while i<j:
            lm=max(lm,height[i])
            rm=max(rm,height[j])
            if lm<rm:
                area+=lm-height[i]
                i+=1
            elif rm<=lm:
                area+=rm-height[j]
                j-=1
        return area
        