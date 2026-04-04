class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)

        for i in range(1,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i-1])

        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i+1])

        area=0
        for i in range(len(height)):
            a=min(leftmax[i],rightmax[i])-height[i]
            if a>0:
                area+=a
        return area

# class Solution:
#     def trap(self, heights: List[int]) -> int:
#         i=0
#         j=len(heights)-1
#         lmax=heights[i]
#         rmax=heights[j]
#         area=0
#         while i<j:
#             if heights[i]>heights[j]:
#                 j-=1
#                 rmax=max(rmax,heights[j])
#             elif heights[i]<=heights[j]:
#                 i+=1
#                 lmax=max(lmax,heights[i])
#             a=min(lmax,rmax)-min(heights[i],heights[j])
#             if a>0:
#                 area+=a
#         return area
            


        