class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest=0
        for i in range(len(nums)):
            sub=1
            diff=1
            for j in range(i,len(nums)):
                if nums[j]-nums[i]==diff:
                    print(nums[j],nums[i],sub)
                    sub+=1
                    diff+=1
            longest=max(longest,sub)
        return longest
                

        