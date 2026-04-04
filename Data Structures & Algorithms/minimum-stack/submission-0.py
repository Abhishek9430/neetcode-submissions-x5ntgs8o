class MinStack:

    def __init__(self):
        self.min_val={}
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        index=len(self.stack)-1
        if index==0:
            self.min_val[index]=val
        else:
            self.min_val[index]=min(self.min_val[index-1],val)
        return
        
        
    def pop(self) -> None:
        index=len(self.stack)-1
        self.stack.pop()
        if index>=0:
            del self.min_val[index]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.min_val)>0:
            index=len(self.stack)-1
            return self.min_val[index]
        
