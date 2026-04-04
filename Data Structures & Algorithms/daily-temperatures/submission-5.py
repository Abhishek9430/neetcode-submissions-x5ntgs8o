class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                small_index,small_temp = stack.pop()
                res[small_index] = (index-small_index)
            stack.append([index,temp])
        return res
        