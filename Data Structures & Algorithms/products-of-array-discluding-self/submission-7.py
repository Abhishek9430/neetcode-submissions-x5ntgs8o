class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)

        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]

        res=[0]*(len(nums))
        post=1
        for i in range(len(nums)-1,-1,-1):
            if i ==  len(nums)-1:
                res[i]=prefix[i]
            else:
                post*=nums[i+1]
                res[i]=prefix[i]*post
        return res 

            