class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token in {"+","-","/","*"}:
                a=int(stack.pop())
                b=int(stack.pop())

                if token=="+":
                    stack.append(a+b)
                elif token=="-":
                    stack.append(b-a)
                elif token=="/":
                    stack.append(b/a)
                elif token=="*":
                    stack.append(a*b)

            else:
                stack.append(token)
        return int(stack[-1])

                
        