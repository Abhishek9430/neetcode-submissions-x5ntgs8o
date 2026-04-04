class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for idx,val in enumerate(nums):
            if target-val in visited:
                return [visited[target-val],idx]
            visited[val]=idx

        