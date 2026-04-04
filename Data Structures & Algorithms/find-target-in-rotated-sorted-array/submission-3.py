class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot index
        def pivot(array):
            i=0
            j=len(array)-1
            while i<j:
                mid=i+(j-i)//2
                if array[j]<array[mid]:
                    i=mid+1 # mid is not the candidate since something smaller exists
                else:
                    j=mid # mid can be candidate since j is greater thus mid can be smallest
            return i
        
        # break the array into 2 and search in both sorted arrays
        def search(i,j,nums):
            while i<=j:
                mid=i+(j-i)//2
                if nums[mid]>target:
                    j=mid-1
                elif nums[mid]<target:
                    i=mid+1
                else:
                    return mid
            return -1
        p=pivot(nums)
        if p<len(nums):
            search_a=search(p,len(nums)-1,nums)
            if search_a!=-1:
                return search_a
        if p>0:
            search_b=search(0,p-1,nums)
            if search_b!=-1:
                return search_b
        return -1





        