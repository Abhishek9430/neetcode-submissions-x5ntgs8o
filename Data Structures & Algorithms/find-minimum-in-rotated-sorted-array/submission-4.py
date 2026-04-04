class Solution:
    def findMin(self, nums: List[int]) -> int:
        ### find rotation
        i=0
        j=len(nums)-1

        while i<j:
            mid=i+(j-i)//2
            if nums[j]<=nums[mid]:
                i=mid+1
            else:
                j=mid
        return nums[j]
        