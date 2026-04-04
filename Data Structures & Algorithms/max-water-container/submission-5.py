class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        area = 0
        while i < j:
            small_area = min(heights[i],heights[j])*(j-i)
            area=max(area,small_area)
            if heights[i] <  heights[j]:
                i+=1
            elif heights[i] >= heights[j]:
                j-=1
        
        return area



        