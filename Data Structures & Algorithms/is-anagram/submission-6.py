class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t): return False
        counter=[0]*26

        for cs,ct in zip(s,t):
            counter[ord(cs)-ord('a')]+=1
            counter[ord(ct)-ord('a')]-=1
        
        for c in counter:
            if c>0:
                return False
        return True