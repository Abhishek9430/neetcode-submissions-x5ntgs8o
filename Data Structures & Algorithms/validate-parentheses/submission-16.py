class Solution:
    def isValid(self, s: str) -> bool:
        otc={"}":"{","]":"[",")":"("}
        stack = []
        for bracket in s:
            print(stack,":",bracket)
            if stack and stack[-1] == otc.get(bracket,""):
                stack.pop()
            else:
                stack.append(bracket)
        if not stack:
            return True
        return False
        