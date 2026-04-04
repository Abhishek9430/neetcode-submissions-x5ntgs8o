class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        area=0
        while i<j:
            currArea=(j-i)*min(arr[i],arr[j])
            area=max(area,currArea)
            if arr[i]<arr[j]:
                i+=1
            elif arr[j]<arr[i]:
                j-=1
            else:
                i+=1
        return area

            
        