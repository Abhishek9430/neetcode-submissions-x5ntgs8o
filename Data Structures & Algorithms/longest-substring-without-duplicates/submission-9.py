class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        i=0
        j=0
        ml=0
        while j < len(s):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1
            charset.add(s[j])
            ml=max(ml,j+1-i)
            j+=1
        return ml
        