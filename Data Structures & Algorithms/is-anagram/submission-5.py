class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_arr=[0]*26
        if len(s)!=len(t):
            return False

        for i,j in zip(range(len(s)),range(len(t))):
            ords=ord('a')-ord(s[i])
            ordt=ord('a')-ord(t[j])
            freq_arr[ords]+=1
            freq_arr[ordt]-=1
        
        for val in freq_arr:
            if val!=0:
                return False
        return True
