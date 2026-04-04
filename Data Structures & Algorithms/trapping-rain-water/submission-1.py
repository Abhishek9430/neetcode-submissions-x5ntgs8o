class Solution:
    def trap(self, heights: List[int]) -> int:
        lm=[0]*len(heights)
        rm=[0]*len(heights)
        for idx,val in enumerate(heights):
            if idx==0:
                lm[idx]=max(val,0)
            else:
                lm[idx]=max(val,lm[idx-1])
        
        for i in range(len(heights)-1,-1,-1):
            if i==len(heights)-1:
                rm[-1]=max(heights[i],0)
            else:
                rm[i]=max(heights[i],rm[i+1])
                
        total_area=0
        for idxh,height in enumerate(heights):
            area=min(lm[idxh],rm[idxh])-height
            if area>0:
                total_area+=area
        
        return total_area