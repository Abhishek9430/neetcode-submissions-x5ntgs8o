class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums,target):
            i=0
            j=len(nums)-1
            while i <= j:
                mid=i + (j-i)//2 ## low  + (high-low)/2
                print(mid)
                if target<nums[mid]:
                    j=mid-1
                elif target>nums[mid]:
                    i=mid+1
                else:
                    return True
            return False
        
        for row in matrix:
            res=search(row,target)
            if res:
                return res
        return False
        