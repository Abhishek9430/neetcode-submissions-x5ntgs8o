class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lpa=[1]*len(nums)

        for i in range(len(nums)-1):
            lpa[i+1]=lpa[i]*nums[i]

        
        rp=1
        for i in range(len(nums)-1,-1,-1):
            lpa[i]=lpa[i]*rp
            rp=rp*nums[i]
        
        return lpa
        