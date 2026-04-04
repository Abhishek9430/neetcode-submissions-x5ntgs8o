class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            count,mf={},0
            for j in range(i,len(s)):
                lenwindow=j-i+1
                count[s[j]]=count.get(s[j],0)+1
                mf=max(count[s[j]],mf)
                if lenwindow-mf<=k:
                    res=max(res,lenwindow)
        return res
        # def mostfreq(d):
        #     mf=0
        #     for val in d.values():
        #         mf=max(mf,val)
        #     return mf

        # freq={}
        # l=0
        # res=0
        # for r in range(len(s)):
        #     freq[s[r]]=freq.get(s[r],0)+1
        #     if (r-l+1)-mostfreq(freq)<=k:
        #         res=max(res,r-l+1)
        #     else:
        #         freq[s[l]]-=1
        #         l+=1
        # return res


