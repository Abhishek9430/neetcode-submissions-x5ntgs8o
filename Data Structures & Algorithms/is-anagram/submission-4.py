class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*(26)
        for char in s:
            freq[ord(char)-ord('a')]+=1
        
        for ch in t:
            freq[ord(ch)-ord('a')]-=1

        for val in freq:
            if val!=0:
                return False
        return True
        