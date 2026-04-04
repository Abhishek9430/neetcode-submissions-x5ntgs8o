class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        d={
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack=[]
        for i in range(len(s)):
            if s[i] in d: # searches in key
                if len(stack)>0 and stack[-1]==d[s[i]]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(s[i])
        return True if not stack else False
            

        