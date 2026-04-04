class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=[1]*len(nums) # prefix
        right_product=[1]*len(nums) # postfix
        
        left_product[0]=nums[0]
        right_product[-1]=nums[-1]
        for i in range(1,len(nums)):
            left_product[i]=left_product[i-1]*nums[i]

        for j in range(len(nums)-2,-1,-1):
            right_product[j]=right_product[j+1]*nums[j]
        
        print(left_product)
        print(right_product)
        # get product
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(right_product[1])
            elif i==len(nums)-1:
                res.append(left_product[-2])
            else:
                res.append(left_product[i-1]*right_product[i+1])
        return res

            