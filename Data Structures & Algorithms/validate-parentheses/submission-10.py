class Solution:
    def isValid(self, s: str) -> bool:
        openToClose={')':'(','}':'{',']':'['}


        stack=[]
        for b in s:
            if b in openToClose.values():
                stack.append(b)
            elif b in openToClose.keys():
                if stack and stack[-1]==openToClose[b]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
                    
        