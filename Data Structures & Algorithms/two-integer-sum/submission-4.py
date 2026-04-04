class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_helper=[(val,index) for index,val in enumerate(nums)]
        nums_helper.sort(key=lambda x: x[0])
        i=0
        j=len(nums)-1

        while i<j:
            if nums_helper[i][0]+nums_helper[j][0]<target:
                i+=1
            elif nums_helper[i][0]+nums_helper[j][0]>target:
                j-=1
            else:
                return [min(nums_helper[i][1],nums_helper[j][1]),max(nums_helper[i][1],nums_helper[j][1])]
        return [-1,-1]
        