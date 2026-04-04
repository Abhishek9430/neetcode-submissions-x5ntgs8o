class Solution:
    def isValid(self, s: str) -> bool:
        otc={'}':'{',']':'[',')':'('}
        
        stack=[]
        for b in s:
            if stack and otc.get(b,"")==stack[-1]:
                stack.pop()
            else:
                stack.append(b)
        return len(stack)==0
        
        