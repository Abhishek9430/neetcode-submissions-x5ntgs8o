class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tups=[0]*26
        for char in s1:
            tups[ord('a')-ord(char)]+=1
        tups=tuple(tups)


        j=len(s1)
        for i in range(len(s2)):
            s=s2[i:i+j]
            st=[0]*26
            for c in s:
                st[ord('a')-ord(c)]+=1
            st=tuple(st)
            if st==tups:
                return True
        return False


                
        