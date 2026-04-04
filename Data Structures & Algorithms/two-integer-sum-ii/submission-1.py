class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]+arr[j]>target:
                j-=1
            elif arr[i]+arr[j]<target:
                i+=1
            else:
                return [i+1,j+1]
        