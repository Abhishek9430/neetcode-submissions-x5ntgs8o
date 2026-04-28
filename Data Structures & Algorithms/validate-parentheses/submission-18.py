class Solution:
    def isValid(self, s: str) -> bool:
        otc = {"}":"{","]":"[",")":"("}
        stack = []

        for bracket in s:
            if stack and bracket in ["}","]",")"] and stack[-1] == otc[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack)==0
        