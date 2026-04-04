class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i=0
        j=i
        ml=0
        charset=set()
        while j<len(s):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1
            charset.add(s[j])
            ml=max(ml,j+1-i)
            j+=1
        return ml

        