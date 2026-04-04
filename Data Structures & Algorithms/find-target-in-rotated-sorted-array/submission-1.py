class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def pivot(nums):
            i=0
            j=len(nums)-1
            while i<j:
                mid=i+(j-i)//2
                if nums[j]<nums[mid]:
                    i=mid+1
                else:
                    j=mid
            return j

        def bsearch(l,r,target):
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                elif nums[mid]==target:
                    return mid
            return -1

        p=pivot(nums)
        res=bsearch(0,p-1,target)
        if res!=-1:
            return res
        return bsearch(p,len(nums)-1,target)



        