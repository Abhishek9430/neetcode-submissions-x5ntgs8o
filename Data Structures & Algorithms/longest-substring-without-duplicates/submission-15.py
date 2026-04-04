class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        dup=set()
        l = 0
        lmax=0
        for i in range(len(string)):
            while string[i] in dup:
                dup.remove(string[l])
                l+=1
            
            dup.add(string[i])
            lmax=max(lmax,i-l+1)
        return lmax
