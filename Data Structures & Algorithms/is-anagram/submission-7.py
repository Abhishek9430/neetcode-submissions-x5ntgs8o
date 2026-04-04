class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        freq = [0]*26
        for char in s.lower():
            freq[ord(char)-ord('a')]+=1
        
        for new_char in t.lower():
            freq[ord(new_char)-ord('a')]-=1
        
        for index,val in enumerate(freq):
            if val!=0:
                return False
        return True
        

        