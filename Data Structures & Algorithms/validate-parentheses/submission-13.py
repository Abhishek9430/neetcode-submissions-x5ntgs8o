class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_to_open = {'}':'{',']':'[',')':'('}
        for b in s:
            if b in close_to_open.values():
                stack.append(b)
            elif b in close_to_open.keys():
                if stack and stack[-1]==close_to_open[b]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0                 
        