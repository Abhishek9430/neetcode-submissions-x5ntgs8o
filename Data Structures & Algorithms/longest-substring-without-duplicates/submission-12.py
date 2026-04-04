class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        i,j=0,0
        lmax=0
        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                lmax=max(lmax,j-i+1)
                j+=1
            else:
                seen.remove(s[i])
                i+=1
        return lmax
