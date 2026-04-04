class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums,target,i,j):
            res=[]
            while i<j:
                if nums[i]+nums[j]<target:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                else:
                    res.append([nums[i],nums[j],-1*target])
                    i+=1
                    j-=1
                    while i < j and nums[i]==nums[i-1]:
                        i+=1
            return res
        
        nums.sort()
        res=[]
        seen=set()
        for index,num in enumerate(nums):
            if num in seen:
                continue
            target=-1*num
            small_res=twoSum(nums,target,index+1,len(nums)-1)
            if small_res:
                res.extend(small_res)
            seen.add(num)
        return res
        