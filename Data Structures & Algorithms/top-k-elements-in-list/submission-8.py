class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        
        res=[]
        for i in range(k):
            maxf=0
            maxk=-1
            for key,freq in d.items():
                if freq>maxf:
                    maxf=freq
                    maxk=key
            res.append(maxk)
            del d[maxk]
        return res
