class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        result=[]

        prev=1
        for p in range(len(nums)):
            prev=prev*nums[p]
            prefix[p]=prev

        post=1
        for q in range(len(nums)-1,-1,-1):
            post=post*nums[q]
            postfix[q]=post

        for i in range(len(nums)):
            if i==0:
                result.append(postfix[1])
            elif i==len(nums)-1:
                result.append(prefix[-2])
            else:
                result.append(prefix[i-1]*postfix[i+1])

        return result