class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        arr=[0 for i in range(256)]
        
        for s_ in s:
            arr[ord(s_)]+=1
        
        for t_ in t:
            arr[ord(t_)]-=1
        
        total=0
        for a in arr:
            if a!=0:
                return False
        return True