class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[0]*len(nums)
        right=[0]*len(nums)

        left[0]=nums[0]
        right[-1]=nums[-1]

        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i]
        
        for j in range(len(nums)-2,-1,-1):
            right[j]=right[j+1]*nums[j]
        

        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(right[1])
            elif i==len(nums)-1:
                res.append(left[-2])
            else:
                res.append(left[i-1]*right[i+1])
        return res
        