class Solution:
    def trap(self, heights: List[int]) -> int:
        # 2 pointers
        i=0
        j=len(heights)-1
        lm=heights[i]
        rm=heights[j]
        area=0
        while i < j:
            if lm < rm:
                i+=1
                lm=max(lm,heights[i]) #new lm
                small_area=lm-heights[i] # formula=> min(lm,rm)-heights[i] in this case it is known min(lm,rm) is lm by condition if lm<rm
                if small_area>0:
                    area+=small_area
            else:
                j-=1
                rm=max(rm,heights[j])
                small_area=rm-heights[j]
                if small_area>0:
                    area+=small_area
        return area

        # prefix and suffix array
        # lm=[0]*len(heights)
        # rm=[0]*len(heights)
        # for idx,val in enumerate(heights):
        #     if idx==0:
        #         lm[idx]=max(val,0)
        #     else:
        #         lm[idx]=max(val,lm[idx-1])
        
        # for i in range(len(heights)-1,-1,-1):
        #     if i==len(heights)-1:
        #         rm[-1]=max(heights[i],0)
        #     else:
        #         rm[i]=max(heights[i],rm[i+1])
                
        # total_area=0
        # for idxh,height in enumerate(heights):
        #     area=min(lm[idxh],rm[idxh])-height
        #     if area>0:
        #         total_area+=area
        
        # return total_area