class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def mostFrequent(d):
            mf=0
            for val in d.values():
                mf=max(mf,val)
            return mf

        i=0
        j=0
        d={}
        res=0
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            if (j+1-i)-mostFrequent(d)>k:
                d[s[i]]=d[s[i]]-1
                i+=1
            res=max(res,j+1-i)
            j+=1
        return res
        