class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tup=[0]*26
        for char in s1:
            tup[ord(char)-ord('a')]+=1
        
        tup=tuple(tup)

        maxl=len(s1)
        for r,val in enumerate(s2):
            string=s2[r:r+maxl]
            tup_s=[0]*26
            for small_char in string:
                tup_s[ord(small_char)-ord('a')]+=1
            tup_s=tuple(tup_s)
            if tup_s==tup:
                return True
        return False
        