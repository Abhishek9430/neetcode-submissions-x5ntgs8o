class Solution:
    def maxArea(self, heights: List[int]) -> int:
            
        i=0
        j=len(heights)-1
        ma=0
        while i<j:
            area=min(heights[i],heights[j])*(j-i)
            ma=max(area,ma)
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>=heights[j]:
                j-=1
        return ma
            

