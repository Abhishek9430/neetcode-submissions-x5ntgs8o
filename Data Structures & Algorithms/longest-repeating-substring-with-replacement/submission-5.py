class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def mostfreq(d):
            mf=0
            for val in d.values():
                mf=max(mf,val)
            return mf
        
        d={}
        l=0
        m=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            window=r-l+1
            if window-mostfreq(d)<=k:
                m=max(m,window)
            else:
                d[s[l]]-=1
                l+=1
        return m