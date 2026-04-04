class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)

        for index in range(1,len(height)):
            leftmax[index]=max(leftmax[index-1],height[index-1])
        
        for index in range(len(height)-2,-1,-1):
            rightmax[index]=max(rightmax[index+1],height[index+1])

        area=0
        for index,val in enumerate(height):
            a=min(leftmax[index],rightmax[index])-val
            if a>0:
                area+=a
        return area


        

        
        