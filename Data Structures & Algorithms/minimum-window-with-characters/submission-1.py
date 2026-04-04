class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        count,window={},{}

        for char in t:
            count[char]=count.get(char,0)+1

        have,need=0,len(count)
        i,j=0,0
        res,rlen=[i,j],float("inf")
        while j<len(s):
            char=s[j]
            window[char]=window.get(char,0)+1

            if char in count and count[char]==window[char]:
                have+=1

            while have==need:
                # update result
                if (j+1-i)<rlen:
                    res,rlen=[i,j],(j+1-i)
                
                # shrink  window
                window[s[i]]-=1
                if s[i] in count and window[s[i]]<count[s[i]]:
                    have-=1
                i+=1
            j+=1
            
        l,r=res
        return s[l:r+1] if rlen!=float("inf") else ""

                


                    
                
                
                

            
        