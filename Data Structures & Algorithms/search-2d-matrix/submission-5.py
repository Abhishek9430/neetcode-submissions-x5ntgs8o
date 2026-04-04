class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums,target):
            i=0
            j=len(nums)-1
            while i<=j:
                mid=i+(j-i)//2
                if nums[mid]>target:
                    j=mid-1
                elif nums[mid]<target:
                    i=mid+1
                else:
                    return True
            return False

        ### identif for which row binary search to call

        i=0
        j=len(matrix)-1
        while i<=j:
            mid=i+(j-i)//2
            if matrix[mid][-1]<target:
                i=mid+1
            elif matrix[mid][0]>target:
                j=mid-1
            else:
                break
        if not i<=j:
            return False ### all possible iteration done but no iteration we were able to find a matching row in which we could further search
        res=search(matrix[mid],target)
        return res
        

        