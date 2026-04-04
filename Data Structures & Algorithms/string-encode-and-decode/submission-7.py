class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for word in strs:
            res+=str(len(word))+"#"+word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        res=[]
        while i<len(s):
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            res.append(s[i:j])
            i=j
        return res
