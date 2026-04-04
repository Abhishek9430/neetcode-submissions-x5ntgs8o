class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i,j,target):
            res=[]
            while i<j:
                if nums[i]+nums[j]<target:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                elif nums[i]+nums[j]==target:
                    res.append([nums[i],nums[j],-1*target])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
            return res

        
        nums.sort()
        seen=set()
        res=[]
        print(nums)
        for index,val in enumerate(nums):
            if val in seen:
                continue
            pair=twoSum(index+1,len(nums)-1,-1*val)
            if pair:
                res.extend(pair)
            seen.add(val)
        return res
        