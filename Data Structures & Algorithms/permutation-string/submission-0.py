class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        i=0
        j=i+len(s1)
        d={}
        for c in s1:
            d[c]=d.get(c,0)+1
            
        while j<=len(s2):
            d_temp={}
            for k in range(i,j):
                d_temp[s2[k]]=d_temp.get(s2[k],0)+1
            
            if d==d_temp:
                return True
            d_temp={}
            i+=1
            j+=1
        return False



        

        

        