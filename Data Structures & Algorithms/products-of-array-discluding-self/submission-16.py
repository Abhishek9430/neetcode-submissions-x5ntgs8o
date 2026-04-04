class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]

        q=1
        for j in range(len(nums)-2,-1,-1):
            q*=nums[j+1]
            res[j]=res[j]*q
        
        return res



        