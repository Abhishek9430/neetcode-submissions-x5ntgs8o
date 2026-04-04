class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                s=0
                for i in range(2):
                    s+=int(stack.pop())
                stack.append(s)
            elif token=="-":
                rev_stack=[]
                for i in range(2):
                    rev_stack.append(int(stack.pop()))
                diff=rev_stack.pop()
                while rev_stack:
                    diff-=rev_stack.pop()
                stack.append(diff)
            elif token=="*":
                m=1
                for i in range(2):
                    m*=int(stack.pop())
                stack.append(m)
            elif token=="/":
                rev_stack_div=[]
                for i in range(2):
                    rev_stack_div.append(int(stack.pop()))
                div=rev_stack_div.pop()
                while rev_stack_div:
                    div/=rev_stack_div.pop()
                stack.append(div)
            else:
                stack.append(token)
        
        return int(stack[-1])

                
        