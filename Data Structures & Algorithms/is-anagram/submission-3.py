class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        arr=[0 for i in range(123)]
        
        for i in range(len(s)):
            arr[ord(s[i])]+=1
            arr[ord(t[i])]-=1
        
        total=0
        for a in arr:
            if a!=0:
                return False
        return True