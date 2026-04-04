class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i,j,target):
            res = []
            while i < j:
                if nums[i] + nums[j] < target:
                    i+=1
                elif nums[i] + nums[j] > target:
                    j-=1
                elif nums[i] +  nums[j] == target:
                    res.append([nums[i],nums[j],-1*target])
                    while i+1 < len(nums) and nums[i]==nums[i+1]:
                        i+=1
                    i+=1
                    j-=1
            return res

        nums.sort()
        result = []
        seen = set()
        for index,value in enumerate(nums):
            if value in seen:
                continue
            seen.add(value)
            target = -1*value
            combinations = twoSum(index+1,len(nums)-1,target)
            if combinations:
                result.extend(combinations)

        return result



        