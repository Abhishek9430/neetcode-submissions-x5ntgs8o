class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_to_open = {'}':'{',']':'[',')':'('}
        for b in s:
            if stack and close_to_open.get(b,"")==stack[-1]:
                stack.pop()
            else:
                stack.append(b)
        return len(stack)==0