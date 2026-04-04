class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        area=0
        while i<j:
            # area=lxb=min(arr[i],arr[j])*j-i
            area=max((min(arr[i],arr[j])*(j-i)),area)
            if arr[i]<arr[j]:
                i+=1
            elif arr[j]<arr[i]:
                j-=1
            else:
                i+=1 # since both are equal extend any one
        return area

        