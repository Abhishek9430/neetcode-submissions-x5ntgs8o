class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,i,j,target):
            res=[]
            while i<j:
                if arr[i]+arr[j]<target:
                    i+=1
                elif arr[i]+arr[j]>target:
                    j-=1
                else:
                    res.append([arr[i],arr[j],-1*target])
                    i+=1
                    j-=1
                    while i<j and arr[i]==arr[i-1]:
                        i+=1
            return res
        
        nums.sort()
        res=[]
        for index,val in enumerate(nums):
            if index>0 and nums[index]==nums[index-1]:
                continue
            if val>0:
                return res
            result=twoSum(nums,index+1,len(nums)-1,-1*val)
            res.extend(result)
        return res

            