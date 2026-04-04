class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        amax=0
        while i<j:
            area=(j-i)*min(arr[i],arr[j])
            amax=max(area,amax)
            if arr[i]<arr[j]:
                i+=1
            elif arr[i]>=arr[j]:
                j-=1
            
        return amax

            
        