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

        ###  indentify which row to search for using binary serach
        i=0
        j=len(matrix)-1
        res=False
        while i <=j:
            midr=i + (j-i)//2
            print("i,j",i,j,"midrow",midr)
            if matrix[midr][-1]<target:
                i=midr+1
            elif matrix[midr][0]>target:
                j=midr-1
            else:
                break
        if not (i<=j):
            return False ## all possible iterations done on rows and pointers crossed each other thus while loop eneded implies unable to find row itself
        res=search(matrix[midr],target)
        return res

        