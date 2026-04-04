class Solution:
    def nxtminm(self,heights):
        stack=[-1]
        res=[-1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack[-1]!=-1 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            res[i]=stack[-1]
            stack.append(i)
        return res

    def prevminm(self,heights):
        stack=[-1]
        res=[-1]*len(heights)
        for i in range(0,len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            res[i]=stack[-1]
            stack.append(i)
        return res

    def largestRectangleArea(self,heights):
        if len(heights)==1:
            return heights[0]
        rightextensions=self.nxtminm(heights)
        leftextensions=self.prevminm(heights)
        area=-1
        for i in range(len(heights)):
            l=heights[i]
            re=rightextensions[i]
            le=leftextensions[i]
            if re ==-1:
                re=len(heights)
            b=re-le-1
            area=max(area,l*b)
        return area



        