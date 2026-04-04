class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]

        prev=1
        for p in range(len(nums)):
            prev=prev*nums[p]
            result.append(prev)

        post=1
        for q in range(len(nums)-1,-1,-1):
            if q==0:
                result[q]=post
            else:
                result[q]=result[q-1]*post
                post*=nums[q]


        return result