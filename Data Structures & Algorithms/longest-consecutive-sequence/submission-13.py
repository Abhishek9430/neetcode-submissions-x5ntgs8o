class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={k:0 for k in nums}
        minm=10000
        maxlen=0
        for i in range(len(nums)):
            val=nums[i]
            length=1
            while val-1 in d:
                length+=1
                val-=1
            maxlen=max(length,maxlen)
        return maxlen
            