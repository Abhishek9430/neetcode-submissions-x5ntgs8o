class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter={}
        for num in nums:
            counter[num]=counter.get(num,0)+1
        
        for _,value in counter.items():
            if value > 1:
                return True
        return False
        