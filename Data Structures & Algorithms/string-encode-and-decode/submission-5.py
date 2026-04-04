class Solution:

    def encode(self, strs: List[str]) -> str:
        string=''
        for word in strs:
            string+=str(len(word))+'#'+word
        return string

    def decode(self, s: str) -> List[str]:
        res=[]
        i,j=0,0
        while i<len(s):
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            res.append(s[i:j])
            i=j
        return res

