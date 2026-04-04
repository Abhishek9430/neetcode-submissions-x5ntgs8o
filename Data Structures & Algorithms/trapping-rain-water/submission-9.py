class Solution:
    def trap(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        lmax=heights[i]
        rmax=heights[j]
        area=0
        while i<j:
            if heights[i]>heights[j]:
                j-=1
                rmax=max(rmax,heights[j])
            elif heights[i]<=heights[j]:
                i+=1
                lmax=max(lmax,heights[i])
            a=min(lmax,rmax)-min(heights[i],heights[j])
            if a>0:
                area+=a
        return area
            

