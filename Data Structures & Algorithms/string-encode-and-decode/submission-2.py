class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res


    def decode(self, string: str) -> List[str]:
        res=[]
        i=0
        while i<len(string):
            j=i
            while string[j]!='#':
                j+=1
            l=int(string[i:j])
            i=j+1
            j=i+l
            res.append(string[i:j])
            i=j
        return res
            
